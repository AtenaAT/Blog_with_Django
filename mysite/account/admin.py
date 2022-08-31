from django.contrib import admin
from .models import CustomUser as User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('mobile', 'age', 'first_name', 'last_name', 'gender')
    list_filter = ('age', 'gender')
    search_fields = ('mobile',)
