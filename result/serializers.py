from result.models import Photos, Results
from rest_framework import serializers


class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = [
            "name","image"
        ]



class PhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = ["image"
        ]
