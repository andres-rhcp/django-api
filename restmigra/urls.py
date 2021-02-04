from django.conf.urls import url 
from restmigra import views 
 
urlpatterns = [ 
    url(r'^api/restmigra$', views.user_list),
    url(r'^api/restmigra/(?P<pk>[0-9]+)$', views.user_detail)
    # url(r'^api/rest/published$', views.user_list_published)
]
