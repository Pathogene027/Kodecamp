from django.shortcuts import render, redirect
from .models import chech_in
from django.views.decorators.csrf import csrf_protect


# Create your views here.

@csrf_protect
def checkit(request):
    if request.method == "POST":
        r_number = request.POST.get("room")
        a_paid = request.POST.get("amount")
        o_name = request.POST.get("occuname")
        o_email = request.POST.get("occumail")
        o_occupation = request.POST.get("occu")
        n_of_n = request.POST.get("night")
        s_date = request.POST.get("start")
        e_date = request.POST.get("end")
        new_data = chech_in(room_number=r_number, amount_paid=a_paid, occupant_name=o_name,
                            occupant_email=o_email, occupant_occupation=o_occupation,
                            number_of_nights=n_of_n, start_date=s_date, end_date=e_date
                            )
        new_data.save()
        return redirect('check:checkit')
    return render(request, 'check/checkin.html')


def login(request):
    if request.method == 'POST':

    return render(request, 'check/web.html')

def logout(request):
    return render(request, 'check/logout.html')
