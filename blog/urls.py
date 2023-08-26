from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


app_name = 'blog'

urlpatterns=[
    path('',views.post_list,name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_details, name='post_detail'),

]





if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
