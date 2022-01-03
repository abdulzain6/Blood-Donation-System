from django.db import models

# Create your models here.
class Hospital(models.Model):
    Name = models.CharField(max_length = 60)
    Floors = models.IntegerField(null=False)
    Address = models.CharField(null=False , max_length = 200)

class Blood_Bank(models.Model):
    Name = models.CharField(max_length = 50)
    Phone_Number = models.CharField(null=False ,max_length = 20) 
    Address = models.CharField(null=False , max_length = 200)
    Hospital = models.ForeignKey(Hospital , on_delete = models.CASCADE)


class Doctor(models.Model):
    Name = models.CharField(null=False , max_length = 50)
    Specialization = models.CharField(null=False , max_length = 20)
    Phone_Number = models.CharField(null=False ,max_length = 20)
    Gender = models.CharField(null=False , max_length = 10)
    Hospital = models.ForeignKey(Hospital , on_delete = models.CASCADE)
    CNIC = models.CharField(null=False ,max_length = 50)


class Patient (models.Model):
    CNIC = models.CharField(primary_key=True , null=False ,max_length = 50)
    Age = models.IntegerField(null=False)
    Gender = models.CharField(null=False , max_length = 10)
    Medical_Report = models.TextField(null=False)
    Name = models.CharField(null=False ,max_length =50)
    Blood_Group = models.CharField(null=False , max_length = 5)
    Examined_By = models.ForeignKey(Doctor , on_delete=models.DO_NOTHING )
    Blood_Bank = models.ForeignKey(Blood_Bank, on_delete=models.DO_NOTHING)

class Donor (models.Model):
    CNIC = models.CharField(primary_key=True , null=False , max_length = 50)
    Age = models.IntegerField(null=False)
    Gender = models.CharField(null=False , max_length =10)
    Name = models.CharField(null=False , max_length = 50)
    Address = models.CharField(null=False , max_length = 200)
    Contact_Number = models.CharField(null=False , max_length = 20)
    Medical_Report = models.TextField(null=False)
    Blood_Group = models.CharField(null=False , max_length = 5)
    Examined_By = models.ForeignKey(Doctor , on_delete=models.DO_NOTHING)
    Blood_Bank = models.ForeignKey(Blood_Bank, on_delete=models.DO_NOTHING)


class Security_Guard (models.Model):
    CNIC = models.CharField(null=False ,max_length = 50)
    Name = models.CharField(null=False , max_length = 50)
    Gender = models.CharField(null=False , max_length = 10)
    Experience = models.IntegerField(null=False)
    Hospital = models.ForeignKey(Hospital , on_delete = models.CASCADE)

class Parking_Area(models.Model):
    Floors = models.IntegerField(null=False)
    Space = models.IntegerField(null=False)
    Time_Allotment = models.IntegerField(null=False)
    Hospital = models.ForeignKey(Hospital , on_delete = models.CASCADE)

class Pharmacy (models.Model):
    Hospital = models.ForeignKey(Hospital , on_delete = models.CASCADE)
    Name = models.CharField(max_length = 50)
    Medicine = models.IntegerField(null=False)
    Phone_Number = models.CharField(null=False , max_length =20)
    Staff = models.IntegerField(null=False)












