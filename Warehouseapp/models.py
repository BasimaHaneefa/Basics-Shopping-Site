from django.db import models

from Adminapp.models import tbl_warehouse
from Userapp.models import tbl_cart

# Create your models here.

class tbl_deliveryboy(models.Model):
    deliveryboy_name=models.CharField(max_length=50)
    deliveryboy_email=models.CharField(max_length=50)
    deliveryboy_contact=models.CharField(max_length=50)
    deliveryboy_photo=models.FileField(upload_to='DeliveryBoyDocs/')
    deliveryboy_password=models.CharField(max_length=50)
    deliveryboy_address=models.CharField(max_length=50)
    warehouse=models.ForeignKey(tbl_warehouse,on_delete=models.CASCADE,null=True)

class tbl_assigndelivery(models.Model):
    deliveryboy=models.ForeignKey(tbl_deliveryboy,on_delete=models.CASCADE)
    cart=models.ForeignKey(tbl_cart,on_delete=models.CASCADE)
    assign_status=models.CharField(max_length=10,default=0)
    assign_date=models.DateField(auto_now_add=True)
    