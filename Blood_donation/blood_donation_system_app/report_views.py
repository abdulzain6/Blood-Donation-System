from django.shortcuts import render
from django.http import HttpResponse , HttpRequest , FileResponse
from reportlab.pdfgen import canvas
from .report import * 

def show_guard_report(request : HttpRequest):
    guards = Security_Guard.objects.all()
    make_report_guard(guards)
    pdf = open('blood_donation_system_app/reports/guards_report.pdf', 'rb')
    return FileResponse(pdf , as_attachment=True)

def show_bloodbank_report(request : HttpRequest):
    bb = Blood_Bank.objects.all()
    make_bb_report(bb)
    pdf = open('blood_donation_system_app/reports/blood_bank_report.pdf', 'rb')
    return FileResponse(pdf , as_attachment=True)

def show_doctor_report(request : HttpRequest):
    doc = Doctor.objects.all()
    make_doc_report(doc)
    pdf = open('blood_donation_system_app/reports/doctor_report.pdf', 'rb')
    return FileResponse(pdf , as_attachment=True)

def show_patient_report(request : HttpRequest):
    patient = Patient.objects.all()
    make_patient_report(patient)
    pdf = open('blood_donation_system_app/reports/patient_report.pdf', 'rb')
    return FileResponse(pdf , as_attachment=True)

def show_donor_report(request : HttpRequest):
    donor = Donor.objects.all()
    make_donor_report(donor)
    pdf = open('blood_donation_system_app/reports/donor_report.pdf', 'rb')
    return FileResponse(pdf , as_attachment=True)

def show_parking_report(request : HttpRequest):
    pa = Parking_Area.objects.all()
    make_parking_report(pa)
    pdf = open('blood_donation_system_app/reports/parking_report.pdf', 'rb')
    return FileResponse(pdf , as_attachment=True)

def show_pharmacy_report(request : HttpRequest):
    p = Pharmacy.objects.all()
    make_pharmacy_report(p)
    pdf = open('blood_donation_system_app/reports/pharmacy_report.pdf', 'rb')
    return FileResponse(pdf , as_attachment=True)

def show_hospital_report(request : HttpRequest):
    hos = Hospital.objects.all()
    make_hospital_report(hos)
    pdf = open('blood_donation_system_app/reports/hospital_report.pdf', 'rb')
    return FileResponse(pdf , as_attachment=True)