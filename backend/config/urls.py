from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from tours.views import FrontendIndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tours.urls')),
    path('', FrontendIndexView.as_view(), name='frontend-index'),

    # Direct static file serving for root css, js, and assets directories in local development
    re_path(r'^css/(?P<path>.*)$', serve, {'document_root': settings.BASE_DIR.parent / 'css'}),
    re_path(r'^js/(?P<path>.*)$', serve, {'document_root': settings.BASE_DIR.parent / 'js'}),
    re_path(r'^assets/(?P<path>.*)$', serve, {'document_root': settings.BASE_DIR.parent / 'assets'}),
]
