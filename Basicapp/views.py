from django.shortcuts import render

# Create your views here.
def Sum(request):
    if request.method=="POST":
        num=int(request.POST.get("txtname"))
        num1=int(request.POST.get("txtname1"))
        sum=num+num1
        return render(request,"basicapp/Sum.html",{'result':sum})
    else:
        return render(request,"Basicapp/sum.html")

def calculator(request):
    res=0
    if request.method=="POST":
        num=int(request.POST.get("txtname"))
        num1=int(request.POST.get("txtname1"))
        btn=request.POST.get('btn')
        if btn=="+":
            res=num+num1
        elif btn=="-":   
            res=num-num1
        elif btn=="*": 
            res=num*num1
        elif btn=="/": 
            res=num/num1
        return render(request,"basicapp/calculator.html",{'result':res})
    else:
        return render(request,"Basicapp/calculator.html")
def marklist(request):
    res=0
    if request.method=="POST":
        Name=request.POST.get("txt_name")
        Contact=int(request.POST.get("txt_contact"))
        Email=request.POST.get("email")
        Department=request.POST.get("txt_dept")
        Mark1=int(request.POST.get("txt_mark1"))
        Mark2=int(request.POST.get("txt_mark2"))
        Mark3=int(request.POST.get("txt_mark3"))
        Total=Mark1+Mark2+Mark3
        Percentage=(Total/300)*100
        if Percentage   >= 90:
            Grade="A" 
        elif Percentage >= 80:
            Grade="B"
        elif Percentage >= 70:
            Grade="C"
        elif Percentage >= 60:
            Grade="D"
        elif Percentage>= 50:
            Grade="E"
        elif Percentage>= 40:
            Grade="F"

        return render(request,"Basicapp/Marklist.html",{'Name':Name,'Contact':Contact,'Email':Email,'Department':Department,'Total':Total,'Percent':Percentage,'Grade':Grade,})
        return render(request,"Basicapp/Marklist.html")
def Salary(request):
    if request.method=="POST":
           fristname=request.POST.get("txtfname")
           lastname=request.POST.get("txtlname")
           Name=request.POST.get("txtfname"+"txtlname")
           Gender=request.POST.get("gender")
           Martial=request.POST.get("Martial")
           if Gender=="Male":
              Name="Mr."+Name
           elif Gender=="Female" and Marital=="single":
                Name="Ms."+Name
           else:
                Name="Mrs."+Name
                Gender=int(request.POST.get("Gender"))
                Marital=request.POST.get("marital")
                Department=request.POST.get("txt_dept")
                Basicsalary=int(request.POST.get("basicsalary"))
           if Basicsalary >= 20000:
              TA=Basicsalary*0.4
              PA=Basicsalary*0.35
              HRA=Basicsalary*0.3
              LIC=Basicsalary*0.25
              PF=Basicsalary*0.2
           elif Basicsalary >= 15000:
              TA=Basicsalary*0.35
              PA=Basicsalary*0.3
              HRA=Basicsalary*0.25
              LIC=Basicsalary*0.2
              PF=Basicsalary*0.15
           elif Basicsalary < 15000:
              TA=Basicsalary*0.3
              PA=Basicsalary*0.25
              HRA=Basicsalary*0.2
              LIC=Basicsalary*0.15
              PF=Basicsalary*0.1
              NET=(Basicsalary+TA+DA+HRA)-LIC-PF
           return render(request,"Basicapp/Salary.html",{'Name':Name,'Gender':Gender,'Martial':Martial,'Dept':Dept,'TA':TA,'DA':DA,'HRA':HRA,'LIC':LIC,'PF':PF,'NET':NET,})
    else: 
           return render(request,"Basicapp/Salary.html")
           