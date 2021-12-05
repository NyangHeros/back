from django.shortcuts import render
from rest_framework.decorators import api_view, schema
from rest_framework.response import Response
from api.module_test import cat_snn
from .models import Photos, Results
import urllib
import numpy as np
from skimage import io
import os
from django.core.files import File

# Create your views here.


@api_view(['POST'])
def SnnView(request):
    content = {'status': 'success', 'data': {}}
    photo = Photos()
    photo.cat_image = request.data['image']
    photo.save()
    cat_image_name = request.data['image'].name

    try:
        content['data'] = cat_snn(f'http://127.0.0.1:8000/media/static/images/{cat_image_name}')
        result = Results()
        result.name = content['data']
        result.image = request.data['image']
        result.save()
    except Exception as e:
        content['status'] = 'fail'
        content['data'] = photo.image_url
        print(f'/media/static/images/{cat_image_name}')
        print(str(e))
    return Response(content)