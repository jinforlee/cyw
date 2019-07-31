from django.urls import path
from . import views

app_name="world"
urlpatterns=[
    path('visitor/', views.visitor, name="visitor"),
    path('gallery/', views.gallery, name="gallery"),
    path('create/', views.create, name="create"),
    path('new/', views.new, name="new"), #여기 추가함
    path('<int:id>/', views.show, name="show"), #여기 추가함
    path('<int:id>/new_comment/', views.new_comment, name="new_comment"),
    path('<int:id>/create_comment/', views.create_comment, name="create_comment"),
    path('<int:id>', views.delete, name="delete"),
    path('<int:id>', views.delete_comment, name="delete_comment"),
    path('favourite/', views.favourite, name="favourite"),
    path('<int:id>/like/', views.like, name="like"),
]