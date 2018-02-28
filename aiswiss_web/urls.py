from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from hospital.views import show_hospital
from school.views import show_school

urlpatterns = [
                  path('admin/', admin.site.urls),
                  url(r'^hospital/(.+)/$', show_hospital),
                  url(r'^school/(.+)/$', show_school),
                  url(r'^froala_editor/', include('froala_editor.urls')),
                  path('news/', include('news.urls')),
                  path('', include('website.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
