import os

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
