from django.urls import path
from . import views

urlpatterns = [
    path('<str:mail>/<str:number>',views.test_books),
    path('<str:email>',views.test_input)


]