
#Code for practice
    # def index (request):
    #     return HttpResponse("Hello Rhutam")
    #
    # def only(request):
    #     return HttpResponse("Only Rhutam")

    # def linkNavigate(request):
    #     li ="""<h1>Personal Navigator<br></h1>
    #             <a href="https://trhutam.wixsite.com/theotheroutlook"> The Other Outlook </a><br>
    #             <a href="https://www.youtube.com/playlist?list=PLu0W_9lII9agiCUZYRsvtGTXdxkzPyItg"> Web Development Tutorials </a><br>
    #             <a href = "https://www.youtube.com/playlist?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME">PythonTutorials</a>"""
    #     return HttpResponse(li)

    # def acceptName(request):
    #     text=request.POST.get('djtext','No Name')
    #     return HttpResponse(f'Review:\n {text} ')

from django.http import HttpResponse
from django.shortcuts import render
#Backend Code for the texteditor website

def temp(request):
   return render(request,'index.html')

def textEditor(request):
    entertext = request.POST.get('editedtext', 'No Name')   # request.GET.get('textareaname',default display) This is used
    removepunc=request.POST.get('RemovePunc','off')         # to accept data from the user into the backend
    capletter=request.POST.get('capitalizer','off')
    esremover=request.POST.get('extraspaceremover','off')
    cc=request.POST.get('charcount','off')

    if esremover == 'on' and (len(entertext)) >0:
        analyzed=""
        for index, char in enumerate(entertext):
            if not (entertext[index] == " " and entertext[index + 1] == " "):
                analyzed = analyzed + char
        list = {'Objective': 'Edited Text', 'Analysed': f'{analyzed} '}
        entertext=analyzed

    if removepunc == 'on' and (len(entertext)) >0:
        punctuations = '''!()-[]{};:'"\,<>+./?@#$%^&*_~'''
        analyzed = ""
        for char in entertext:
            if char not in punctuations:
                analyzed = analyzed + char
        list = {'Objective': 'Edited Text', 'Analysed': f'{analyzed}'}
        entertext = analyzed

    if capletter== 'on'and (len(entertext)) >0:
        analyzed = entertext.upper()
        list = {'Objective': 'Edited Text', 'Analysed': f'{analyzed}' }
        entertext = analyzed

    if cc == 'on' and (len(entertext)) > 0:
        count = 0
        for char in entertext:
            count += 1
        list = {'Objective': 'Edited Text', 'Analysed': f'{analyzed} There are {count} characters in your text'}
        entertext = analyzed

    if cc != 'on' and capletter != 'on'and removepunc != 'on' and esremover != 'on':
        return HttpResponse("Error : You have not selected any options!")
    elif entertext is "":
        return HttpResponse("Error :You have not entered any text!")

    return render(request, 'analyze.html', list)


