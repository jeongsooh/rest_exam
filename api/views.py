from django.shortcuts import render

from api.models import Item

# Create your views here.

def index(request):
    if request.method == 'POST':
        temp = request.POST.get('e_data')

        item = Item()
        item.sensor_id = "gre_sensor"
        item.e_data = temp
        item.save()

        return render(request, 'index.html', context={'text':temp})

    return render(request, 'index.html', context={'text':'GET method'})