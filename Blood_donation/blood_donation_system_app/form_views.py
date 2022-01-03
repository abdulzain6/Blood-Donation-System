from django.shortcuts import render
from django.http import HttpResponse , HttpRequest
from .models import *


success_msg = "Data Successfully Inserted."
# Create your views here.
def show_patients_form (request :HttpRequest):
    if request.method == 'GET':
        return render(request , "blood_donation_system_app/patientsForm.html")
    elif request.method == 'POST':
        try:
            patient = Patient()
            patient.Name = request.POST["name"]
            patient.CNIC = request.POST["cnic"]
            patient.Age = request.POST["age"]
            patient.Medical_Report = request.POST["medical_report"]
            patient.Gender = request.POST["gender"]
            patient.Blood_Group = request.POST["blood_group"]
            BB = Blood_Bank.objects.get(id = request.POST["blood_bank_id"])
            patient.Blood_Bank = BB
            doc = Doctor.objects.get(id = request.POST["examined_by_id"])
            patient.Examined_By = doc
            patient.save()
            return render(request , "blood_donation_system_app/patientsForm.html", context = {"alert_variable" : success_msg})
        except Blood_Bank.DoesNotExist:
            context = {"error_message": "Blood Bank does not exist."}
            return render(request, "blood_donation_system_app/error.html" , context=context)  
        except Doctor.DoesNotExist:
            context = {"error_message": "Doctor does not exist."}
            return render(request, "blood_donation_system_app/error.html" , context=context)          
        except:
            context = {"error_message": "OOPs There was a problem doing that."}
            return render(request, "blood_donation_system_app/error.html" , context=context)

def show_doctors_form (request:HttpRequest):
    if request.method == 'GET':
        return render(request , "blood_donation_system_app/doctorsForm.html")
    elif request.method == 'POST':
        try:
            doctor = Doctor()
            doctor.Name = request.POST["name"]
            doctor.Specialization = request.POST["Specialization"]
            doctor.Phone_Number = request.POST["Phone_Number"]
            doctor.Gender = request.POST["gender"]
            doctor.CNIC = request.POST["CNIC"]
            hospital = Hospital.objects.get(id = request.POST["hospital_id"])
            doctor.Hospital = hospital
            doctor.save()
            return render(request , "blood_donation_system_app/doctorsForm.html", context = {"alert_variable" : success_msg})
        except Hospital.DoesNotExist:
            context = {"error_message": "Hospital does not exist."}
            return render(request, "blood_donation_system_app/error.html" , context=context)            
        except:
            context = {"error_message": "OOPs There was a problem doing that."}
            return render(request, "blood_donation_system_app/error.html" , context=context)
        

def show_donors_form (request:HttpRequest):
    if request.method == 'GET':
        return render(request , "blood_donation_system_app/donorsForm.html")
    elif request.method == 'POST':
        try:
            donor = Donor()
            donor.Name = request.POST["name"]
            donor.CNIC = request.POST["cnic"]
            donor.Age = request.POST["age"]
            donor.Medical_Report = request.POST["medical_report"]
            donor.Gender = request.POST["gender"]
            donor.Blood_Group = request.POST["blood_group"]
            BB = Blood_Bank.objects.get(id = request.POST["blood_bank_id"])
            doc = Doctor.objects.get(id = request.POST["examined_by_id"])
            donor.Address = request.POST["address"]
            donor.Contact_Number = request.POST["contact_no"]
            donor.Blood_Bank = BB
            donor.Examined_By = doc
            donor.save()
            return render(request , "blood_donation_system_app/donorsForm.html", context = {"alert_variable" : success_msg})
        except Blood_Bank.DoesNotExist:
            context = {"error_message": "Blood Bank does not exist."}
            return render(request, "blood_donation_system_app/error.html" , context=context)  
        except Doctor.DoesNotExist:
            context = {"error_message": "Doctor does not exist."}
            return render(request, "blood_donation_system_app/error.html" , context=context)          
        except:
            context = {"error_message": "OOPs There was a problem doing that."}
            return render(request, "blood_donation_system_app/error.html" , context=context)


