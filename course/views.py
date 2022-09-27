from django.shortcuts import render
from .forms import User
from Backend.backend import Usis
import time
# Create your views here.
def home(request):
    return render(request,'index.html')

def data_render(request):
    l=[]
    if request.method=="POST":
        from1 = User(request.POST)
        if from1.is_valid():
            email=from1.cleaned_data['email']
            psd = from1.cleaned_data['psd']
            ayear= from1.cleaned_data['ayear']
            asession =from1.cleaned_data['asession']
            course = from1.cleaned_data['course']
            with Usis() as bot:
                bot.land_first_page()
                bot.login(email,psd)
                bot.seat_status_option()
                bot.seat_stattus_selection(ayear, asession)
                time.sleep(45)
                bot.input_course(course)
                table = bot.courses_list()
            return render(request,'hi.html', {'table':table})
