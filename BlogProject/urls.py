from django.contrib import admin
from django.urls import path,include
import BlogProjectApp.views
import PortfolioApp.views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',BlogProjectApp.views.home,name='home'),
    path('admin/', admin.site.urls),
    path('blog/',include('BlogProjectApp.urls')),
    path('accounts/',include('AccountsApp.urls')),
    path('portfolio/',PortfolioApp.views.portfolio,name="portfolio"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
