from django.db import models

# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)
class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)
class tbl_brand(models.Model):
    brand_name=models.CharField(max_length=50)
class tbl_registration(models.Model):
    registration_name=models.CharField(max_length=50) 
    registration_contact=models.CharField(max_length=50) 
    registration_email=models.CharField(max_length=50)
    registration_password=models.CharField(max_length=50)

class tbl_producttype(models.Model):
    producttype_name=models.CharField(max_length=50)

class tbl_subtype(models.Model):
    subtype_name=models.CharField(max_length=50)
    producttype=models.ForeignKey(tbl_producttype,on_delete=models.CASCADE) 

class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)
class tbl_warehouse(models.Model):
    warehousereg_name=models.CharField(max_length=50)   
    warehousereg_district=models.ForeignKey(tbl_district,on_delete=models.CASCADE,null=True) 
    warehousereg_address=models.CharField(max_length=50) 
    warehousereg_email=models.CharField(max_length=50) 
    warehousereg_password=models.CharField(max_length=50) 
    