from django.contrib import admin
from .models import Author,Post,Tag, Comment

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","date","author",)
    list_filter = ("author","tag","date",)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Author)
admin.site.register(Post,BlogAdmin)
admin.site.register(Tag)
admin.site.register(Comment)

