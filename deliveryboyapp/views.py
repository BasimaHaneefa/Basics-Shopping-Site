from django.shortcuts import redirect, render
from Warehouseapp.models import tbl_deliveryboy,tbl_assigndelivery
from Userapp.models import tbl_cart
# Create your views here.

def Home(request):
    return render(request,"DeliveryBoyapp/Homepage.html")

def MyProfile(request): 
    myprofile=tbl_deliveryboy.objects.get(id=request.session["dbid"] )
    return render(request,"DeliveryBoyapp/MyProfile.html",{'data':myprofile})
def EditProfile(request): 
    myprofile=tbl_deliveryboy.objects.get(id=request.session["dbid"] )
    if request.method=="POST":
        myprofile.deliveryboy_name=request.POST.get("txtname")
        myprofile.deliveryboy_email=request.POST.get("txtemail")
        myprofile.deliveryboy_contact=request.POST.get("txtcontact")
        myprofile.deliveryboy_address=request.POST.get("txtaddress")
        myprofile.save()
        return redirect("webdeliveryboy:myprofile")
    else:
        return render(request,"DeliveryBoyapp/EditProfile.html",{'data':myprofile})

def ChangePassword(request): 
    myprofile=tbl_deliveryboy.objects.get(id=request.session["dbid"] )
    new=request.POST.get("txtpassword1")
    current=request.POST.get("currentpassword")
    confirm=request.POST.get("txtpassword2")
    old=myprofile.deliveryboy_password
    if request.method=="POST":
        if old == current:
            if new == confirm:
                myprofile.deliveryboy_password=new
                myprofile.save()
                msg="Password Changed"
                return render(request,"DeliveryBoyapp/ChangePassword.html",{'msg':msg})   
            else:
                msg="Password mismatch"
                return render(request,"DeliveryBoyapp/ChangePassword.html",{'msg':msg})   
        else:
            msg="Wrong Old Password"
            return render(request,"DeliveryBoyapp/ChangePassword.html",{'msg':msg}) 
    else:
        return render(request,"DeliveryBoyapp/ChangePassword.html")                             
     

def AssignedOrder(request):
    myprofile=tbl_deliveryboy.objects.get(id=request.session["dbid"] )
    data=tbl_assigndelivery.objects.filter(deliveryboy=myprofile)
    return render(request,"DeliveryBoyapp/ViewOrder.html",{'data':data})    

def OrderDelivery(request,did):
    data=tbl_assigndelivery.objects.get(id=did)
    cart=tbl_cart.objects.get(id=data.cart.id)
    cart.cart_status=3
    cart.save()
    return redirect("webdeliveryboy:AssignedOrder")

def logout(request):
    if 'dbid' in request.session:
        del request.session['dbid']
        return redirect('webguest:index')
    else:
        return redirect('webguest:index')       
