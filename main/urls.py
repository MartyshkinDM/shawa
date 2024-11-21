from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from . import views
app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    #path('points', views.shawarma_points_list, name='shawarma_points_list'),
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)