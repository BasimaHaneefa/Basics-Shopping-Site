from django.urls import path,include
from Businessowner import views
app_name="webBusinessowner"
urlpatterns = [
   path('product/',views.Product,name="product"),
   path('DelProduct/<int:did>',views.DelProduct,name="DelProduct"),
   path('gallery/<int:pid>',views.Gallery,name="gallery"),
   path('DelGallery/<int:did>',views.DelGallery,name="DelGallery"),
   path('ajaxsubtype/',views.ajaxsubtype,name="ajaxsubtype"),
   path('myprofile/',views.MyProfile,name="myprofile"),
   path('editprofile/',views.EditProfile,name="editprofile"),
   path('changepassword/',views.ChangePassword,name="changepassword"),
   path("homepage/", views.homepage,name="homepage"),
   path("ViewPurchase/",views.ViewPurchase,name="ViewPurchase"),
   path("BookingUpdates/<int:bid>",views.BookingUpdates,name="BookingUpdates"),

   path("logout/",views. logout,name="logout"),
    ]