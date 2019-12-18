from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

# Create your views here.

class Homepage(TemplateView):
    """
    This API loads the homepage
    url: /
    """
    def get(self, request, *args, **kwargs):
        payload = {}
        pop_cats = PopularCategories.objects.all()
        visited_places = MostVisitedPlaces.objects.all()
        payload['categories'] = pop_cats
        payload['places'] = visited_places

        self.template_name = 'home/index.html'
        return render(request, self.template_name, payload)

    def post(self, request, *args, **kwargs):
        print("I am here")
        print("My Data - ", request.POST.get('place'))
        place = request.POST.get('place')
        location = request.POST.get('location')
        payload = {}
        visited_places = MostVisitedPlaces.objects.filter(address=place)
        payload['places'] = visited_places
        self.template_name = 'home/listings.html'
        return render(request, self.template_name, {"Message": "Object Created"})

# def Homepage(request):
#     if request.method == 'POST':
#         pass

#     if request.method == 'GET':
#         pop_cats = PopularCategories.objects.all()
#         return render(request, 'home/index.html', {'pop_cats': pop_cats})

class Listings(TemplateView):
    """
    This API loads the homepage
    url: /
    """
    def get(self, request, *args, **kwargs):
        payload = {}
        visited_places = MostVisitedPlaces.objects.all()
        payload['places'] = visited_places
        self.template_name = 'home/listings.html'
        return render(request, self.template_name, payload)


