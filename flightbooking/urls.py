"""flightbooking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from .views import home, index
from account.views import UserRegistrationView

urlpatterns = [
    path('', home, name='home'),
    path('index', index, name='index'),
    path('admin/', admin.site.urls),
    path('api/customer_account/', include(('customer_account.api.urls', 'customer_account'), namespace='customer-account-api')),
    path('api/flight/', include(('flight.api.urls', 'flight'), namespace='flight-api')),
    path('api/bookings/', include(('bookings.api.urls', 'bookings'), namespace='bookings-api')),
    path('user/', include('django.contrib.auth.urls')),
    path('user/register/', UserRegistrationView.as_view(), name='register'),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
]


if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))