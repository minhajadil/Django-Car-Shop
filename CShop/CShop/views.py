from django.shortcuts import render
from cars.models import Car
from cars.models import Brand


def home(request, brand_slug=None):
    data = Car.objects.all()
 
    if brand_slug is not None:
        brand = Brand.objects.get(slug= brand_slug)
        data = Car.objects.filter(brand=brand)

    brand = Brand.objects.all()



    return render(request,'home.html',{'data':data,'brands':brand})