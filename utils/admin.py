
from django.contrib import admin

from utils.models import Tag


class TagAdmin(admin.ModelAdmin):

    list_display = (
        'text',
    )


admin.site.register(Tag, TagAdmin)
