from django.shortcuts import render
from django.http import HttpResponse , HttpRequest
from .models import *

def show_patients_list (request :HttpRequest):
    patients = Patient.objects.all()
    return render(request,'blood_donation_system_app/patients.html',{'patients': patients})

def show_doctors_list (request :HttpRequest):
    doctors = Doctor.objects.all()
    return render(request,'blood_donation_system_app/doctors.html',{'doctors': doctors})

def show_hospitals_list (request :HttpRequest):
    hospitals = Hospital.objects.all()
    return render(request,'blood_donation_system_app/hospitals.html',{'hospitals': hospitals})

def show_bloodbanks_list (request :HttpRequest):
    bloodbanks = Blood_Bank.objects.all()
    return render(request,'blood_donation_system_app/bloodbanks.html',{'bloodbanks': bloodbanks})

def show_donors_list (request :HttpRequest):
    donors = Donor.objects.all()
    return render(request,'blood_donation_system_app/donors.html',{'donors': donors})

def show_parkings_list (request :HttpRequest):
    parkings = Parking_Area.objects.all()
    return render(request,'blood_donation_system_app/parkingArea.html',{'parkings': parkings})

def show_pharmacys_list (request :HttpRequest):
    pharmacies = Pharmacy.objects.all()
    return render(request,'blood_donation_system_app/pharmacys.html',{'pharmacies': pharmacies})

def show_guards_list (request :HttpRequest):
    guards = Security_Guard.objects.all()
    return render(request,'blood_donation_system_app/securityGuards.html',{'guards': guards})

def show_patient(request :HttpRequest , CNIC :int):
    patient = Patient.objects.get(CNIC=CNIC)
    return render(request,'blood_donation_system_app/patientsdetail.html',{'patient':patient})

def show_bloodbank(request :HttpRequest , id :int):
    bb = Blood_Bank.objects.get(id=id)
    return render(request,'blood_donation_system_app/bloodbanksdetail.html',{'bloodbank':bb})

def show_doctor(request :HttpRequest , id :int):
    doc = Doctor.objects.get(id=id)
    return render(request,'blood_donation_system_app/doctorsdetail.html',{'doctor':doc})

def show_donor(request :HttpRequest , CNIC ):
    donor = Donor.objects.get(CNIC=CNIC)
    return render(request,'blood_donation_system_app/donorsdetail.html',{'donor':donor})

def show_hospital(request :HttpRequest , id :int):
    hos = Hospital.objects.get(id=id)
    return render(request,'blood_donation_system_app/hospitalsdetail.html',{'hospital':hos})

def show_parking(request :HttpRequest , id :int):
    parking = Parking_Area.objects.get(id=id)
    return render(request,'blood_donation_system_app/parkingAreasdetail.html',{'parking':parking})

def show_pharmacy(request :HttpRequest , id :int):
    pharmacy = Pharmacy.objects.get(id=id)
    return render(request,'blood_donation_system_app/pharmacysdetail.html',{'pharmacy':pharmacy})

def show_guard(request :HttpRequest , id :int):
    guard = Security_Guard.objects.get(id=id)
    return render(request,'blood_donation_system_app/securityGuardsdetail.html',{'guard':guard})