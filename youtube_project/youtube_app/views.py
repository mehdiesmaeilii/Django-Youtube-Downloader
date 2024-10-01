from django.shortcuts import render,redirect
from django.views.generic import View
from pytube import YouTube
# Create your views here.

def home(request):
    return render(request,'index.html')

def submit(request):
    url=request.GET['inp']
    url2=url[32]
    obj=YouTube(url)
    print(obj)
    streams=obj.streams.all()
    print(streams)
    # lp for list of pixels
    lp=[]
    for i in streams:
        lp.append(i.resolution)
# below statement will remove duplicate resolutions
    lp=list(dict.fromkeys(lp))      
    embed=url.replace('watch?v=','embed/')
    return render(request,'list.html',{'url':url,'url2':url2,'embed':embed,'lp':lp})


def down(request):
    path='c:/downloads/'
    # 360p
    pi=pixel[:4]     #this is for pixels
    val=pixel[4:]    #this is for video unique id
    str='www.youtube.com/watch?v='    #this is common link for every video
    obj=YouTube(str)
    obj.streams.get_by_resolution(pi).download(path)
    print("download success check in c:/downloads")
    return render(request,'index.html') 