from django.contrib import admin

# Register your models here.
from .models import Category, News, Comment

admin.site.register(Category)

# creating the class news to see the views in admin panel 

class AdminNews(admin.ModelAdmin):
    list_display =('title','category', 'add_time')
# we need to register the class AdminNews in the register model 
# as shown bellow :-

admin.site.register(News, AdminNews)

#modifying the comment models for the  admin panel.

class AdminComment(admin.ModelAdmin):
    list_display = ('news', 'name', 'email','comment','status' )
admin.site.register(Comment,AdminComment)