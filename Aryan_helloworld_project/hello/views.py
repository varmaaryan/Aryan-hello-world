from django.shortcuts import render
from django.http import JsonResponse

def hello_world_json(request):
    return JsonResponse({"Message": "Hello World!"})

def hello_world_bold(request):
    return render(request, 'api/hello_world_bold.html')

def hello_world_template(request):
    return render(request, 'api/hello_world.html', {"message": "Hello World!"})
