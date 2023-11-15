"""
URL configuration for ProcureIt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse
from ProcureIt.views import hello
from ProcureIt_0_0_1.views import *

urlpatterns = [
    path('', hello), # change to default page for app
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('list_vendors/', get_vendors, name='list_vendors'),
    path('get_vendor/<int:id>', get_vendordetails, name='get_vendor'),
    path('purchaseorders/', get_purchaseorders, name='get_purchaseorders'),
    path('get_podetails/<int:id>', get_purchaseorderdetails, name='get_podetails'),
    path('get_grns/', get_grns, name='get_grns'),
    path('grnitems/<int:id>', get_grndetails, name='grnitems'),
    path('update_grn/<int:id>', update_grn, name='update_grn'),
    path('update_grndetails/<int:id>', update_grndetails, name='update_grndetails'),
    path('update_podetails', update_purchaseorderdetails, name='update_podetails'),
    path('create_purchaseorder', create_purchaseorder, name='create_purchaseorder'),
    path('add_poitem/<int:id>', add_poitem, name='add_poitem'),
    path('create_grn', create_grn, name='create_grn'),
    path('delete_poitem/<int:id>', delete_purchaseorderitem, name='delete_purchaseorderitem'),
    path('delete_grnitem/<int:id>', delete_grnitem, name='delete_grnitem'),
    #path('welcome_view', welcome_view),
]
