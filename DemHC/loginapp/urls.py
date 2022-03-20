from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
path('',views.log,name="log"),
path('login',views.login_view,name="login"),
path('logout',views.logout_view,name="logout"),
path('register/',views.registerPage,name="register"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)