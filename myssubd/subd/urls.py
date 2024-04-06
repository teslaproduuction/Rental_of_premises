from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('Users/', views.Users, name='Users'),
    path('Pomechenia/', views.Pomechenia, name='Pomechenia'),
    path('Pomechenia/<int:pk>/', views.PomecheniaInfo, name='PomecheniaInfo'),
    path("signup/", views.signup.as_view(), name="signup"),
    path('Profil/<int:pk>/', views.ProfilUpdateView.as_view(), name='Profil'),
    path('Dogovor/<int:pk>/', views.Dogovors, name='Dogovors'),
    path('DogovorALL/', views.DogovorALL, name='DogovorALL'),
    path('DogovorInfo/<int:pk>/', views.DogovorInfo, name='DogovorInfo')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

