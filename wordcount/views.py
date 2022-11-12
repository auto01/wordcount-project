from django.http import HttpResponse
from django.shortcuts import render


def get_word_cnt(s):
    c=0
    words=s.split(" ")
    return len(words)

def get_word_dict(s):
    wd={}
    for w in s.split():
        if w in wd:
            wd[w]+=1
        else:
            wd[w]=1
    return wd


def homepage(request):

    return render(request,'home.html')
    
def aboutpage(request):
    return render(request,'about.html')

def count(request):
    fulltext=request.GET['fulltext']
    print(fulltext)
    cnt=get_word_cnt(fulltext)
    wd=get_word_dict(fulltext)
    wd=sorted(wd.items(),key=lambda x:x[1],reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'cnt':cnt,'wd':wd})

