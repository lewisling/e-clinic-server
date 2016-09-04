from django.conf.urls import url
from .views import ReservationList


urlpatterns = [
    url(r'^reservations/$', ReservationList.as_view())
]
