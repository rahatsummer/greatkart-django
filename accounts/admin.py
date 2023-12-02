from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name',
                    'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined', 'password')
    ordering = ('-date_joined',)

    # for custom user display case, we need these properties
    filter_horizontal = ()
    list_filter = ()
    # this fieldset properties make my password readonly.
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
