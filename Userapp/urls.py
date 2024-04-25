from django.urls import path
from Userapp import views
app_name="webuser"

urlpatterns = [
    path('myprofile/',views.MyProfile,name="myprofile"),
    path('editprofile/',views.EditProfile,name="editprofile"),
    path('changepassword/',views.ChangePassword,name="changepassword"),
    path("homepage/", views.homepage,name="homepage"),
    path("SearchSeller/", views.SearchSeller,name="SearchSeller"),
    path("AjaxSeller/", views.AjaxSeller,name="AjaxSeller"),
    path("ViewProduct/<int:oid>", views.ViewProduct,name="ViewProduct"),
    path("AjaxProduct/", views.AjaxProduct,name="AjaxProduct"),
    path('addcart/<int:pid>',views.Addcart,name='addcart'),
    path("Mycart/", views.Mycart,name="mycart"),
    path("DelCart/<int:did>", views.DelCart,name="delcart"),
    path("CartQty/", views.CartQty,name="cartqty"),
    path("Pay/", views.Pay,name="pay"),
    path("ViewMyPurchase/",views. ViewMyPurchase,name="ViewMyPurchase"),
    path("Complaint/",views.Complaint,name="Complaint"),
    path("Delcomplaint/<int:did>", views.Delcomplaint,name="Delcomplaint"),
    path("Feedback/",views.Feedback,name="Feedback"),
    path("Delfeedback/<int:did>", views.Delfeedback,name="Delfeedback"),

    path("logout/",views. logout,name="logout"),
    ]