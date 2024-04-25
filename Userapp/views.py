from django.shortcuts import render,redirect
from Guestapp.models import tbl_userreg,tbl_ownerreg
from Adminapp.models import *
from Businessowner.models import *
from Userapp.models import *
# Create your views here.

def homepage(request):
    return render(request,"Userapp/HomePage.html")

def MyProfile(request): 
    myprofile=tbl_userreg.objects.get(id=request.session["uid"] )
    return render(request,"Userapp/MyProfile.html",{'data':myprofile})
def EditProfile(request): 
    myprofile=tbl_userreg.objects.get(id=request.session["uid"] )
    if request.method=="POST":
        myprofile.userregistration_name=request.POST.get("txtname")
        myprofile.userrregistration_email=request.POST.get("txtemail")
        myprofile.userregistration_contact=request.POST.get("txtcontact")
        myprofile.userregistration_address=request.POST.get("txtaddress")
        myprofile.save()
        return redirect("webuser:myprofile")
    else:
        return render(request,"Userapp/EditProfile.html",{'data':myprofile})

def ChangePassword(request): 
    myprofile=tbl_userreg.objects.get(id=request.session["uid"] )
    new=request.POST.get("txtpassword1")
    current=request.POST.get("currentpassword")
    confirm=request.POST.get("txtpassword2")
    old=myprofile.userregistration_password
    if request.method=="POST":
        if old == current:
            if new == confirm:
                myprofile.userregistration_password=new
                myprofile.save()
                msg="Password Changed"
                return render(request,"Userapp/ChangePassword.html",{'msg':msg})   
            else:
                msg="Password mismatch"
                return render(request,"Userapp/ChangePassword.html",{'msg':msg})   
        else:
            msg="Wrong Old Password"
            return render(request,"Userapp/ChangePassword.html",{'msg':msg}) 
    else:
        return render(request,"Userapp/ChangePassword.html")  

def SearchSeller(request):
    district=tbl_district.objects.all()
    data=tbl_ownerreg.objects.all()
    return render(request,"Userapp/SearchSeller.html",{'dis':district,'data':data})

def AjaxSeller(request):
    if request.GET.get("dis") !="" and request.GET.get("plac") !="":
        # print(request.GET.get("dis"))
        disdata=tbl_district.objects.get(id=request.GET.get("dis"))
        placdata=tbl_place.objects.get(id=request.GET.get("plac"))
        data=tbl_ownerreg.objects.filter(ownerregistration_place__district=disdata,ownerregistration_place=placdata)
        return render(request,"Userapp/Ajaxseller.html",{'data':data})
    elif request.GET.get("dis") !="":
        disdata=tbl_district.objects.get(id=request.GET.get("dis"))
        data=tbl_ownerreg.objects.filter(ownerregistration_place__district=disdata)
        return render(request,"Userapp/Ajaxseller.html",{'data':data})
    elif request.GET.get("plac") !="":
        placdata=tbl_place.objects.get(id=request.GET.get("plac"))
        data=tbl_ownerreg.objects.filter(ownerregistration_place=placdata)
        return render(request,"Userapp/Ajaxseller.html",{'data':data})
    else:
        data=tbl_ownerreg.objects.all()
        return render(request,"Userapp/Ajaxseller.html",{'data':data})

def ViewProduct(request,oid):
    ownerdata=tbl_ownerreg.objects.get(id=oid)
    request.session["owner"]=ownerdata.id
    ptype=tbl_producttype.objects.all()
    data=tbl_product.objects.filter(owner=ownerdata)
    return render(request,"Userapp/ViewProduct.html",{'type':ptype,'data':data})

def AjaxProduct(request):
    if request.GET.get("did") !="" and request.GET.get("pid") !="":
        ptype=tbl_producttype.objects.get(id=request.GET.get("did")) 
        stype=tbl_subtype.objects.get(id=request.GET.get("pid"))
        data=tbl_product.objects.filter(subtype=stype,subtype__producttype=ptype,owner=request.session["owner"])
        return render(request,"Userapp/Ajaxproduct.html",{'data':data})
    elif request.GET.get("did") !="" :
        print(request.session["owner"])
        ptype=tbl_producttype.objects.get(id=request.GET.get("did")) 
        data=tbl_product.objects.filter(subtype__producttype=ptype,owner=request.session["owner"])
        return render(request,"Userapp/Ajaxproduct.html",{'data':data})
    elif request.GET.get("pid") !="":
        stype=tbl_subtype.objects.get(id=request.GET.get("pid"))
        data=tbl_product.objects.filter(subtype=stype,owner=request.session["owner"])
        return render(request,"Userapp/Ajaxproduct.html",{'data':data})
    else:
        data=tbl_product.objects.filter(owner=request.session["owner"])
        return render(request,"Userapp/Ajaxproduct.html",{'data':data})

