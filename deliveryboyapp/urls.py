from django.urls import path
from deliveryboyapp import views
app_name="webdeliveryboy"
urlpatterns = [
    path('Home/',views.Home,name="Home"),
    path('myprofile/',views.MyProfile,name="myprofile"),
   path('editprofile/',views.EditProfile,name="editprofile"),
   path('changepassword/',views.ChangePassword,name="changepassword"),
   path('AssignedOrder/',views.AssignedOrder,name="AssignedOrder"),
    path('OrderDelivery/<int:did>',views.OrderDelivery,name="OrderDelivery"),
 
    path("logout/",views. logout,name="logout"),

]