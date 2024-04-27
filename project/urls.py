
from django.contrib import admin
from django.urls import path
from app import views
 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('login',views.loginpage, name="login"),
    path('logout',views.logoutpage, name="logout"),
    path('register',views.register, name="register"),
    path('collections',views.collections, name="collections"),
    path('collectionsview/<str:name>',views.collectionsview, name="collectionsview"),
    path('addcard',views.add_card, name="addcard"),
    path('card',views.card ,name="card"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    