def Addcart(request,pid):
    if 'uid' in request.session:
        productdata=tbl_product.objects.get(id=pid)
        custdata=tbl_userreg.objects.get(id=request.session["uid"])
        bookingcount=tbl_booking.objects.filter(user=custdata,booking_status=0).count()
        if bookingcount>0:
         bookingdata=tbl_booking.objects.get(user=custdata,booking_status=0)
         cartcount=tbl_cart.objects.filter(booking=bookingdata,product=productdata).count()
         if cartcount>0:
          msg="Already added"
          return render(request,"UserApp/SearchSeller.html",{'msg':msg})
         else:
        
          tbl_cart.objects.create(booking=bookingdata,product=productdata,cart_qty=1)
          msg="Added To cart"
          return render(request,"UserApp/SearchSeller.html",{'msg':msg})
        else:
           tbl_booking.objects.create(user=custdata)
           bookingcount=tbl_booking.objects.filter(booking_status=0,user=custdata).count()
           if bookingcount>0:
            bookingdata=tbl_booking.objects.get(user=custdata,booking_status=0)
            cartcount=tbl_cart.objects.filter(booking=bookingdata,product=productdata).count()
            if cartcount>0:
             msg="Already added"
             return render(request,"UserApp/SearchSeller.html",{'msg':msg})
            else:
             tbl_cart.objects.create(booking=bookingdata,product=productdata,cart_qty=1)
             msg="Added To cart"
            return render(request,"UserApp/SearchSeller.html",{'msg':msg})
    else:
          return redirect("webguest:login")
    
def Mycart(request):
   if request.method=="POST":
     bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
     bookingdata.booking_totalamount=request.POST.get("carttotalamt")
     bookingdata.booking_status=1
     bookingdata.save()
     return redirect("webuser:pay")
   else:
    customerdata=tbl_userreg.objects.get(id=request.session["uid"])
    bcount=tbl_booking.objects.filter(user=customerdata,booking_status=0).count()
   #cartcount=cart.objects.filter(booking__customer=customerdata,booking__status=0).count()
    if bcount>0:
    #cartdata=cart.objects.filter(booking__customer=customerdata,booking__status=0)
     book=tbl_booking.objects.get(user=customerdata,booking_status=0)
     bid=book.id
     request.session["bookingid"]=bid
     bkid=tbl_booking.objects.get(id=bid)
     cartdata=tbl_cart.objects.filter(booking=bkid)
     return render(request,"Userapp/MyCart.html",{'data':cartdata})
    else:
      return render(request,"Userapp/MyCart.html")
def DelCart(request,did):
   tbl_cart.objects.get(id=did).delete()
   return redirect("webuser:mycart")
def CartQty(request):
   qty=request.GET.get('QTY')
   cartid=request.GET.get('ALT')
   cartdata=tbl_cart.objects.get(id=cartid)
   cartdata.cart_qty=qty
   cartdata.save()
   return redirect("webuser:mycart")

def Pay(request):
   bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
   amnt=bookingdata.booking_totalamount
   if request.method=="POST":
      bookingdata.payment_status=1
      bookingdata.save()
      return redirect("webuser:ViewMyPurchase")
   else:
      return render(request,"Userapp/Payment.html",{'amnt':amnt})

def ViewMyPurchase(request):
    customerdata=tbl_userreg.objects.get(id=request.session["uid"])
    booking=tbl_booking.objects.filter(user=customerdata,booking_status__gte=0)
    cartdata = []
    for booking_obj in booking:
        carts_for_booking = tbl_cart.objects.filter(booking=booking_obj)
        cartdata.extend(carts_for_booking)
    return render(request,"Userapp/ViewMyPurchase.html",{'data':cartdata})    

def Complaint(request):
    customerdata=tbl_userreg.objects.get(id=request.session["uid"])
    Complaint=tbl_complaint.objects.filter(user=customerdata)
    if request.method=="POST":
       tbl_complaint.objects.create(user=customerdata,
                                    complaint_title=request.POST.get("txttit"),
                                    complaint_content=request.POST.get("txtcomplaint"))
       return redirect("webuser:Complaint")
    else:
        return render(request,"Userapp/Complaint.html",{'complaint':Complaint}) 

def Delcomplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect("webuser:Complaint")

def Feedback(request):
    customerdata=tbl_userreg.objects.get(id=request.session["uid"])
    feedback=tbl_feedback.objects.filter(user=customerdata)
    if request.method=="POST":
       tbl_feedback.objects.create(user=customerdata,
                                   feedback_content=request.POST.get("txtpro"))
       return redirect("webuser:Feedback")
    else:
        return render(request,"Userapp/Feedback.html",{'feedback':feedback})       

def Delfeedback(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return redirect("webuser:Feedback")   

def logout(request):
    if 'uid' in request.session:
        del request.session['uid']
        return redirect('webguest:index')
    else:
        return redirect('webguest:index')       