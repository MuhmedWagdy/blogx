from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import Post,Comment


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ['title','created_date','draft','author']
    list_filter = ['draft','author']

class CommentAdmin(admin.ModelAdmin):
    list_display =  ['user','post','created_at']







admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
