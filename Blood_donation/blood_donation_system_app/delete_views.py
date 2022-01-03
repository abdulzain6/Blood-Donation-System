from django.shortcuts import render
from django.http import HttpResponse , HttpRequest
from .models import *

def delete_patients (request :HttpRequest ):
    if request.method == "POST":
        try:
            CNIC = request.POST["delete"]
            Patient.objects.filter(CNIC=CNIC).delete()
        except:
            pass

        patients = Patient.objects.all()
        return render(request,'blood_donation_system_app/patients.html',{'patients': patients})


def delete_doctors (request :HttpRequest):
    if request.method == "POST":
        try:
            id = request.POST["delete"]
            Doctor.objects.filter(id=id).delete()
        except:
            context = {"error_message" : "Cannot delete Doctor, Foreign key error"}
            return render(request, "blood_donation_system_app/error.html" , context=context)
        doctors = Doctor.objects.all()
        return render(request,'blood_donation_system_app/doctors.html',{'doctors': doctors})

def delete_hospitals (request :HttpRequest):
    if request.method == "POST":
        try:
            id = request.POST["delete"]
            Hospital.objects.filter(id=id).delete()
        except :
            context = {"error_message" : "Cannot delete hospital, Foreign key error"}
            return render(request, "blood_donation_system_app/error.html" , context=context)

            
        hospitals = Hospital.objects.all()
        return render(request,'blood_donation_system_app/hospitals.html',{'hospitals': hospitals})

def delete_bloodbanks (request :HttpRequest):
    if request.method == "POST":
        try:
            id = request.POST["delete"]
            Blood_Bank.objects.filter(id=id).delete()
        except:
            context = {"error_message" : "Cannot delete Blood Bank, Foreign key error"}
            return render(request, "blood_donation_system_app/error.html" , context=context)
        bloodbanks = Blood_Bank.objects.all()
        return render(request,'blood_donation_system_app/bloodbanks.html',{'bloodbanks': bloodbanks})

def delete_donors (request :HttpRequest):
    if request.method == "POST":
        try:
            CNIC = request.POST["delete"]
            Donor.objects.filter(CNIC=CNIC).delete()
        except:
            pass
        donors = Donor.objects.all()
        return render(request,'blood_donation_system_app/donors.html',{'donors': donors})

def delete_parkings (request :HttpRequest):
    if request.method == "POST":
        
        id = request.POST["delete"]
        
        print(id)
        Parking_Area.objects.filter(id=id).delete()

        parkings = Parking_Area.objects.all()
        return render(request,'blood_donation_system_app/parkingArea.html',{'parkings': parkings})

def delete_pharmacys (request :HttpRequest):
    if request.method == "POST":

        try:
            id = request.POST["delete"]
            Pharmacy.objects.filter(id=id).delete()
        except:
            pass
        pharmacies = Pharmacy.objects.all()
        return render(request,'blood_donation_system_app/pharmacys.html',{'pharmacies': pharmacies})

def delete_guards (request :HttpRequest):
    if request.method == "POST":
        try:
            id = request.POST["delete"]
            Security_Guard.objects.filter(id=id).delete()
        except:
            pass
        guards = Security_Guard.objects.all()
        return render(request,'blood_donation_system_app/securityGuards.html',{'guards': guards})