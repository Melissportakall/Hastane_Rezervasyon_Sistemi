from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patient-login/', views.patient_login, name='patient_login'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('login/', views.login, name='login'),  # Genel giriş URL'si
    path('test/', views.test, name='test'),
    path('patient-signup/', views.patient_signup, name='patient_signup'),
    path('patient_login', views.hastalogin_view, name='patient_login'),
    path('doctor-signup/', views.doctor_signup, name='doctor_signup'),
    path('doctor_loginview/', views.doctorlogin_view, name='doctor_loginview'),
    path('doctor_login/', views.doctor_login, name='doctor_login'),
    path('hasta_isim/', views.hastaisimtanimlama,name='hasta_isim'),
    path('randevu/', views.randevu_ekrani,name='randevu'),
    path('rapor/', views.rapor_view,name='rapor'),
    path('randevu-doktor', views.randevu_ekrani_doktor, name='randevu-doktor'),
    path('randevuu/', views.randevu_ekrani, name='randevuu'),
    path('hastarandevual/', views.hastarandevual, name='hastarandevual'),
    path('randevual/', views.randevual, name='randevual'),
    path('randevualkaydet/', views.randevualkaydet, name='randevualkaydet'),
    path('randevualekle/', views.randevualekle, name='randevualekle'),
    path('randevu-iptal/', views.randevuiptal, name='randevu-iptal'),
]

