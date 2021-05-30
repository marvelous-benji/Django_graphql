from django.contrib import admin
from .models import Profile,Tag,Post
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post

    list_display = (
            "id",
            "title",
            "subtitle",
            "slug",
            "published_date",
            "published",
            )
    list_filter = ("published_date","published",)

    list_editable = (
            "title",
            "subtitle",
            "slug",
            "published_date",
            "published",
            )

    search_fields = (
            "title",
            "subtitle",
            "slug",
            "body",
            )

    prepopulated_fields = {
            "slug":("title","subtitle",)
            }

    save_on_top = True
    date_hierarchy = "published_date"
