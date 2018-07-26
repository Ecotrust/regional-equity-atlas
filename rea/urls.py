from django.conf.urls import include, url
from rea import views as rea_views

urlpatterns = [
    url(r'^get_content', rea_views.get_content),
]
