from django.urls import path
from . import views 
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.urls import path
from .views import SignUpView
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path ('', views.inicio, name='inicio'),
    path ('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crear, name='crear'),
    path('libros/editar', views.editar, name='editar'),
    path('eliminar/<int:id>' ,views.eliminar, name= 'eliminar'),
    path('libros/editar/<int:id>' ,views.editar, name= 'editar'),

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

