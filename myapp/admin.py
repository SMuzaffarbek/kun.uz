from django.contrib import admin

from .models import Category, News

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'img', 'view_news']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['category']
    list_display_links = ['title', 'created_at']
    search_fields = ['title', ]
