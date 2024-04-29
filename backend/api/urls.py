
from django.urls import path
from api.views import CarView

urlpatterns = [
    path('car/', CarView.as_view(), name="get-car"),
]
