"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.proj, name='proj')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='proj')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

# import sys
# path = '/home/test/PycharmProjects/pythonProject123/mysite'
# if path not in sys.path:
#   sys.path.append(path)

from proj import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.plswork)
]
#path('', include(('proj.urls', 'proj'), namespace='proj')),

#import sys
#sys.path.insert(0, '..proj')

