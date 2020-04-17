from django.contrib import admin
from .models import WallpaperImg, Categories, Comment, Carousel

# Register your models here.


admin.site.register(WallpaperImg)
admin.site.register(Categories)
admin.site.register(Carousel)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'comment', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('user', 'comment')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
