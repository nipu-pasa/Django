from django.shortcuts import render

# Create your views here.
def home_screen_view(request):
    context = {}
    context['some_string']="this is the some string i am passing to the view"
    context['some_number'] = 123223
    return render(request,"personal/home.html",{})
