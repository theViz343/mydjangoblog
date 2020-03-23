from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost
# Register your models here.
class BlogPostAdmin(SummernoteModelAdmin):
    summernote_fields = ('post_text',)
admin.site.register(BlogPost, BlogPostAdmin)
