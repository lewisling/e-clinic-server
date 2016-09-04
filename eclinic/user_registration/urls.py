from django.conf.urls import url

from .views import UserList

urlpatterns = [
    url(r'^users/$', UserList.as_view()),
    url(r'^doctors/$', DoctorList.as_view()),
    url(r'^patients/$', PatientList.as_view())
]
