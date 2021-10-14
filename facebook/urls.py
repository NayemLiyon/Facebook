
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import fheack

#_____CHANGE ADMIN PANEL_____
admin.site.site_header = 'Facebook'
admin.site.site_title = 'Heack'
admin.site.index_title = 'Runing Heack'



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('fheack.urls',namespace='index')),
   

]


#ami for static foder
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
