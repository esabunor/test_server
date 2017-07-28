"""test_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from addressesapp.views import get_contacts, delete_person, main, notfound, addressesbook
from addressesapp.api import AddressesList

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$',main),
    url(r'^book/$',addressesbook,name='addressesbook'),
    url(r'^delete/(?P<name>.*)/$',delete_person,name='delete_person'),
    url(r'^book-search/$',get_contacts, name='get_contacts'),
    url(r'^addresses-list/$', AddressesList.as_view(), name='addresses-list'),
    url(r'^notfound/$',notfound,name='notfound')
]
