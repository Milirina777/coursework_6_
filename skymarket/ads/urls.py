from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from skymarket.ads.views import AdViewSet, CommentViewSet

router_ads = SimpleRouter()
router_ads.register("", AdViewSet, basename='ads')

router_comments = NestedSimpleRouter(parent_prefix="", parent_router=router_ads,
                                     lookup='ad')  # внешний ключ
router_comments.register("comments", CommentViewSet, basename='comments')

urlpatterns = []

urlpatterns += router_ads.urls
urlpatterns += router_comments.urls
