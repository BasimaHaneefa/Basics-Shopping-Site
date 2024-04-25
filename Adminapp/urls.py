from django.urls import path,include
from Adminapp import views
app_name="webadmin"
urlpatterns = [
    path('Home/',views.Home,name="Home"),
    path('district/',views.District,name="district"),
    path('deldis/<int:did>',views.deldis,name="deldis"),
    path('editdis/<int:did>',views.editdis,name="editdis"),

    
    path('registration/',views.Registration,name="registration"),
    path('delreg/<int:rid>',views.delreg,name="delreg"),
    path('editreg/<int:rid>',views.editreg,name="editreg"),

    path('producttype/',views.ProductType,name="producttype"),
    path('delpro/<int:pid>',views.delpro,name="delpro"),
    path('editpro/<int:pid>',views.editpro,name="editpro"),

    path('ProductSubtype/',views.ProductSubtype,name="subtype"),
    path('delsubtype/<int:sid>',views.delsubtype,name="delsubtype"),
    
    path('Place/',views.Place,name="Place"),
    path('delPlace/<int:placeid>',views.delPlace,name="delPlace"),
    path('editPlace/<int:placeid>',views.editPlace,name="editPlace"),

    path('Warehouse/',views.warehouse,name="Warehouse"),
    path('delwhouse/<int:wid>',views.delwhouse,name="delwhouse"),

    path('OwnerVerify/',views.OwnerVerify,name="OwnerVerify"),
    path('Rejectowner/<int:aid>',views.Rejectowner,name="Rejectowner"),
    path('Acceptowner/<int:aid>',views.Acceptowner,name="Acceptowner"),
    path("ViewComplaint/",views. ViewComplaint,name="ViewComplaint"),
    path("Reply/<int:rid>",views. Reply,name="Reply"),
    path("ViewFeedback/",views. ViewFeedback,name="ViewFeedback"),

    path("logout/",views.logout,name="logout"),
]