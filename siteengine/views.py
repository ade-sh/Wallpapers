import mimetypes
from wsgiref.util import FileWrapper

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from .forms import CommentForm
from .models import Categories, WallpaperImg, Carousel


# Create your views here.


def index(request):
    categoryset = Categories.objects.all()
    wallpaperset = WallpaperImg.objects.all()
    carousel = Carousel.objects.all()
    paginator = Paginator(wallpaperset, 25)
    page_number = 1
    num_pages = paginator.num_pages
    page_set = {page_number - 1, page_number, page_number + 1}
    page_obj = paginator.get_page(page_number)
    return render(request, template_name="siteengine/index.html",
                  context={'categoryset': categoryset, "carousel": carousel, 'wallpaperset': page_obj,
                           "page_number": page_number,
                           "page_set": page_set, "num_pages": num_pages})


def browsepages(request, page):
    categoryset = Categories.objects.all()
    wallpaperset = WallpaperImg.objects.all()
    paginator = Paginator(wallpaperset, 25)
    num_pages = paginator.num_pages
    page_number = page
    page_obj = paginator.get_page(page_number)
    page_set = {page - 1, page, page + 1}
    return render(request, template_name="siteengine/browserPages.html",
                  context={'categoryset': categoryset, 'wallpaperset': page_obj, "page_number": page_number,
                           "page_set": page_set, "num_pages": num_pages})


def browse_category(request, categ, page):
    wallpaperset = WallpaperImg.objects.filter(category__category_name=categ)
    paginator = Paginator(wallpaperset, 25)  # Show 25 contacts per page.
    num_pages = paginator.num_pages
    page_number = page
    page_obj = paginator.get_page(page_number)
    page_set = {page - 1, page, page + 1}
    return render(request, template_name="siteengine/browserPages.html",
                  context={'wallpaperset': page_obj, "page_number": page_number,
                           "page_set": page_set, "num_pages": num_pages})


def wallpaper_description_page(request, wid):
    comment_form = CommentForm()
    wallpaperset = WallpaperImg.objects.get(id=wid)
    comments = wallpaperset.comments.filter(active=True)
    new_comment = None
    no_login = None
    if request.method == 'POST':
        if request.user.is_authenticated:
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                # Assign the current post to the comment
                new_comment.post = wallpaperset
                new_comment.user = request.user
                # Save the comment to the database
                new_comment.save()
        else:
            no_login = 'no_login'
    return render(request, template_name="siteengine/WallpaperDescription.html",
                  context={'wallpaperimg': wallpaperset, 'comments': comments,
                           'new_comment': new_comment,
                           'comment_form': comment_form, "no_login": no_login, })


def download_image(request, product_id):
    wall_image = WallpaperImg.objects.get(id=product_id)
    product_image_url = wall_image.image.path
    product_image_name = wall_image.image.url

    wrapper = FileWrapper(open(product_image_url, 'rb'))
    response = HttpResponse(wrapper)
    response['Content-Disposition'] = "attachment; filename=%s" % product_image_name
    return response
