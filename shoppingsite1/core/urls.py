from django.urls import path
from .views import DangNhap, UserView, dang_ky, HomePage, profile, password_change
from django.contrib.auth import views as auth_views
from django.conf import settings
from . import views

app_name = 'core'
urlpatterns = [
    path('login/', DangNhap.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login/logout.html'), name='logout'),
    path('register/', dang_ky, name='register'),
    path('profile/', profile, name='profile'),
    path('password_change/', password_change, name='password_change'),
    path('userview/', UserView.as_view(), name='user-view'),
    path('', HomePage.as_view(), name='index'),

]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)