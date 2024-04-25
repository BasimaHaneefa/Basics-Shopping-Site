from django.urls import path,include
from Guestapp import views
app_name="webguest"
urlpatterns = [
   path('userreg/',views.UserRegistration,name="userreg"),
   path('ownerreg/',views.BusinessOwnerreg,name="ownerreg"),
   path('login/',views.Login,name="login"),
   path('ajaxplace/',views.ajaxplace,name="AjaxPlace"),
   path('',views.index,name="index"),
    ]