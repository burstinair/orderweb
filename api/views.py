# from django.shortcuts import render
# from django.core import serializers
from django.http import HttpResponse
import json
from django.core.files import File

def rec(request):
	result = {'result': int(request.GET['a']) + int(request.GET['b'])}
	# return HttpResponse(serializers.serialize('json', result))
	return HttpResponse(json.dumps(result))

def resolve(request):
	f = open('tmp/test.jpg', 'w')
	f.write(request.body)
	f.close()
	return HttpResponse('{"status":"ok"}')