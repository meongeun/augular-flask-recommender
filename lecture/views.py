from django.http import JsonResponse
from rest_framework.parsers import JSONParser

from .models import Lecture, Category
from rest_framework import viewsets
from .serializers import LectureSerializer, CategorySerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class LectureViewSet(viewsets.ModelViewSet):
    serializer_class = LectureSerializer
    queryset = Lecture.objects.all()
    authentication_classes = (TokenAuthentication, ) #기본적으로는 하나의 Auth를 이용하는데 추가할 수 있음
    permission_classes = (IsAuthenticated, )   # 이 함수는 authentication이 필요


def category_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Category.objects.all()
        serializer = CategorySerializer(snippets, many=True) # many=True 속성은 list일 때 쓰임??
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':

        data = JSONParser().parse(request)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)