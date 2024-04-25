from django.db import models
from Adminapp.models import tbl_subtype
from Guestapp.models import tbl_ownerreg
from Businessowner.models import *
# Create your models here.


class tbl_product(models.Model):
    product_name=models.CharField(max_length=50)  
    product_price=models.CharField(max_length=50) 
    product_details=models.CharField(max_length=50) 
    product_image=models.FileField(upload_to='ProductDoc/')
    subtype=models.ForeignKey(tbl_subtype,on_delete=models.CASCADE)
    owner=models.ForeignKey(tbl_ownerreg,on_delete=models.CASCADE)

class tbl_gallery(models.Model):
    gallery_photos=models.FileField(upload_to='GallaryDoc/')
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)
     
