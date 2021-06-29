from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("BRAND PAGE.")

def template_index(request):
    print("PAGE : template_index")
    return render(request, './brand/index.html')