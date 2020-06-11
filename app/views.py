from django.shortcuts import render

# Create your views here.
def jinja(request):
    return render(request,'jinja.html',context = {'strikingperson':'Saran','nonstriking':'Logi'})
