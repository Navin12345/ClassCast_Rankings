from django.conf.urls import url
from webapp import views


urlpatterns = [
    url(r'^rankings/(?P<student_id>[A-Za-z0-9_.-]+)/$', views.rankings.as_view(), name='rankings'),
]
