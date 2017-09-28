from django.db import models
import datetime
# Create your models here.
class Restaurant(models.Model):

    title = models.CharField(max_length=30, help_text="Restaurant name")
    city = models.CharField(max_length=20, help_text="City", null=True)

    def __str__(self):

        return '{}, {}'.format(self.title, self.city)

class Category(models.Model):

    title = models.CharField(max_length=200, help_text="Enter category name")

    def __str__(self):

        return self.title

class SubCategory(models.Model):

    title = models.CharField(max_length=200, help_text="Enter subcategory name")
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    def __str__(self):

        return self.title

class Dish(models.Model):

    title = models.CharField(max_length=200, help_text="Dish name")
    price = models.CharField(max_length=10, help_text="Dish price", null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey('SubCategory', on_delete=models.SET_NULL, null=True)

    def __str__(self):

        return '{}, Price: {}, Category: {}, SubCategory: {}'.format(self.title, self.price, self.category, self.subcategory)

class Worker(models.Model):
    name = models.CharField(max_length=30, help_text='worker name')
    patromymic = models.CharField(max_length=30, help_text='worker patronymic', null=True)
    surname = models.CharField(max_length=30, help_text='worker surname')
    place = models.ForeignKey('Restaurant', on_delete=models.SET_NULL, null=True)

    def __str__(self):

        return 'Name: {}, Patronymic: {}, Surname: {}, Restaurant: {}'.format(self.name, self.patromymic, self.surname, self.place)