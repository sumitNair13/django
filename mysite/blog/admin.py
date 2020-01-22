from django.contrib import admin
from blog.models import Post,Comment
from blog.models import UserProfileInfo
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserProfileInfo)
