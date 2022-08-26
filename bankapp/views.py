from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.http import JsonResponse
from .forms import PersonCreationForm
from .models import Person, City


def index(request):
    return render(request, 'index.html')

def branch(request):
    return render(request, 'branch.html')

def ernakulam(request):
    return render(request,'ernakulam.html')

def calicut(request):
    return render(request,'calicut.html')

def trivandrum(request):
    return render(request,'trivandrum.html')

def palghat(request):
    return render(request,'palghat.html')

def thrissur(request):

    return render(request, 'thrissur.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('person_add')
        else:
            messages.info(request,"invalid login")
            return redirect('login')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save();
                return  redirect('login')

        else:
            messages.info(request,"password not matched")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")

def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'accept.html')
    return render(request, 'home.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'home.html', {'form': form})


# AJAX
def load_cities(request):
    district_id = request.GET.get('district_id')
    cities = City.objects.filter(district_id=district_id).all()
    # return render(request, 'city_dropdown_list_options.html', {'cities': cities})
    return JsonResponse(list(cities.values('id', 'name')), safe=False)


