from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import xml.dom.minidom
import urllib.request as ur

def converterView(request):

    #parse GET request parameters
    amount = request.GET.get('amount', '')
    src_currency = request.GET.get('src_currency', '')
    dest_currency = request.GET.get('dest_currency', '')
    reference_date = request.GET.get('reference_date', '')

    #get exchange rates for reference date from file
    src_rate = 1 if src_currency=='EUR' else getEuroExchangeRate(reference_date, src_currency)
    dst_rate = 1 if dest_currency=='EUR' else getEuroExchangeRate(reference_date, dest_currency)

    #calculate amount in dest_currency and construct response
    if(isValidInput(amount, src_rate, dst_rate)):
        resultAmount = calculateDestCurrAmount(amount, dst_rate, src_rate)
    else:
        resultAmount = -1

    responseData = {
        'amount': resultAmount,
        'currency': dest_currency
    }
    return JsonResponse(responseData)

def getEuroExchangeRate(date, currency):

    #load xml from url
    doc = xml.dom.minidom.parse(ur.urlopen('https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml'))
    outerCube = doc.getElementsByTagName("Cube")[0]
    innerCubes = outerCube.getElementsByTagName("Cube")
    for cube in innerCubes:
        if ('time' in cube.attributes.keys() and cube.getAttribute('time')==date):
            for rate in cube.childNodes:
                if (rate.getAttribute('currency')==currency):
                    return rate.getAttribute('rate')
    return ''


def calculateDestCurrAmount(amount, dst_rate, src_rate):
    return (float(amount)*float(dst_rate)/float(src_rate))

def isValidInput(amount, src_rate, dst_rate):
    return int(amount)>0 and src_rate!='' and dst_rate!=''

def homepageView(request):

    return HttpResponse('welcome to the currency converter')
