from image_cropping import ImageCroppingMixin

from django.contrib import admin

from blog.models import BlogPost


class BlogPostAdmin(ImageCroppingMixin, admin.ModelAdmin):

    list_display = (
        'title',
        'created_date',
        'published_date',
        # 'spot',
        'admin_blogpost_photo_thumb',
        # 'user'
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
                    'blogpost_photo',
                    # 'spot',
                    'admin_blogpost_photo_thumb',
                    # 'user',
                ]
            }),
    ]

    readonly_fields = (
        'admin_blogpost_photo_thumb',
        'post_slug',
    )


admin.site.register(BlogPost, BlogPostAdmin)