def show_security_guards_form (request:HttpRequest):
    if request.method == 'GET':
        return render(request , "blood_donation_system_app/securityGuardsForm.html")
    elif request.method == 'POST':
        try:
            guard = Security_Guard()
            guard.CNIC = request.POST["cnic"]
            guard.Name = request.POST["name"]
            guard.Gender = request.POST["gender"]
            guard.Experience = request.POST["experience"]
            guard.Hospital  = Hospital.objects.get(id = request.POST["hospital_id"])
            guard.save()
            return render(request , "blood_donation_system_app/securityGuardsForm.html", context = {"alert_variable" : success_msg})
        except Hospital.DoesNotExist:
            context = {"error_message": "Hospital does not exist."}
            return render(request, "blood_donation_system_app/error.html" , context=context)            
        except:
            context = {"error_message": "OOPs There was a problem doing that."}
            return render(request, "blood_donation_system_app/error.html" , context=context)


def show_parkings_form (request:HttpRequest):
    if request.method == 'GET':
        return render(request , "blood_donation_system_app/parkingAreasForm.html")
    elif request.method == 'POST':
        try:
            Parking = Parking_Area()
            Parking.Floors = request.POST["floors"]
            Parking.Space = request.POST["space"]
            Parking.Time_Allotment = request.POST["time_allotment"]
            hospital = Hospital.objects.get(id = request.POST["hospital_id"])
            Parking.Hospital = hospital
            Parking.save()
            return render(request , "blood_donation_system_app/parkingAreasForm.html", context = {"alert_variable" : success_msg})
        except Hospital.DoesNotExist:
            context = {"error_message": "Hospital does not exist."}
            return render(request, "blood_donation_system_app/error.html" , context=context)            
        except:
            context = {"error_message": "OOPs There was a problem doing that."}
            return render(request, "blood_donation_system_app/error.html" , context=context)


def show_pharmacys_form (request:HttpRequest):
    if request.method == 'GET':
        return render(request , "blood_donation_system_app/pharmacysForm.html")
    elif request.method == 'POST':
        try:
            pharmacy = Pharmacy()
            pharmacy.Name = request.POST["name"]
            pharmacy.Medicine = request.POST["medicine_amt"]
            pharmacy.Phone_Number = request.POST["phone_number"]
            pharmacy.Staff = request.POST["staff_no"]
            hospital = Hospital.objects.get(id = request.POST["hospital_id"])
            pharmacy.Hospital = hospital
            pharmacy.save()
            return render(request , "blood_donation_system_app/pharmacysForm.html", context = {"alert_variable" : success_msg})
        except Hospital.DoesNotExist:
            context = {"error_message": "Hospital does not exist."}
            return render(request, "blood_donation_system_app/error.html" , context=context)            
        except:
            context = {"error_message": "OOPs There was a problem doing that."}
            return render(request, "blood_donation_system_app/error.html" , context=context)

def show_hospitals_form (request:HttpRequest):
    if request.method == 'GET':
        return render(request , "blood_donation_system_app/hospitalsForm.html")
    elif request.method == 'POST':
        try:
            hospital = Hospital()
            hospital.Name = request.POST["name"]
            hospital.Floors = request.POST["floors"]
            hospital.Address = request.POST["address"]
            hospital.save()
            return render(request , "blood_donation_system_app/hospitalsForm.html", context = {"alert_variable" : success_msg})
        except:
            return render(request, "blood_donation_system_app/error.html")

def show_blood_banks_form (request:HttpRequest):
    if request.method == 'GET':
        return render(request , "blood_donation_system_app/bloodBanksForm.html")
    elif request.method == 'POST':
        try:
            BB = Blood_Bank()
            BB.Name = request.POST["name"]
            BB.Phone_Number = request.POST["phone_number"]
            BB.Address = request.POST["address"]
            hospital = Hospital.objects.get(id = request.POST["hospital_id"])
            BB.Hospital = hospital
            BB.save()
            return render(request , "blood_donation_system_app/bloodBanksForm.html", context = {"alert_variable" : success_msg})
        except Hospital.DoesNotExist:
            context = {"error_message": "Hospital does not exist."}
            return render(request, "blood_donation_system_app/error.html" , context=context)            
        except:
            context = {"error_message": "OOPs There was a problem doing that."}
            return render(request, "blood_donation_system_app/error.html" , context=context)

            