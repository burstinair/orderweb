# coding=utf8
from django.http import HttpResponse
import json
from models import *


# 默认全部为同一Shop
shop = Shop(1, name="默认店")
shop.save()


def resolve(request):
    print len(request.body)

    # FixMe test: 将图片写入文件
    f = open('tmp/test.jpg', 'wb')
    f.write(request.body)
    f.close()

    # TODO 解析结果
    resolveResult = [
        {'name': '麻婆豆腐', 'price': 34.5},
        {'name': '红烧肉', 'price': 23}
    ]

    for dishResult in resolveResult:
        try:
            dish = Dish.objects.get(shop=shop, name=dishResult['name'])
        except Exception:
            dish = Dish(shop=shop, name=dishResult['name'], price=dishResult['price'])
        dish.save()
        dishResult['id'] = dish.pk

    # 返回结果
    result = {'status': 'success', 'result': resolveResult}
    return HttpResponse(json.dumps(result))


def submit(request):
    print request.body

    params = json.loads(request.body, "utf-8")
    order = Order(device_id=params['deviceId'])
    order.save()
    for orderItemRaw in params['orders']:
        orderItem = OrderItem(order=order, dish=Dish(orderItemRaw['id']), count=orderItemRaw['count'])
        orderItem.save()

    return HttpResponse('{"status": "success"}')
