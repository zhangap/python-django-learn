from django.http import HttpResponse


from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello World!")


def runoob(request):
    context = {}
    context['name'] = '三丰'
    views_list = ['菜鸟教程1', '菜鸟教程2', '菜鸟教程3']
    context['views_list'] = views_list
    context['list_empty'] = []
    context['age'] = 18
    return render(request, 'runoob.html', context=context)