"""corporate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.home.views import index, service_page,service_details_page,contact_us, thank_you,support,about_us_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name="index"),
    path('service/',service_page, name="service"),
    path('sdetails/<int:id>', service_details_page, name="sdetails"),
    path('contact-us/', contact_us, name = "contact_us"),
    path('thank_you/', thank_you, name = "thank_you"),
    path('support/', support, name = "support"),
    path('about-us/', about_us_page, name = "aboutus"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)