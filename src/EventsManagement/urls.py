from django.urls import path
from django.contrib import admin
from Delagates.views import *


urlpatterns = [

#login and register urls
   path('register/', registerPage, name='register'),
   path('login/', loginPage, name='login'),
   path('logout/', logoutUser, name='logout'),

# admin url
   path('admin/',admin.site.urls),
# home url
   path('',home, name='home'),
   
# delagates forms urls
   path('nonpaying/',nonpaying_form, name='NonPaying'),
   path('paying/',paying_form, name='Paying'),
   path('sponsorship/',sponsorship_form, name='Sponsorship'),
   path('exibitor/',exibitor_form, name='Exibitor'),
# delagates lists view urls
   path('display1/',nonpaying_view, name='Display1'),
   path('display2/',paying_view, name='Display2'),
   path('display3/',sponsorship_view, name='Display3'),
   path('display4/',exibitor_view, name='Display4'),

# delagate personal view and update
   path('delagate1/<str:pk>/',nonpaying_delagate, name='Delagate1'),
   path('delagate2/<str:pk>/',paying_delagate, name='Delagate2'),
   path('delagate3/<str:pk>/',sponsorship_delagate, name='Delagate3'),
   path('delagate4/<str:pk>/',exibitor_delagate, name='Delagate4'),

#updating delagates
   path('update1/<str:pk>/',updateNonpaying, name='update1'),
   path('update2/<str:pk>/',updatePaying, name='update2'),
   path('update3/<str:pk>/',updateSponsorship, name='update3'),
   path('update4/<str:pk>/',updateExibitor, name='update4'),
   
#delete delagate
   path('delete1/<str:pk>/',deleteNonpaying, name="delete1"),
   path('delete2/<str:pk>/',deletePaying, name="delete2"),
   path('delete3/<str:pk>/',deleteSponsorship, name="delete3"),
   path('delete4/<str:pk>/',deleteExibitor, name="delete4"),

#export
   path('export/',export, name="export"),
   path('export_1/',export_NP, name="export_1"),
   path('export_2/',export_P, name="export_2"),
   path('export_3/',export_S, name="export_3"),
   path('export_4/',export_E, name="export_4"),
   

]
