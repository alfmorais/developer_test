from django.core import serializers
from django.http import JsonResponse
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from .models import (Survey,
                     SurveyQuestion,
                     SurveyQuestionAlternative,
                     SurveyUserAnswer)
from .serializers import (SurveySerializer,
                          SurveyQuestionSerializer,
                          SurveyQuestionAlternativeSerializer,
                          SurveyUserAnswerSerializer)


# define viewsets for classes created on serializers.py
class SurveyViewSet(viewsets.ModelViewSet):
    serializer_class = SurveySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Survey.objects.all()

    def get(self, request, format=None):
        """
        This method GET function will responsable for
        show all values regarding to Survey include
        all foreing key and database relationship
        """
        return Response({
            "message": "It's OK until now",
        })
