from django.core import serializers
from django.db.models import Prefetch
from django.http import JsonResponse
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from .models import (Survey, SurveyQuestion, SurveyQuestionAlternative,
                     SurveyUserAnswer)
from .serializers import (SurveyQuestionAlternativeSerializer,
                          SurveyQuestionSerializer, SurveySerializer,
                          SurveyUserAnswerSerializer)


# define viewsets for classes created on serializers.py
class SurveyViewSet(viewsets.ModelViewSet):
    serializer_class = SurveySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Survey.objects.all()


class SurveyQuestionViewSet(viewsets.ModelViewSet):
    serializer_class = SurveyQuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = SurveyQuestion.objects.all()


class SurveyQuestionAlternativeViewSet(viewsets.ModelViewSet):
    serializer_class = SurveyQuestionAlternativeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = SurveyQuestionAlternative.objects.all()


class SurveyUserAnswerViewSet(viewsets.ModelViewSet):
    serializer_class = SurveyUserAnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = SurveyUserAnswer.objects.all()
