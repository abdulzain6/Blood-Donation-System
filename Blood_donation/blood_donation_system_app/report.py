from reportlab.platypus import SimpleDocTemplate ,Table , TableStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from .models import *


def generate_report_using_data(data , filename):
    pdf = SimpleDocTemplate(
        filename,
        pagesize=letter
    )

    table = Table(data)

    rowNumb = len(data)
    for i in range(1, rowNumb):
        bc = colors.burlywood if i % 2 == 0 else colors.beige
        ts = TableStyle(
            [('BACKGROUND', (0,i),(-1,i), bc)]
        )
        table.setStyle(ts)

    ts = TableStyle(
        [
        ('BOX',(0,0),(-1,-1),2,colors.black),

        ('LINEBEFORE',(2,1),(2,-1),2,colors.red),
        ('LINEABOVE',(0,2),(-1,2),2,colors.green),

        ('GRID',(0,1),(-1,-1),2,colors.black),
        ]
    )
    table.setStyle(ts)

    elems = [table]
    pdf.build(elems)


def make_report_guard(models_All):
    data = []
    headings = [f.name for f in Security_Guard._meta.get_fields()]
    data.append(headings)

    for item in models_All:
        row = [item.id , item.CNIC, item.Name, item.Gender, item.Experience, item.Hospital.id]
        data.append(row)
    fileName = 'blood_donation_system_app/reports/guards_report.pdf'

    generate_report_using_data(data , fileName)

def make_bb_report(models_All):
    data = []
    headings = ["Id" , "Name" , "Phone Number" ,"Address" , "Hospital Id"]
    data.append(headings)
    for item in models_All:
        row = [item.id , item.Name, item.Phone_Number, item.Address, item.Hospital.id]
        data.append(row)
    fileName = 'blood_donation_system_app/reports/blood_bank_report.pdf'

    generate_report_using_data(data , fileName)

def make_doc_report(models_All):
    data = []
    headings = ["Id" , "Name" , "Specialization" ,"Phone Number" , "Gender" , "Hospital Id" , "CNIC"]
    data.append(headings)
    for item in models_All:
        row = [item.id , item.Name, item.Specialization, item.Phone_Number,item.Gender, item.Hospital.id , item.CNIC]
        data.append(row)
    fileName = 'blood_donation_system_app/reports/doctor_report.pdf'

    generate_report_using_data(data , fileName)

def make_patient_report(models_All):
    data = []
    headings = ["CNIC" , "Age" , "Gender" ,"Name" , "Medical Report" , "Examined By" , "Blood bank id"]
    data.append(headings)
    for item in models_All:
        row = [item.CNIC , item.Age, item.Gender, item.Name,item.Medical_Report, item.Examined_By.Name , item.Blood_Bank.id]
        data.append(row)
    fileName = 'blood_donation_system_app/reports/patient_report.pdf'

    generate_report_using_data(data , fileName)

def make_donor_report(models_All):
    data = []
    headings = ["CNIC" , "Age" , "Gender" ,"Name" ,"Address","Contact Number", "Medical Report" , "Examined By" , "Blood bank id"]
    data.append(headings)
    for item in models_All:
        row = [item.CNIC , item.Age, item.Gender, item.Name,item.Address,item.Contact_Number, item.Medical_Report, item.Examined_By.Name , item.Blood_Bank.id]
        data.append(row)
    fileName = 'blood_donation_system_app/reports/donor_report.pdf'

    generate_report_using_data(data , fileName)




        
            

def make_hospital_report(models_All):
    data = []
    headings = ["ID"  , "Name" , "Floors" ,"Address"]
    data.append(headings)
    for item in models_All:
        row = [item.id , item.Name, item.Floors, item.Address]
        data.append(row)
    fileName = 'blood_donation_system_app/reports/hospital_report.pdf'

    generate_report_using_data(data , fileName)

def make_pharmacy_report(models_All):
    data = []
    headings = ["ID"  , "Hospital ID" , "Name" ,"Medicine" , "Phone Number" , "Staff"]
    data.append(headings)
    for item in models_All:
        row = [item.id , item.Hospital.id, item.Name, item.Medicine , item.Phone_Number , item.Staff]
        data.append(row)
    fileName = 'blood_donation_system_app/reports/pharmacy_report.pdf'

    generate_report_using_data(data , fileName)    
        
def make_parking_report(models_All):
    data = []
    headings = ["ID"  , "Floors" , "Space" ,"Time Allotment (mins)" , "Hospital ID"]
    data.append(headings)
    for item in models_All:
        row = [item.id , item.Floors, item.Space, item.Time_Allotment , item.Hospital.id]
        data.append(row)
    fileName = 'blood_donation_system_app/reports/parking_report.pdf'

    generate_report_using_data(data , fileName)