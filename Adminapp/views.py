from django.shortcuts import render,redirect
from Adminapp.models import * # for import models from Adminapp
from Guestapp.models import *
from Userapp.models import tbl_complaint,tbl_feedback
# Create your views here.

def Home(request):
    bcount=tbl_ownerreg.objects.filter(ownerregistration_status=1).count()
    wcount=tbl_warehouse.objects.all().count()
    ucount=tbl_userreg.objects.all().count()
    return render(request,"Adminapp/HomePage.html",{'owner':bcount,'warehouse':wcount,'user':ucount})

def District(request):
    districtdata=tbl_district.objects.all()
    if request.method=="POST":
       tbl_district.objects.create(district_name=request.POST.get("txtdis"))
       return render(request,"Adminapp/District.html",{'dis':districtdata})
    else:
       return render(request,"Adminapp/District.html",{'dis':districtdata})
def deldis(request,did):
    tbl_district.objects.get(id=did).delete() 
    return redirect("webadmin:district") 
def editdis(request,did):
    disdata=tbl_district.objects.get(id=did)
    if request.method=="POST":
        disdata.district_name=request.POST.get('txtdis')
        disdata.save()
        return redirect("webadmin:district")
    else:
        return render(request,"Adminapp/District.html",{'edit':disdata})          

def Registration(request):
    regdata=tbl_registration.objects.all()
    if request.method=="POST":
       tbl_registration.objects.create(registration_name=request.POST.get("txtname"),
                                       registration_contact=request.POST.get("txtnumber"),
                                       registration_email=request.POST.get("txtemail"),
                                       registration_password=request.POST.get("txtpassword")
                                       )
       return render(request,"Adminapp/Registration.html",{'reg':regdata})
    else:
       return render(request,"Adminapp/Registration.html",{'reg':regdata}) 

def delreg(request,did):
    tbl_registration.objects.get(id=did).delete() 
    return redirect("webadmin:registration") 

def editreg(request,did):
    regdata=tbl_registration.objects.get(id=did)
    if request.method=="POST":
        regdata.registration_name=request.POST.get('txtreg')
        regdata.registration_contact=request.POST.get('txtnumder')
        regdata.registration_email=request.POST.get('txtemail')
        regdata.registration_password=request.POST.get('txtpassword')
        regdata.save()
        return redirect("webadmin:registration")
    else:
        return render(request,"Adminapp/Registration.html",{'edit':regdata})

def ProductType(request):
    producttypedata=tbl_producttype.objects.all()
    if request.method=="POST":
       tbl_producttype.objects.create(producttype_name=request.POST.get("txtpro"))
       return render(request,"Adminapp/ProductType.html",{'pro':producttypedata})
    else:
       return render(request,"Adminapp/ProductType.html",{'pro':producttypedata})

def delpro(request,pid):
    tbl_producttype.objects.get(id=pid).delete() 
    return redirect("webadmin:producttype")

def editpro(request,pid):
    prodata=tbl_producttype.objects.get(id=pid)
    if request.method=="POST":
        prodata.producttype_name=request.POST.get('txtpro')
        prodata.save()
        return redirect("webadmin:producttype")
    else:
        return render(request,"Adminapp/ProductType.html",{'edit':prodata})

def ProductSubtype(request):
    producttypedata=tbl_producttype.objects.all()
    subtypedata=tbl_subtype.objects.all()
    if request.method=="POST":
       selectedproduct=tbl_producttype.objects.get(id=request.POST.get("ProductType"))
       tbl_subtype.objects.create(subtype_name=request.POST.get("txtsubtype"),producttype=selectedproduct)
       return render(request,"Adminapp/ProductSubtype.html",{'pro':producttypedata,'sub':subtypedata})
    else:
       return render(request,"Adminapp/ProductSubtype.html",{'pro':producttypedata,'sub':subtypedata})
def delsubtype(request,sid):
    tbl_subtype.objects.get(id=sid).delete() 
    return redirect("webadmin:subtype")         

def Place(request):
    districtdata=tbl_district.objects.all()
    placedata=tbl_place.objects.all()
    if request.method=="POST":
        selecteddistrict=tbl_district.objects.get(id=request.POST.get("District"))
        tbl_place.objects.create(place_name=request.POST.get("txtplace"),district=selecteddistrict)
        return render(request,"Adminapp/Place.html",{'District':districtdata,'place':placedata})
    else:
        return render(request,"Adminapp/Place.html",{'District':districtdata,'place':placedata}) 

def delPlace(request,placeid):
    tbl_place.objects.get(id=placeid).delete()
    return redirect("webadmin:Place")

def editPlace(request,placeid):
    districtdata=tbl_district.objects.all()
    placedata=tbl_place.objects.get(id=placeid)
    if request.method=="POST":
        selecteddistrict=tbl_district.objects.get(id=request.POST.get("District"))
        placedata.place_name=request.POST.get('txtplace')
        placedata.district=selecteddistrict
        placedata.save()
        return redirect("webadmin:Place")
    else:
        return render(request,"Adminapp/Place.html",{'edit':placedata,'District':districtdata})
def warehouse(request):
    districtdata=tbl_district.objects.all() 
    warehousedata=tbl_warehouse.objects.all()
    if request.method=="POST": 
        district=tbl_district.objects.get(id=request.POST.get("District")) 
        tbl_warehouse.objects.create (warehousereg_name=request.POST.get("txtname"),
                                      warehousereg_district=district,
                                      warehousereg_address=request.POST.get("txtaddress"),
                                      warehousereg_email=request.POST.get("txtemail"),
                                      warehousereg_password=request.POST.get("txtpassword"),
                                     )  
        return render(request,"Adminapp/Warehouse.html",{'District':districtdata,'whouse':warehousedata})
    else:
        return render(request,"Adminapp/Warehouse.html",{'District':districtdata,'whouse':warehousedata})                                   

def delwhouse(request,wid):
    tbl_warehouse.objects.get(id=wid).delete()
    return redirect("webadmin:Warehouse")                                             

def OwnerVerify(request):
    new=tbl_ownerreg.objects.filter(ownerregistration_status=0)
    accepted=tbl_ownerreg.objects.filter(ownerregistration_status=1)
    rejected=tbl_ownerreg.objects.filter(ownerregistration_status=2)
    return render(request,"Adminapp/OwnerVerification.html",{'new':new,'accepted':accepted,'rejected':rejected})

def Acceptowner(request,aid):
    data=tbl_ownerreg.objects.get(id=aid)
    data.ownerregistration_status=1
    data.save()
    return redirect("webadmin:OwnerVerify") 

def Rejectowner(request,aid):
    data=tbl_ownerreg.objects.get(id=aid)
    data.ownerregistration_status=2
    data.save()
    return redirect("webadmin:OwnerVerify")
def ViewComplaint(request):
    newcom=tbl_complaint.objects.filter(complaint_status=0)
    recom=tbl_complaint.objects.filter(complaint_status=1)
    return render(request,"Adminapp/ViewComplaint.html",{'new':newcom,'repl':recom})  
def Reply(request,rid):
    com=tbl_complaint.objects.get(id=rid)
    if request.method=="POST":
        com.complaint_reply=request.POST.get("txtpro")
        com.complaint_status=1
        com.save()
        return redirect("webadmin:ViewComplaint")
    else:
        return render(request,"Adminapp/Reply.html")
def ViewFeedback(request):
    data=tbl_feedback.objects.all()
    return render(request,"Adminapp/ViewFeedback.html",{'data':data})     

def logout(request):
    if 'aid' in request.session:
        del request.session['aid']
        return redirect('webguest:index')
    else:
        return redirect('webguest:index')                   