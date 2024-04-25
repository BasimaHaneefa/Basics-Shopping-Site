from django.shortcuts import render,redirect
from Adminapp.models import tbl_district, tbl_warehouse
from Userapp.models import tbl_cart
from Warehouseapp.models import * 
# Create your views here.

def Home(request):
   return render(request,"Warehouseapp/HomePage.html")

def MyProfile(request): 
    myprofile=tbl_warehouse.objects.get(id=request.session["wid"] )
    return render(request,"Warehouseapp/MyProfile.html",{'data':myprofile})
def EditProfile(request): 
    dis=tbl_district.objects.all()
    myprofile=tbl_warehouse.objects.get(id=request.session["wid"] )
    if request.method=="POST":
        seldis=tbl_district.objects.get(id=request.POST.get("District"))
        myprofile.warehousereg_name=request.POST.get("txtname")
        myprofile.warehousereg_email=request.POST.get("txtemail")
        myprofile.warehousereg_address=request.POST.get("txtaddress")
        myprofile.warehousereg_district=seldis
        myprofile.save()
        return redirect("webwarehouse:myprofile")
    else:
        return render(request,"Warehouseapp/EditProfile.html",{'data':myprofile,'dis':dis})

def ChangePassword(request): 
    myprofile=tbl_warehouse.objects.get(id=request.session["wid"] )
    new=request.POST.get("txtpassword1")
    current=request.POST.get("currentpassword")
    confirm=request.POST.get("txtpassword2")
    old=myprofile.warehousereg_password
    if request.method=="POST":
        if old == current:
            if new == confirm:
                myprofile.warehousereg_password=new
                myprofile.save()
                msg="Password Changed"
                return render(request,"Warehouseapp/ChangePassword.html",{'msg':msg})   
            else:
                msg="Password mismatch"
                return render(request,"Warehouseapp/ChangePassword.html",{'msg':msg})   
        else:
            msg="Wrong Old Password"
            return render(request,"Warehouseapp/ChangePassword.html",{'msg':msg}) 
    else:
        return render(request,"Warehouseapp/ChangePassword.html")  


def DeliveryBoy(request):
    myprofile=tbl_warehouse.objects.get(id=request.session["wid"] )
    boydata=tbl_deliveryboy.objects.filter(warehouse=myprofile)
    if request.method=="POST":
       tbl_deliveryboy.objects.create(deliveryboy_name=request.POST.get("txtname"),
                                       deliveryboy_email=request.POST.get("txtemail"),
                                       deliveryboy_password=request.POST.get("txtpassword"),
                                       deliveryboy_address=request.POST.get("txtaddress"),
                                       deliveryboy_contact=request.POST.get("contact"),
                                       deliveryboy_photo=request.FILES.get("photo"),
                                       warehouse=myprofile
                                       )
       return redirect("webwarehouse:deliveryboy")
    else:
       return render(request,"Warehouseapp/DeliveryBoy.html",{'deliveryboy':boydata})

def DelDeliveryboy(request,did):
    tbl_deliveryboy.objects.get(id=did).delete()
    return redirect("webwarehouse:deliveryboy")

def Vieworder(request):
    myprofile=tbl_warehouse.objects.get(id=request.session["wid"] )
    dis=myprofile.warehousereg_district.id
    scart=tbl_cart.objects.filter(product__owner__ownerregistration_place__district=dis,booking__booking_status__gte=3)
    return render(request,"Warehouseapp/ViewOrder.html",{'data':scart})

def OrderStatus(request,pid):
    scart=tbl_cart.objects.get(id=pid)
    scart.cart_status=1
    scart.save()
    return redirect("webwarehouse:Vieworder")
    

def assigndelivery(request,did):
    myprofile=tbl_warehouse.objects.get(id=request.session["wid"] )
    boydata=tbl_deliveryboy.objects.filter(warehouse=myprofile)
    scart=tbl_cart.objects.get(id=did)
    if request.method=="POST":
        seldata=tbl_deliveryboy.objects.get(id=request.POST.get("staff"))
        tbl_assigndelivery.objects.create(deliveryboy=seldata,
                                          cart=scart,
                                          assign_status=1)
        scart.cart_status=2
        scart.save()
        return redirect("webwarehouse:Vieworder")
    else:
        return render(request,"Warehouseapp/AssignDelivery.html",{'data':boydata})
    
def logout(request):
    if 'wid' in request.session:
        del request.session['wid']
        return redirect('webguest:index')
    else:
        return redirect('webguest:index') 