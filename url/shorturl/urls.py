
from django.contrib import admin
from django.urls import path
from urlapp.views import index,get_actual_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('get-actual-url/<str:url>',get_actual_url,name="get_actual_ull"),
]
