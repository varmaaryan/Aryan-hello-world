from django.urls import path
from . import views

urlpatterns = [
    path('hello/json/', views.hello_world_json),
    path('hello/', views.hello_world_template),
    path('hello/bold/', views.hello_world_bold),
]
