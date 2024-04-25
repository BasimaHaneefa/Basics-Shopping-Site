from django.urls import path,include
from Basicapp import views
urlpatterns = [
    path('addition/',views.Sum),

    path('calc/',views.calculator),
    path('marklist/',views.marklist),
    path('Salary/',views.Salary),
]