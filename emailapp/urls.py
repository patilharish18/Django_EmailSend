from django.urls import path
from.import views

urlpatterns = [
    path('', views.mypage,name="mypage"),
    path('save/',views.send_mail,name='savetodb'),
]
