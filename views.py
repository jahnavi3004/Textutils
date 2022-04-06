from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    #Get the text
    djtext = request.GET.get('text','default')

    #check checkbox values
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    extraspaceremover = request.GET.get('extraspaceremover','off')
    charactercounter = request.GET.get('charactercounter','off')

    #check which checkbox is on
    if removepunc == "on":
        #analyzed = djtext
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Remove Punctuation', 'analyzed_text':analyzed}
        #Analyze the text
        return render(request, 'analyze.html', params)
    elif fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to UPPERCASE', 'analyzed_text':analyzed}  
        return render(request, 'analyze.html', params)  
    elif extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'Remove Extra Space', 'analyzed_text':analyzed}  
        return render(request, 'analyze.html', params)        
    elif newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose':'New Line Remover', 'analyzed_text':analyzed}  
        return render(request, 'analyze.html', params)
    elif charactercounter == 'on':
        count = 0
        for char in range(0,len(djtext)):
            if djtext[char] != " ":
                count = count + 1
        analyzed = str(count)
        params = {'purpose':'Character Counter', 'analyzed_text':analyzed}  
        return render(request, 'analyze.html', params) 
    else:
        return HttpResponse("error")                    
