from result.models import Results
from rest_framework import serializers


class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = [
            "name","image"
        ]
