from django.contrib import admin
from django.urls import path
from .views import resultsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('results/', resultsView),
]
