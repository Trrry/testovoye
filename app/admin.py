from django.contrib import admin

# Register your models here.
from app.models import Category, Dish, SubCategory, Restaurant, Worker

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Dish)
admin.site.register(Restaurant)
admin.site.register(Worker)