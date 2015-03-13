from image_cropping import ImageCroppingMixin

from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from core.models import Spot, Rating, Opinion, OpinionUsefulnessRating, UsersSpotsList
from accounts.models import SpotUser
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
    hstore_fields = [field['name'] for field in settings.HSTORE_SCHEMA]

    list_display = ['name', 'friendly_rate', 'address_city', 'is_enabled', 'is_certificated'] + hstore_fields
    list_filter = ('address_city', 'is_enabled', 'spot_type')
    search_fields = ['name', 'address_city', 'address_street']
    exclude = ('location',)
    readonly_fields = ['is_enabled', 'friendly_rate', 'spot_slug'] + hstore_fields

    fieldsets = (
        (None, {'fields': ('name', 'spot_type', 'is_certificated')}),
        ('Address', {'fields': ('address_street','address_number', 'address_city','address_country')}),
        ('Contact details', {'fields': ('phone_number', 'email', 'www', 'facebook')}),
        ('Photo', {'fields': ('venue_photo', 'cropping_venue_photo')}),
        ('Evaluations and facilities calculated based on ratings', {'fields': tuple(['friendly_rate', 'is_enabled']+hstore_fields)})
    )




class UsersSpotsListAdmin(admin.ModelAdmin):
    list_filter = ('role', 'user',)

admin.site.register(SpotUser, SpotUserAdmin)
admin.site.register(Spot, SpotAdmin)
admin.site.register(Rating)
admin.site.register(Opinion)
admin.site.register(OpinionUsefulnessRating)
admin.site.register(UsersSpotsList, UsersSpotsListAdmin)