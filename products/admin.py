from django.contrib import admin
from . models import Comment
from . models import Product
from .models import Category


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Comment)
