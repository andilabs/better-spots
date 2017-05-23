from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

from accounts.models import EmailVerification
from .models import User, UserFavouritesSpotList
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
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


class UserFavouritesSpotListAdmin(admin.ModelAdmin):
    list_display = (
        'spot',
        'user',
    )

    list_filter = (
        'user',
        'spot'
    )


class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('verification_key', 'key_timestamp', 'user')


admin.site.register(User, UserAdmin)
admin.site.register(UserFavouritesSpotList, UserFavouritesSpotListAdmin)
admin.site.register(EmailVerification, EmailVerificationAdmin)