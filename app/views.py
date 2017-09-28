from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from app.models import Dish, Worker, Restaurant, Category, SubCategory


def disheslist(request):
    if request.method == 'GET':
        dishes = Dish.objects.all()
        response_data = {}
        temp = []
        count = 0
        for i in dishes:
            temp.append(
                {'id': count,
                 'title': i.title,
                 'price': i.price,
                 })
            count = count + 1
        response_data['dishes'] = temp
        return JsonResponse(response_data)
@csrf_exempt
def categorieslist(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        responce_data = {}
        temp = []
        count = 0
        for c in categories:
            temp.append({
                'id': count,
                'category' : c.title
            })
        responce_data['categories'] = temp
        return JsonResponse(responce_data)
def subcats(request):
    if request.method == 'GET':
        subcategories = SubCategory.objects.all()
        responce_data = {}
        temp = []
        count = 0
        for s in subcategories:
            temp.append({
                'id' : count,
                'subcategory' : s.title
            })
        responce_data['subcategories'] = temp
        return JsonResponse(responce_data)
def order(request):
    if request.method == 'POST':
        
