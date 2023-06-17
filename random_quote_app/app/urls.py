
from django.urls import path
from .views import quote

urlpatterns = [
    path("",quote,name="quote"),
    # path("/changes")
]
