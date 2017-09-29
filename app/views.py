from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from app.models import Dish, Worker, Restaurant, Category, SubCategory
import json
from burger_shop import urls
from simplejson import JSONDecodeError

def disheslist(request, dish_id):
    if request.method == 'GET':
        if dish_id == '0':
            dishes = Dish.objects.all()
            response_data = {}
            temp = []
            count = 0
            for i in dishes:
                temp.append(
                    {'id': i.id,
                     'title': i.title,
                     'price': i.price,
                     })
                count = count + 1
            response_data['dishes'] = temp
            return JsonResponse(response_data)
        else:
            id = dish_id
            dishes = Dish.objects.filter(pk=id)
            response_data = {}
            temp = []
            count = 0
            for i in dishes:
                temp.append(
                    {'id': i.id,
                     'title': i.title,
                     'price': i.price,
                     })
                count = count + 1
            response_data['dishes'] = temp
            return JsonResponse(response_data)
@csrf_exempt
def categorieslist(request, cat_id):
    if request.method == 'GET':
        if cat_id == '0':
            categories = Category.objects.all()
            responce_data = {}
            temp = []
            ids = []
            count = 0
            for c in categories:
                temp.append({
                    'id': c.id,
                    'category': c.title
                })
            responce_data['categories'] = temp
            return JsonResponse(responce_data)
        else:
            id = cat_id
            categories = Category.objects.filter(pk=id)
            responce_data = {}
            temp = []
            ids = []
            count = 0
            for c in categories:
                temp.append({
                    'id': c.id,
                    'category' : c.title
                })
            responce_data['categories'] = temp
            return JsonResponse(responce_data)


def subcats(request, sub_id):
    if request.method == 'GET':
        if sub_id == '0':
            subcategories = SubCategory.objects.all()
            responce_data = {}
            temp = []
            count = 0
            for s in subcategories:
                temp.append({
                    'id': s.id,
                    'subcategory': s.title
                })
            responce_data['subcategories'] = temp
            return JsonResponse(responce_data)
        else:
            id = sub_id
            subcategories = SubCategory.objects.filter(pk=id)
            responce_data = {}
            temp = []
            count = 0
            for s in subcategories:
                temp.append({
                    'id' : s.id,
                    'subcategory' : s.title
                })
            responce_data['subcategories'] = temp
            return JsonResponse(responce_data)

@csrf_exempt
def order(request):
    if request.method == 'POST':
        data_unicode = request.body.decode('utf-8').replace('\0', '')
        data = json.loads(data_unicode)
        custom_decks = data['custom_decks']
        return JsonResponse(custom_decks)
