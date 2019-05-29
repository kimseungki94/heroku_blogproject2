from django.contrib import admin
from django.urls import path
import BlogProjectApp.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',BlogProjectApp.views.home,name="home"),
]
