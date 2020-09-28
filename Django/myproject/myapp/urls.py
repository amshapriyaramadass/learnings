
from django.urls import path

urlpatterns = [
    path('hello/', 'myapp.views.hello', name = 'hello'),
]


