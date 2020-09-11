from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lecture/', include('lecture.urls')),  #lecture 앱을 실행시킨다
]
