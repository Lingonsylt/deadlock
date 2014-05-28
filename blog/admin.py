from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'publish',)
    search_fields = ('title', 'publish')
    list_filter = ['pub_date', 'publish']
    fieldsets = [
        ("Details", {'fields': ['title', 'publish', 'pub_date'], 'classes': ('grp-collapse grp-closed', 'collapse')}),
        ('Blog Entry', {'fields': ['entry'], 'classes': ('grp-collapse grp-closed', 'collapse')}),
    ]

admin.site.register(Post, PostAdmin)
