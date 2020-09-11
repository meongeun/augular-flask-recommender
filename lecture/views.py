from .models import Lecture
from rest_framework import viewsets
from .serializers import LectureSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class LectureViewSet(viewsets.ModelViewSet):
    serializer_class = LectureSerializer
    queryset = Lecture.objects.all()
    authentication_classes = (TokenAuthentication, ) #기본적으로는 하나의 Auth를 이용하는데 추가할 수 있음
    permission_classes = (IsAuthenticated, )   # 이 함수는 authentication이 필요