from django.urls import path
from .views import index, verifay, details, xabr_yuborish, send_filter

app_name = 'index'
urlpatterns = [
    path('', index, name='index'),
    path('verifay/', verifay, name='verifay'),
    path('details/<int:pk>', details, name='details'),
    path('xabar-yuborish', xabr_yuborish, name='xabar_yuborish'),
    path('send_filter', send_filter, name='send_filter'),
]