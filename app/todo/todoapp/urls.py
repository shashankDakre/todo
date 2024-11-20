from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('view/', views.view, name='create'),
    path('edit/<int:id>/',views.edit,name="edit"),
    path('update/<int:id>/',views.update,name="update"),
]


#    path('edit/<int:id>/',views.edit,name="edit"),
#     path('update/<int:id>/',views.update,name="update"),
#     path('delete/<int:id>/',views.delete,name="delete"),