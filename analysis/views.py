from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .RCNNTree import getTreeLabel
from .RCNNPerson import getPersonLabel
from .RCNNHouse import getHouseLabel
from time import sleep
import json
from datetime import datetime
from .models import *
from django.shortcuts import get_object_or_404


# Create your views here.
def inputImage(request):
    return render(request, 'analysis/inputImage.html')


num = 1


@csrf_exempt
def getPic(request):
    print("check")
    if request.method == 'POST':
        global num
        hoLo = handle_upload_file(request.FILES['house'], 'house', str(num))
        trLo = handle_upload_file(request.FILES['tree'], 'tree', str(num))
        perLo = handle_upload_file(request.FILES['person'], 'person', str(num))
        # SLEEP 1초(파일 저장시간)
        sleep(1)
        # 분석 모델 시작
        result1 = getHouseLabel(str(num))
        result2 = getTreeLabel(str(num))
        result3 = getPersonLabel(str(num))
        houseHtml = getLabelHTP(result1)
        treeHtml = getLabelHTP(result2)
        personHtml = getLabelHTP(result3)
        imgHouse = "<div style=\"display:block; margin: auto;\" class=\"col-md-4\">" \
                   "<img style=\"width: 20rem; height: 20rem;\" src=\"../../static/labelImage/houseLabel" + str(num) + ".jpg\">" \
                   "</div>" \
                   "<br>" + houseHtml
        imgTree = "<div style=\"display:block; margin: auto;\" class=\"col-md-4\">" \
                  "<img style=\"width: 20rem; height: 20rem;\" src=\"../../static/labelImage/treeLabel" + str(num) + ".jpg\">" \
                   "</div><br>" + treeHtml
        imgPerson = "<div style=\"display:block; margin: auto;\" class=\"col-md-4\">" \
                    "<img style=\"width: 20rem; height: 20rem;\" src=\"../../static/labelImage/personLabel" + str(num) + ".jpg\">" \
                   "</div><br>" + personHtml
        context = {'imgHouse': imgHouse, 'imgTree': imgTree, 'imgPerson': imgPerson, }
        num += 1
        return HttpResponse(json.dumps(context), "application/json")


def getLabelHTP(labelname):
    dnum = 0
    result = "<div style=\"display:block;\" class=\"col-md-8\">" \
             "<h3 style=\"text-align: left;\"><strong>그림 해석</strong></h3>" \
             "<ul style=\"line-height: 200%; text-align: justify; font-size: larger;\">"
    label = list(set(labelname['class']))

    for _ in label:
        labelEng = label[dnum]
        data = get_object_or_404(Label, label_eng=labelEng)
        labelContent = data.content
        result += "<li>" + labelContent + "</li>"
        dnum += 1

    result += "</ul></div>"
    return result


def handle_upload_file(f, name, count):
    fileLocation = './media/photos/' + name + '/' + name + count + '.jpg'
    with open(fileLocation, 'wb+') as destination:
        destination.write(f.read())
    return fileLocation