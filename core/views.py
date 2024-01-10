from django.shortcuts import render
from .models import WheelItem
# Create your views here.

def spin_wheel(request):
    wheel_items = WheelItem.objects.all()
    context = {
    	'wheel_items': wheel_items
    }
    return render(request, 'core/dashboard.html', context)
