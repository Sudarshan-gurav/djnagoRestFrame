from django.contrib import admin
from django.urls import path
from . views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('',alldeilds_detail,name='allfeilds'),
    path('add/',alldeilds_detail,name='add'),
    path('',home,name='home'),
    path('edit/<int:pk>',editField,name='edit'),
    path('delete/<int:pk>',deleteField,name='delete'),
    path('form/',form_Forms,name='form'),
    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)