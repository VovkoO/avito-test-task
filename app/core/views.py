from django.shortcuts import render
from django.http import HttpResponse, FileResponse
import os

# Create your views here.
def get_mongo(request):
    # if request.method == 'GET':
    #     pwd = os.path.dirname(__file__)
    #     file = open(pwd + '/MongoDB.sh', 'r')
    #     return HttpResponse(file)

    if request.method == 'GET':
        pwd = os.path.dirname(__file__)
        response = FileResponse(open(pwd + '/MongoDB.sh', 'rb'))
        return response


def get_rabbit(request):
    # if request.method == 'GET':
    #     pwd = os.path.dirname(__file__)
    #     file = open(pwd + '/MongoDB.sh', 'r')
    #     return HttpResponse(file)

    if request.method == 'GET':
        pwd = os.path.dirname(__file__)
        response = FileResponse(open(pwd + '/RabbitMQ.sh', 'rb'))
        return response
