
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import query_db

urlpatterns = {
    path('input', query_db, name="single_item")
}

urlpatterns = format_suffix_patterns(urlpatterns)