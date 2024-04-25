from django.db import models
from Adminapp.models import *
# Create your models here.
class tbl_userreg(models.Model):
    userregistration_name=models.CharField(max_length=50) 
    userregistration_contact=models.CharField(max_length=50) 
    userregistration_email=models.CharField(max_length=50)
    userregistration_address=models.CharField(max_length=50)
    userregistration_gender=models.CharField(max_length=50)
    userregistration_place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    userregistration_photo=models.FileField(upload_to='UserDoc/')
    userregistration_password=models.CharField(max_length=50)  
    userregistration_confirmpassword=models.CharField(max_length=50)
class tbl_ownerreg(models.Model):
    ownerregistration_name=models.CharField(max_length=50) 
    ownerregistration_about=models.CharField(max_length=50) 
    ownerregistration_contact=models.CharField(max_length=50)
    ownerrregistration_email=models.CharField(max_length=50)
    ownerregistration_address=models.CharField(max_length=50)
    owerregistration_district=models.CharField(max_length=50)
    ownerregistration_proof=models.FileField(upload_to='OwnerDoc/')
    ownerregistration_place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    ownerregistration_photo=models.FileField(upload_to='OwnerDoc/')
    ownerregistration_password=models.CharField(max_length=50)  
    ownerregistration_confirmpassword=models.CharField(max_length=50)   
    ownerregistration_status=models.CharField(max_length=50,default=0)   

      