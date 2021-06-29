from django.shortcuts import render
from .models import Hospital


def hospital(request):
    hospital_list = Hospital.objects.all()
    print(hospital_list)

    return render(
        request, 'secondapp/hospital_list.html', 
        {'hospital_list': hospital_list}
    )
