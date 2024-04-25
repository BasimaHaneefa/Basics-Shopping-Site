from django.shortcuts import render,redirect
from Guestapp.models import * 
from Adminapp.models import *
from Warehouseapp.models import tbl_deliveryboy
# for import models from Guestapp

# Create your views here.
def UserRegistration(request):
    districtdata=tbl_district.objects.all()
    placedata=tbl_place.objects.all()
    userregdata=tbl_userreg.objects.all()
    if request.method=="POST":
      selectedplace=tbl_place.objects.get(id=request.POST.get("place"))
      tbl_userreg.objects.create(userregistration_name=request.POST.get('txtname'),
                                       userregistration_contact=request.POST.get('txtnumber'),
                                       userregistration_email=request.POST.get('txtemail'),
                                       userregistration_address=request.POST.get('txtaddress'),
                                       userregistration_place=selectedplace,
                                       userregistration_photo=request.FILES.get('Photo'),
                                       userregistration_password=request.POST.get('txtpassword1'),
                                       userregistration_confirmpassword=request.POST.get('txtpassword2')
                                       )
      return render(request,"Guestapp/UserRegistration.html",{'place':placedata,'userreg':userregdata,'District':districtdata})
    else:
      return render(request,"Guestapp/UserRegistration.html",{'place':placedata,'userreg':userregdata,'District':districtdata})

def BusinessOwnerreg(request):
    districtdata=tbl_district.objects.all()
    placedata=tbl_place.objects.all()
    ownerregdata=tbl_ownerreg.objects.all()
    if request.method=="POST":
       selectedplace=tbl_place.objects.get(id=request.POST.get("place"))
       tbl_ownerreg.objects.create(ownerregistration_name=request.POST.get("txtname"),
                                       ownerregistration_about=request.POST.get("txtabout"),
                                       ownerregistration_contact=request.POST.get("txtnumber"),
                                       ownerrregistration_email=request.POST.get("txtemail"),
                                       ownerregistration_address=request.POST.get("txtaddress"),
                                       owerregistration_district=request.POST.get("District"),
                                       ownerregistration_proof=request.FILES.get("Proof"),
                                       ownerregistration_place=selectedplace,
                                       ownerregistration_photo=request.FILES.get("Photo"),
                                       ownerregistration_password=request.POST.get("txtpassword1"),
                                       ownerregistration_confirmpassword=request.POST.get("txtpassword2")
                                       )
       return render(request,"Guestapp/BusinessOwnerreg.html",{'place':placedata,'ownerreg':ownerregdata,'District':districtdata})
    else:
       return render(request,"Guestapp/BusinessOwnerreg.html",{'place':placedata,'ownerreg':ownerregdata,'District':districtdata})  

def Login(request):
    if request.method=="POST":
       login_email=request.POST.get("txtemail")
       login_password=request.POST.get("txtpassword")

       usercount = tbl_userreg.objects.filter(userregistration_email=login_email,userregistration_password=login_password).count() 
       businessownercount = tbl_ownerreg.objects.filter(ownerrregistration_email=login_email,ownerregistration_password=login_password,ownerregistration_status=1).count()
       admincount = tbl_registration.objects.filter(registration_email=login_email,registration_password=login_password).count()
       warecount=tbl_warehouse.objects.filter(warehousereg_email=login_email,warehousereg_password=login_password).count()
       dboycount=tbl_deliveryboy.objects.filter(deliveryboy_email=login_email,deliveryboy_password=login_password).count()
       if usercount > 0:
          user = tbl_userreg.objects.get(userregistration_email=login_email,userregistration_password=login_password)
          request.session["uid"] = user.id
          return redirect("webuser:homepage")  
       elif  businessownercount > 0:
          businessowner = tbl_ownerreg.objects.get(ownerrregistration_email=login_email,ownerregistration_password=login_password,ownerregistration_status=1)
          request.session["oid"] = businessowner.id
          return redirect("webBusinessowner:homepage")
       elif admincount > 0:
          admin = tbl_registration.objects.get(registration_email=login_email,registration_password=login_password) 
          request.session["aid"] = admin.id
          return redirect("webadmin:Home") 
       elif warecount>0:
          ware=tbl_warehouse.objects.get(warehousereg_email=login_email,warehousereg_password=login_password)
          request.session["wid"]=ware.id
          return redirect("webwarehouse:Home") 
       elif dboycount>0:
          dboy=tbl_deliveryboy.objects.get(deliveryboy_email=login_email,deliveryboy_password=login_password)
          request.session["dbid"]=dboy.id
          return redirect("webdeliveryboy:Home") 
       else:                                           
         return render(request,"Guestapp/Login.html",{"msg":"error"})
    else:
        return render(request,"Guestapp/Login.html") 
       
def ajaxplace(request):
    districtdata=tbl_district.objects.get(id=request.GET.get("disid")) 
    placedata=tbl_place.objects.filter(district=districtdata)  
    return render(request,"Guestapp/Ajaxplace.html",{"data":placedata})        
def index(request):
   if request.method=="POST":
      return render(request,"Guestapp/index.html")
   else:
      return render(request,"Guestapp/index.html")   
