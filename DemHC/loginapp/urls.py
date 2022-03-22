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
path('blogs',views.blogs,name="blogs"),
path('about',views.about,name="about"),
path('add',views.add,name="add"),
# path('admin/', admin.site.urls),
path('post',views.post,name="post"),
path('detail/<int:id>',views.detail,name="detail"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)