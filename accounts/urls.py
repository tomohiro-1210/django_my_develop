from django.urls import path
from .views import acconts_top

urlpatterns = [
    path('top/', acconts_top,name="accounts_top")
]
