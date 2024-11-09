from django.shortcuts import render,redirect
from .models import Evreview,Vehicle
from .forms import EvReviewForm,userRegistrationform,VehicleForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login 
from django.contrib import messages
from .forms import VehicleForm 
# Create your views here.



def about(request):
    return render(request,'about.html')
def landing(request):
    return render(request,'landing.html')

def charge(request):
    vehicles = Vehicle.objects.all()  # Retrieve all vehicle instances
    if request.method == 'POST':
            form = VehicleForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('charge')  # Redirect to the charge page after saving
    else:
            form = VehicleForm()  # Ensure this initializes the form correctly
    
    return render(request, 'charge.html', {'vehicles': vehicles, 'form': form})
    

def index(request):
    vehicles = Vehicle.objects.all()  # Retrieve all vehicle instances
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the index page after saving
    else:
        form = VehicleForm()  # Ensure this initializes the form correctly
    
    return render(request, 'index.html', {'vehicles': vehicles, 'form': form})

def review_list(request):
    reviews = Evreview.objects.all().order_by('-created_at') 
    return render(request, 'reviews.html',{'reviews':reviews})

@login_required
def create_review(request):
    if request.method == 'POST':
        form = EvReviewForm(request.POST,request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  # Assuming User is the model name and it has a foreign key to User model.
            review.save()
            return redirect('reviews')
    else:
        form = EvReviewForm()
    return render(request,'create_reviews.html',{'form':form})

@login_required
def update_review(request,review_id):
    review =get_object_or_404(Evreview,pk =review_id, user=request.user)

    if request.method == 'POST':
         form = EvReviewForm(request.POST,request.FILES ,instance = review )
         if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  # Assuming User is the model name and it has a foreign key to User model.
            review.save()
            return redirect('reviews')
        
    else:
        form=EvReviewForm(instance=review)
    
    return render(request,'create_reviews.html',{'form':form})

@login_required
def delete(request,review_id):
    review = get_object_or_404(Evreview, pk=review_id, user=request.user)
    if request.method == 'POST':
        review.delete()
        return redirect('reviews')
    else:
        return render(request,'delete.html',{'review':review})
    
@login_required
def delete_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)  # Remove the user filtering
    if request.method == 'POST':
        vehicle.delete()
        return redirect('index') 


def register(request):
    if request.method == 'POST':
        form = userRegistrationform(request.POST)  # Correct class name casing
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])  # Set password securely
            user.save()
            login(request, user)  # Log the user in
            messages.success(request, 'Registration successful!')  # Success message
            return redirect('reviews')  # Redirect after successful registration
        else:
            messages.error(request, 'Please correct the errors below.')  # Error message

    else:
        form = userRegistrationform()  # Initialize the form if GET request

    return render(request, 'registration/register.html', {'form': form})
