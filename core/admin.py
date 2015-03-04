from image_cropping import ImageCroppingMixin

from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import SpotUser, Spot, Raiting, Opinion, OpinionUsefulnessRating
from accounts.forms import UserCreationForm, UserChangeForm


class SpotUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'mail_verified', 'is_admin')
    list_filter = ('is_admin', 'mail_verified')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'mail_verified')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'mail_verified', 'password1', 'password2')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


class SpotAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['name', 'friendly_rate', 'address_city', 'is_enabled'] + [field['name'] for field in settings.HSTORE_SCHEMA]
    list_filter = ('address_city', 'is_enabled')
    search_fields = ['name', 'address_city', 'address_street']
    exclude = ('location',)
    readonly_fields = ['spot_slug'] + [field['name'] for field in settings.HSTORE_SCHEMA]


admin.site.register(SpotUser, SpotUserAdmin)
admin.site.register(Spot, SpotAdmin)
admin.site.register(Raiting)
admin.site.register(Opinion)
admin.site.register(OpinionUsefulnessRating)
