from django.contrib import admin

from .models import Category, Location, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'created_at')


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
