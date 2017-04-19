from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken import views
from views import ItemViewSet

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', views.obtain_auth_token)
]
