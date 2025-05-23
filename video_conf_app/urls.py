
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("",views.user_register,name='register'),
    path("login/",views.user_login,name='login'),
    path('home/', views.home, name='home'),
    path('meeting/', views.video_conf, name='meeting'),
    path('join_meeting/', views.join_room, name='join_meeting'),
    path('logout/',views.user_logout),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)