from django.db import models
from Guestapp.models import tbl_userreg
from Businessowner.models import tbl_product
# Create your models here.
class tbl_booking(models.Model):
    user=models.ForeignKey(tbl_userreg,on_delete=models.CASCADE)
    booking_date=models.DateField(auto_now_add=True)
    booking_status=models.CharField(default=0,max_length=10)
    payment_status=models.CharField(default=0,max_length=10)
    booking_totalamount=models.CharField(default=0,max_length=100)

class tbl_cart(models.Model):
    booking=models.ForeignKey(tbl_booking,on_delete=models.CASCADE)
    cart_status=models.CharField(max_length=5,default='0')
    cart_qty=models.CharField(max_length=100)
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)

class tbl_complaint(models.Model):
    user=models.ForeignKey(tbl_userreg,on_delete=models.CASCADE)
    complaint_status=models.CharField(default=0,max_length=10)
    complaint_title=models.CharField(max_length=100)
    complaint_content=models.CharField(max_length=300)
    complaint_reply=models.CharField(default='Not replied',max_length=100)
    complaint_date=models.DateField(auto_now_add=True)

class tbl_feedback(models.Model):
    user=models.ForeignKey(tbl_userreg,on_delete=models.CASCADE)
    feedback_content=models.CharField(max_length=300)
    feedback_date=models.DateField(auto_now_add=True)


    