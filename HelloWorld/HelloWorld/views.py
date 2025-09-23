from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from funasr import AutoModel
import tempfile
from django.views.decorators.csrf import csrf_exempt


model = AutoModel(
    model="iic/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch"
)


def get_xframe_options_value():
    return "SAMEORIGIN"


def hello(request):
    return HttpResponse("Hello World!")


def runoob(request):
    context = {}
    context["name"] = "三丰"
    views_list = ["菜鸟教程1", "菜鸟教程2", "菜鸟教程3"]
    context["views_list"] = views_list
    context["list_empty"] = []
    context["age"] = 18

    context["views_str"] = "<a href='https://www.runoob.com/'>点击跳转</a>"

    return render(request, "runoob.html", context=context)


def extendTpl(request):
    context = {}
    return render(request, "extend.html", context=context)


def uploadView(request):
    return render(request, "uploadView.html", context={})


@require_http_methods(["POST"])
@csrf_exempt
def uploadFile(request):
    file = request.FILES["file"]
    # print('文件大小。。。', file.size)
    # 保存上传的文件
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        content = file.read()
        tmp_file.write(content)
        tmp_file_path = tmp_file.name

    # 语音识别
    result = model.generate(input=tmp_file_path)
    # print(result)
    return JsonResponse(
        {"text": result[0]["text"], "confidence": 10, "file_size": len(content)}
    )
