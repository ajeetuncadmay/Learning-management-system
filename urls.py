from django.urls import path
from . import views

urlpatterns=[
    path('index/',views.index),
    path('',views.index),
    path('about/',views.aboutus),
    path('contact/',views.contact),
    path('batches/',views.mynewbatches),
    path('facility/',views.ourfacilaty),
    path('success/',views.successstories),
    path('signup/',views.registration),
    path('about/', views.aboutus),
    path('signin/',views.signin),
    path('feedback/',views.feedback),

]