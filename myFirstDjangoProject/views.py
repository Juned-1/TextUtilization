from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyze(request):
    djtext=request.POST.get('text','')
    removepunc=request.POST.get('removepunc','off')
    capschar=request.POST.get('capschar','off')
    newLineRemover=request.POST.get('newLineRemover','off')
    extraspaceRemover=request.POST.get('spaceRemover','off')
    charCount=request.POST.get('charCount','off')
    punctuations='''.?!,;:-_[]{}()'"\*<>@#$^%&~`'''
    purpose="|"
    string=djtext
    if removepunc=="on":
        analyzed=""
        for char in string:
            if char not in punctuations:
                analyzed = analyzed + char
        string=analyzed
        purpose=purpose+"Remove Punctuations|"
    if capschar=="on":
        string=string.upper()
        purpose=purpose+"Capitalize Character|"
    if newLineRemover == "on":
        analyzed=""
        for char in string:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        string=analyzed
        print(string)
        purpose=purpose+"Remove new Line|"
    if  extraspaceRemover== "on": #extra space remove
        analyzed=""
        for index,char in enumerate(string):  #enumeration is used in python to get index of list element when iterate over it
            if not(string[index]==" " and string[index+1]==" "):
                analyzed=analyzed+char
        string = analyzed
        purpose=purpose+"Remove Extra Space|"
    if  charCount== "on":
        analyzed= 0
        for char in enumerate(string):  #enumeration is used in python to get index of list element when iterate over it
            analyzed=analyzed+1
        string=string+"\nCharacter in the text is "+str(analyzed)
    if removepunc=="on" or capschar=="on" or newLineRemover=="on" or extraspaceRemover=="on" or charCount=="on":
        param={'purpose':purpose,'analyzedText':string}
        return render(request,'analyze.html',param)
    return HttpResponse("<h3>No character or text is entered by you to Utilize</h3><a href='../'>Go back</a>")
