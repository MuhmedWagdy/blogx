from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import Post,Comment




class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
