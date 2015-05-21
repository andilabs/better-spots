from image_cropping import ImageCroppingMixin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from django.contrib import admin

from blog.models import Post


class PostResource(resources.ModelResource):

    class Meta:
        model = Post


class BlogPostAdmin(
        ImportExportModelAdmin, ImageCroppingMixin, admin.ModelAdmin):

    resource_class = PostResource

    list_display = (
        'title',
        'created_date',
        'published_date',
        'spot',
        'admin_blogpost_photo_thumb',
        'user'
    )

    fieldsets = [
        ('Post',
            {
                'fields':
                [
                    'title',
                    'created_date',
                    'published_date',
                    'spot',
                    'admin_blogpost_photo_thumb',
                    'user'
                ]
            }),
    ]

    readonly_fields = (
        'admin_blogpost_photo_thumb',
        'post_slug')


admin.site.register(Post, BlogPostAdmin)
