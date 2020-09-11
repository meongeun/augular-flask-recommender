from django.urls import path, include
from rest_framework import routers
from .views import LectureViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('lectures', LectureViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', obtain_auth_token),  #post로 아이디/비번을 보내면 해당 사용자의 토큰을 넘겨준다

]