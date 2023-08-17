# i have created this file

from django.http import HttpResponse
#import os
from django.shortcuts import render

'''
def about( request ):
    return HttpResponse("Hello Pragnesh In about")

#this was exe
def txt(request):
    cur_dir = os.path.abspath("textutils/1.txt")
    with open(cur_dir) as fd:
        return HttpResponse(fd.readlines())

'''
def index(request):
    return  render(request,'index.html')
    #return HttpResponse('''<h1>Hello pragnesh</h1> <a href="http://127.0.0.1:8000/removepunc" > open removepunc </a>''')
def about(request):
    about = ''' Hi There thanks for visiting my web site 
                    By using this Text Util you can play with text '''

    params = {'purpose':'About us' ,'analyzed_text' : about}
    return render(request,'analyze.html',params )
def contact(request):
    contact = ''' Contact use for any issue 
                    mo : 9723165311
                    Email : Pragneshrathod999@gmail.com'''
    params = {'purpose':'About us' ,'analyzed_text' : contact}
    return render(request,'analyze.html',params )
def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    capitalfirst = request.POST.get('capitalfirst','off')
    newlineremove = request.POST.get('newlineremove','off')
    charcont = request.POST.get('charcont','off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    if removepunc == "on":
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Remove punctuations' ,'analyzed_text' : analyzed}
        djtext = analyzed

    if fullcaps == "on":
       analyzed = ""
       for char in djtext:
           analyzed = analyzed + char.upper()
       params = {'purpose':'Convert in uppercase' ,'analyzed_text' : analyzed}
       djtext = analyzed

    if capitalfirst == "on":
        analyzed = ""
        analyzed = djtext.title()
        params = {'purpose':'First later capital of each word' ,'analyzed_text' : analyzed}
        djtext = analyzed

    if newlineremove == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and  char != '\r':
                analyzed =analyzed + char
        params = {'purpose':'Remove new line','analyzed_text' : analyzed}
        djtext = analyzed

    if charcont == 'on':
        analyzed = ""
        analyzed = len([char for char in djtext if char.isalpha()])
        params = {'purpose':'Charector count' ,'analyzed_text' : f'Total number of char is : {analyzed}'}

    if removepunc != 'on' and charcont != 'on' and newlineremove != 'on' and capitalfirst != 'on' and fullcaps != 'on':
        params = {'purpose':'Error! ' ,'analyzed_text' : 'please check analyze check box'}

    return render(request,'analyze.html',params)
