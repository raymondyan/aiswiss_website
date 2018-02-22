from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from hospital.views import show_hospital

urlpatterns = [
                  path('admin/', admin.site.urls),
                  url(r'^hospital/(.+)/$', show_hospital),
                  url(r'^froala_editor/', include('froala_editor.urls')),
                  path('', include('website.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
