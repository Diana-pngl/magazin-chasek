from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from magazin_chasek import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.abra_items, name='glavnaya'),                     
    path('kartacka/<int:chislo>/', views.abra_kartacka),
    path('karzina/', views.abra_karzina, name='karzina'),
    path('profil/', views.abra_profil),
    path('accounts/login/', views.abra_vxod, name='vxod'),
    path('vixod_acaunt/', views.abra_vixod),
    path('fdRegistracii/', views.abra_fdr),
    path('dobavit_v_korzina/', views.abra_dvk),
    path('dobavit_iz_korzina/', views.abra_dik),
    path('plus/', views.abra_plus),
    path('minus/', views.abra_minus)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
