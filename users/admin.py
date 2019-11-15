from django.contrib import admin
from .models import Book, UserProfile
# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass

