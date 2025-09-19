from django.http import HttpResponse, JsonResponse

from TestModel.models import Test

# 新增
def saveDB(request):
    test1 = Test(name='test1', age=10)
    test1.save()
    return HttpResponse('<p>数据添加成功</p>')


# 查询数据库
def queryDB(request):
    # 查询所有的数据 select * from
    # listAll = Test.objects.all()
    # response = ''
    # for obj in  listAll:
    #     response += obj.name + '/'
    # return HttpResponse(response)

    # 通过filter设置过滤
    response = Test.objects.filter(id=2)
    result = ''
    for test in response:
        result += test.name + '<br>'
    return HttpResponse('<div>' + result + '</div>')

# 修改
def updateDB(request):
    test1 =  Test.objects.get(id=2)
    test1.name = '被修改后的名字'
    test1.save()
    return HttpResponse('修改成功')


def deleteDB(request):
    test1 = Test.objects.get(name='被修改后的名字')
    test1.delete()

    return HttpResponse('删除成功')