from django.shortcuts import render
from rest_framework.decorators import api_view, schema
from rest_framework.response import Response
from api.module_test import cat_snn

# Create your views here.


@api_view(['POST'])
def SnnView(request):
    content = {'status': 'success', 'data': {}}
    try:
        content.data = cat_snn(r"api/archer_img/")
        return Response(content)
    except BaseException as e:
        content['status'] = 'fail'
        print('Failed to upload to ftp: '+ str(e))
        return Response(content)