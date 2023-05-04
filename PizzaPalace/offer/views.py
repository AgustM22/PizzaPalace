from django.shortcuts import render
from django.http import JsonResponse
from pizza.models import Offer 

def main(request):
    context = {'offers': Offer.objects.all()}
    return render(request, "offer.html", context)

def filter(request):
    if request.method == 'GET':
        filter = request.GET['filter']
        context = Offer.objects.filter(name__icontains=filter)
        Offerlis = []
        for object in context:
            templis = {"id": object.id, "name": object.name, "description": object.description, "price": object.price, "pic": object.pic}
            Offerlis.append(templis)

        return JsonResponse(Offerlis, safe=False)