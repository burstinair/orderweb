# coding=utf8
from django.http import HttpResponse
from django.core.files import File
import json

def resolve(request):
    print len(request.body)
    
    # test: 将图片写入文件
    f = open('tmp/test.jpg', 'wb')
    f.write(request.body)
    f.close()
    
    # 返回解析结果
    result = {'status': 'success', 'result': [
        {'id': 1, 'name': '麻婆豆腐', 'price': 34.5},
        {'id': 2, 'name': '红烧肉', 'price': 23}
    ]}
    return HttpResponse(json.dumps(result))
 
def submit(request):
    print request.body
    
    # TODO 保存点菜结果
    
    return HttpResponse('{"status": "success"}')
 