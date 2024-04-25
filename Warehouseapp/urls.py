from django.urls import path,include
from Warehouseapp import views
app_name="webwarehouse"
urlpatterns = [
    path('Home/',views.Home,name="Home"),
    path('myprofile/',views.MyProfile,name="myprofile"),
    path('editprofile/',views.EditProfile,name="editprofile"),
    path('changepassword/',views.ChangePassword,name="changepassword"),
    path('deliveryboy/',views.DeliveryBoy,name="deliveryboy"),
    path('DelDeliveryboy/<int:did>',views.DelDeliveryboy,name="DelDeliveryboy"),
    path('Vieworder/',views.Vieworder,name="Vieworder"),
    path('OrderStatus/<int:pid>',views.OrderStatus,name="OrderStatus"),
    path('assigndelivery/<int:did>',views.assigndelivery,name="assigndelivery"),
 
 path("logout/",views. logout,name="logout"),
]