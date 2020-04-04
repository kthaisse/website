from django.conf.urls import url
from django.urls import include

from user import views

urlpatterns = [
    url(r"^login/$", views.user_login, name="user_login"),
    url(r"^logout/$", views.user_logout, name="user_logout"),
    url(r"^register/$", views.user_register, name="user_register"),
    url(r"^verify/(?P<verification_key>.+)$", views.verify, name="user_verify"),
    url(r"^send-verification/$", views.send_verification, name="user_sendverification"),
    url("", include("social_django.urls", namespace="social")),
]
