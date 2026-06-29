from django.urls import path
from . import views
from . import apps

urlpatterns = [
    path('',views.index, name="index" ),
    path('about/',views.about, name="about" ),
    path('404/',views.care, name="care" ),
    path('appointment/',views.appointment, name="appointment" ),
    path('contact/',views.contact, name="contact" ),
    path('department-details',views.departmentDetails, name="departmentDetails" ),
    path('departments/',views.departments, name="departments" ),
    path('doctors/',views.doctors, name="doctors" ),
    path('faq/',views.faq, name="faq" ),
    path('gallery/',views.gallery, name="gallery"),
    path('health/',views.health, name="health" ),
    path('privacy/',views.privacy, name="privacy" ),
    path('serviceDetails/',views.serviceDetails, name="serviceDetails" ),
    path('services/',views.services, name="services" ),
    path('starter-page/',views.starterPage, name="starterPage" ),
    path('terms/',views.terms, name="terms" ), 
    path('testimonials',views.testimonials, name="testimonials" ), 
]
