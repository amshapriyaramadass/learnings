from django.shortcuts import render

def hello(request):
   return render(request, "myapp/template/hello.html", {})
# Create your views here.
