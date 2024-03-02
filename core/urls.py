from django.urls import path, include
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.index),
    path('index',views.index, name='index'),
    path('event',views.event),
    path('contact',views.contact),
    path('book',views.book,name='book'),
    path('success',views.success,name="success"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
