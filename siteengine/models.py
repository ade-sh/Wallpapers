import os
from io import BytesIO

from PIL import Image
from django.core.files.base import ContentFile
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Categories(models.Model):
    category_name = models.CharField(max_length=30)
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.category_name


class WallpaperImg(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField('date published')
    thumbnail = models.ImageField(upload_to='thumbs/', editable=False)

    def save(self, *args, **kwargs):

        if not self.make_thumbnail():
            # set to a default thumbnail
            raise Exception('Could not create thumbnail - is the file type valid?')

        super(WallpaperImg, self).save(*args, **kwargs)

    def make_thumbnail(self):

        photo = Image.open(self.image)
        photo.thumbnail([300, 300], Image.ANTIALIAS)

        thumb_name, thumb_extension = os.path.splitext(self.image.name)
        thumb_extension = thumb_extension.lower()

        thumb_filename = thumb_name + '_thumb' + thumb_extension

        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.gif':
            FTYPE = 'GIF'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return False  # Unrecognized file type

        # Save thumbnail to in-memory file as StringIO
        temp_thumb = BytesIO()
        photo.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)

        # set save=False, otherwise it will run in an infinite loop
        self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()

        return True

    def __str__(self):
        return self.title

    def filename(self):
        return os.path.basename(self.image.name)


class Comment(models.Model):
    post = models.ForeignKey(WallpaperImg, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, max_length=80, on_delete=models.CASCADE)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.user)


class Carousel(models.Model):
    img1 = models.ForeignKey(WallpaperImg, on_delete=models.CASCADE)
