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
class SurveyQuestionAlternativeViewSet(viewsets.ModelViewSet):
    serializer_class = SurveyQuestionAlternativeSerializer

    def get_queryset(self):
        survey = Survey.objects.all().values_list(
            'survey_name', flat=True)
        print(survey)
        for value in survey:
            queryset = SurveyQuestionAlternative.objects.prefetch_related(
                'survey_question')
            queryset = queryset.filter(
                survey_question__survey__survey_name=value)
        return queryset
