from rest_framework import serializers
from .models import (Survey,
                     SurveyQuestion,
                     SurveyQuestionAlternative,
                     SurveyUserAnswer)


# Define serializers class from our models.
class SurveyUserAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = SurveyUserAnswer
        fields = ('user_answer',
                  'user_choice')


class SurveyQuestionAlternativeSerializer(serializers.ModelSerializer):
    survey_question = SurveyUserAnswerSerializer(
        many=True, read_only=True)

    class Meta:
        model = SurveyQuestionAlternative
        fields = ('first_alternative',
                  'second_alternative',
                  'third_alternative',
                  'survey_question',)


class SurveyQuestionSerializer(serializers.ModelSerializer):
    survey_name = SurveyQuestionAlternativeSerializer(
        many=True, read_only=True)

    class Meta:
        model = SurveyQuestion
        fields = ('survey',
                  'question',
                  'question_id',
                  'survey_name')


class SurveySerializer(serializers.ModelSerializer):
    question = SurveyQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        fields = ('survey_id',
                  'survey_name',
                  'question')
