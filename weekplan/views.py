from django.http import HttpResponse,Http404, JsonResponse
from django.shortcuts import render

from .models import week

# Create your views here.
def home_view(reguest, *args, **kwargs):
    print(args, kwargs)
    #return HttpResponse("<h1>Hello world</h1>")
    return render(reguest, "pages/home.html", context={}, status=200)

def kek_home_view(reguest,week_id, *args, **kwargs):
    
    """
    REST API VIEW
    Consume by JavaScript/Swift/Java/iOS/Android
    return json data
    """
    data = {
        "id" : week_id,
        #"event" : obj.event,
    }


    status = 200
    try:
        obj = week.objects.get(id=week_id)
        data['weekday'] = obj.weekday
    except:
        data['message'] = "Not found"
        status = 404
    
    return JsonResponse(data, status=status) # jason.dumps conten_type='application'