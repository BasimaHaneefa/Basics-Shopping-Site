from django.shortcuts import render,redirect
from Businessowner.models import * 
from Adminapp.models import *
from Guestapp.models import tbl_ownerreg
from Userapp.models import tbl_booking, tbl_cart
# Create your views here.
def Product(request):
    myprofile=tbl_ownerreg.objects.get(id=request.session["oid"] )
    producttypedata=tbl_producttype.objects.all()
    productdata=tbl_product.objects.filter(owner=myprofile)

    if request.method=="POST":
        data=tbl_subtype.objects.get(id=request.POST.get("ProductSubtype"))
       
        tbl_product.objects.create(product_name=request.POST.get("txtname"),
                                  product_price=request.POST.get("txtprice"),
                                  product_details=request.POST.get("txtdetails"),
                                  subtype=data,
                                  owner=myprofile,
                                  product_image=request.FILES.get("pimage")
                                       )
        return redirect("webBusinessowner:product")
    else:
        return render(request,"Businessowner/Product.html",{'ProductType':producttypedata,'product':productdata})

def DelProduct(request,did):
    tbl_product.objects.get(id=did).delete()
    return redirect("webBusinessowner:product")

def Gallery(request,pid): 
    data=tbl_product.objects.get(id=pid)
    gallerydata=tbl_gallery.objects.filter(product=data)
    if request.method=="POST":
        tbl_gallery.objects.create(gallery_photos=request.FILES.get("Photo"),
                                    product=data) 
        return redirect("webBusinessowner:gallery",pid=pid)
    else:
        return render(request,"Businessowner/Gallery.html",{'gallery':gallerydata}) 

def DelGallery(request,did):
    tbl_gallery.objects.get(id=did).delete()
    return redirect("webBusinessowner:product")


def MyProfile(request): 
    myprofile=tbl_ownerreg.objects.get(id=request.session["oid"] )
    return render(request,"Businessowner/MyProfile.html",{'data':myprofile})
def EditProfile(request): 
    myprofile=tbl_ownerreg.objects.get(id=request.session["oid"] )
    if request.method=="POST":
        myprofile.ownerregistration_name=request.POST.get("txtname")
        myprofile.ownerrregistration_email=request.POST.get("txtemail")
        myprofile.ownerregistration_contact=request.POST.get("txtcontact")
        myprofile.ownerregistration_address=request.POST.get("txtaddress")
        myprofile.save()
        return redirect("webBusinessowner:myprofile")
    else:
        return render(request,"Businessowner/EditProfile.html",{'data':myprofile})

def ChangePassword(request): 
    myprofile=tbl_ownerreg.objects.get(id=request.session["oid"] )
    new=request.POST.get("txtpassword1")
    current=request.POST.get("currentpassword")
    confirm=request.POST.get("txtpassword2")
    old=myprofile.ownerregistration_password
    if request.method=="POST":
        if old == current:
            if new == confirm:
                myprofile.ownerregistration_password=new
                myprofile.save()
                msg="Password Changed"
                return render(request,"Businessowner/ChangePassword.html",{'msg':msg})   
            else:
                msg="Password mismatch"
                return render(request,"Businessowner/ChangePassword.html",{'msg':msg})   
        else:
            msg="Wrong Old Password"
            return render(request,"Businessowner/ChangePassword.html",{'msg':msg}) 
    else:
        return render(request,"Businessowner/ChangePassword.html")                             
     
def ajaxsubtype(request):
    producttypedata=tbl_producttype.objects.get(id=request.GET.get("proid")) 
    subtypedata=tbl_subtype.objects.filter(producttype=producttypedata)  
    return render(request,"Businessowner/Ajaxsubtype.html",{"data":subtypedata}) 
def homepage(request):
    return render(request,"Businessowner/HomePage.html")  
def ViewPurchase(request):
    myprofile=tbl_ownerreg.objects.get(id=request.session["oid"] )
    # booking=tbl_booking.objects.filter(user=myprofile,booking_status__gte=0)
    cartdata=tbl_cart.objects.filter(product__owner=myprofile,booking__booking_status__gte=0)
    return render(request,"Businessowner/ViewPurchase.html",{'data':cartdata})  

def BookingUpdates(request,bid):
    cart=tbl_cart.objects.get(id=bid)
    booking=tbl_booking.objects.get(id=cart.booking.id)
    if booking.booking_status == '1':
        booking.booking_status=3
        booking.save()
        return redirect("webBusinessowner:ViewPurchase")
    elif booking.booking_status == '3':
        booking.booking_status=2
        booking.save()
        return redirect("webBusinessowner:ViewPurchase")
    else:
        return render(request,"Businessowner/ViewPurchase.html")
    

def logout(request):
    if 'oid' in request.session:
        del request.session['oid']
        return redirect('webguest:index')
    else:
        return redirect('webguest:index')       
