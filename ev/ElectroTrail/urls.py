from django.urls import path
from . import views


urlpatterns = [
   
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('', views.landing, name='landing'),
    path('charge/', views.charge, name='charge'),
    path('create/', views.create_review, name='create_review'),
    path('update/<int:review_id>/', views.update_review, name='update_review'),
    path('delete/<int:review_id>/', views.delete, name='delete'),
    path('vehicle/delete/<int:vehicle_id>/', views.delete_vehicle, name='vehicle_delete'),
    path('reviews/', views.review_list, name='reviews'),
    path('register/', views.register, name='register'),
    
   

]  
