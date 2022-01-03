"""Blood_donation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .form_views import *
from .list_views import *
from .delete_views import *
from .report_views import *

def show_home (request:HttpRequest):
    return render(request,'blood_donation_system_app/home.html')


urlpatterns = [
    path("" , show_home),
    path("insert/patients/",show_patients_form),
    path("insert/doctors/",show_doctors_form),
    path("insert/donors/",show_donors_form),
    path("insert/guards/",show_security_guards_form),
    path("insert/parkings/" , show_parkings_form),
    path("insert/pharmacys/" , show_pharmacys_form),
    path("insert/hospitals/" , show_hospitals_form),
    path("insert/bloodbanks/" , show_blood_banks_form),
  


    path('delete/patients/', delete_patients , name="delete_patients"),
    path('delete/doctors/', delete_doctors , name="delete_doctors"),
    path('delete/donors/', delete_donors , name="delete_donors"),
    path('delete/guards/', delete_guards , name="delete_guards"),
    path('delete/parkings/', delete_parkings , name="delete_parkings"),
    path('delete/pharmacys/', delete_pharmacys , name="delete_pharmacys"),
    path('delete/hospitals/', delete_hospitals , name="delete_hospitals"),
    path('delete/bloodbanks/', delete_bloodbanks , name="delete_bloodbanks"),


    path("hospitals/",show_hospitals_list),
    path("patients/",show_patients_list),
    path("doctors/",show_doctors_list),
    path("bloodbanks/",show_bloodbanks_list),
    path("donors/",show_donors_list),
    path("parkings/",show_parkings_list),
    path("pharmacys/",show_pharmacys_list),
    path("guards/",show_guards_list),

    
    path("patients/<int:CNIC>/",show_patient),
    path("bloodbanks/<int:id>/",show_bloodbank),
    path("hospitals/<int:id>/",show_hospital),
    path("doctors/<int:id>/",show_doctor),
    path("donors/<int:CNIC>/",show_donor),
    path("parkings/<int:id>/",show_parking),
    path("pharmacys/<int:id>/",show_pharmacy),
    path("guards/<int:id>/",show_guard),


    path("report/guards/" , show_guard_report),
    path("report/bloodbanks/" , show_bloodbank_report),
    path("report/doctors/" , show_doctor_report),
    path("report/donors/" , show_donor_report),
    path("report/patients/" , show_patient_report),
    path("report/hospitals/" , show_hospital_report),
    path("report/pharmacys/" , show_pharmacy_report),
    path("report/parkings/" , show_parking_report),










    


]
