"""Personal URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from home import views
from django.views.generic import TemplateView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^projects/',include('home.urls')),
    url(r'^$',views.index,name="home"),
    url(r'^contact$',TemplateView.as_view(template_name="home/contact.html"),name="contact"),
    url(r'^project/list$',TemplateView.as_view(template_name="home/project_list.html"),name="project_list"),
    url(r'^project/iot$',TemplateView.as_view(template_name="home/Iot_project.html"),name="iot"),
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
