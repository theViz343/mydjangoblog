from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import BlogPost, CustomTag
# Register your models here.

class CustomTagInline(admin.TabularInline):
    model = BlogPost.custom_tag.through
    verbose_name = 'Tag'
    verbose_name_plural = 'Custom Tags'
    extra = 3

class BlogPostAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = ('post_text',)
    inlines = [CustomTagInline]
    fieldsets = (
        (None, {'fields': ['post_title',] }),
        ('Content', {'fields': ['post_desc','post_text','post_img']}),
        ('Other Information', {'fields': ['post_date','post_tag','featured',]})
    )

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(CustomTag)
