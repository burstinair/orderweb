# from django.shortcuts import render
# from django.core import serializers
from django.http import HttpResponse
import json

def rec(request):
	result = {'result': int(request.GET['a']) + int(request.GET['b'])}
	# return HttpResponse(serializers.serialize('json', result))
	return HttpResponse(json.dumps(result))