
from django.contrib import admin
from django.urls import path, include

# import myapp.urls to simply add them all together on the myapp folder
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls'))
]
