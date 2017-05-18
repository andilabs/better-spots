from image_cropping import ImageCroppingMixin

from django.contrib import admin

from blog.models import BlogPost


class BlogPostAdmin(ImageCroppingMixin, admin.ModelAdmin):

    list_display = (
        'title',
        'created_date',
        'published_date',
        'spot',
        'admin_photo_thumb',
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
                    'text',
                    'photo',
                    'spot',
                    'admin_photo_thumb',
                    'user',
                ]
            }),
    ]

    readonly_fields = (
        'admin_photo_thumb',
        'post_slug',
    )


admin.site.register(BlogPost, BlogPostAdmin)
