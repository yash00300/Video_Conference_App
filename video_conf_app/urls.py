
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("",views.user_register,name='register'),
    path("login/",views.user_login,name='login'),
    path('home/', views.home, name='home'),
    path('logout/',views.user_logout),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)