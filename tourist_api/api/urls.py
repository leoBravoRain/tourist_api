# api/urls.py

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, Create_View_Videos_Location, Create_Place

urlpatterns = {

    url(r'^location/(?P<place_id>[\w\ ]+)/$$', CreateView.as_view(), name="create"),

    url(r'^videos_location/(?P<location_id>[\w\ ]+)/$', Create_View_Videos_Location.as_view(), name="create"),

	url(r'^place/$', Create_Place.as_view(), name="create_place"),

}

urlpatterns = format_suffix_patterns(urlpatterns)