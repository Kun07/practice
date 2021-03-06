from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/', user_views.register, name='register'),
    url(r'^profile/', user_views.profile, name='profile'),
    url(r'^login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    url(r'^', include('blog.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)