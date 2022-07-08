
from django.urls import path
from . import views

urlpatterns = [
    path('',views.getNotes),
    path('create/',views.createNote),
    path('<str:id>/',views.getNote),
    path('update/<str:id>/',views.updateNote),
    path('delete/<str:id>/',views.deleteNote),
    path('d/',views.deleteNote)
]