from django.shortcuts import render, redirect
import random
from datetime import datetime

# Create your views here.
def index(request):
    if not 'yourgold' in request.session:
        request.session['yourgold'] = 0
    if not 'goldlog' in request.session:
        request.session['goldlog'] = ''
    return render(request, 'index.html')

def findgold(request):
    if request.method == 'POST':
        print request.POST
        if request.POST['building'] == 'farm':
            goldchange = random.randrange(10,21)
            request.session['yourgold'] += goldchange
            newstatus = 'You earned '+str(goldchange)+' Time: '+str(datetime.now())+'\n'
            request.session['goldlog'] = newstatus + request.session['goldlog']
            return redirect('/')
        elif request.POST['building'] == 'cave':
            goldchange = random.randrange(5,11)
            request.session['yourgold'] += goldchange
            newstatus = 'You earned '+str(goldchange)+' Time: '+str(datetime.now())+'\n'
            request.session['goldlog'] = newstatus + request.session['goldlog']
            return redirect('/')
        elif request.POST['building'] == 'house':
            goldchange = random.randrange(2,6)
            request.session['yourgold'] += goldchange
            newstatus = 'You earned '+str(goldchange)+' Time: '+str(datetime.now())+'\n'
            request.session['goldlog'] = newstatus + request.session['goldlog']
            return redirect('/')
        elif request.POST['building'] == 'casino':
            goldchange = random.randrange(-50,51)
            request.session['yourgold'] += goldchange
            if goldchange == 0:
                newstatus = "You didn't earn any gold. Time: "+str(datetime.now())+"\n"
                request.session['goldlog'] = newstatus + request.session['goldlog']
            elif goldchange > 0:
                newstatus = 'You earned '+str(goldchange)+' Time: '+str(datetime.now())+'\n'
                request.session['goldlog'] = newstatus + request.session['goldlog']
            else:
                newstatus = 'You lost '+str(goldchange)+' Time: '+str(datetime.now())+'\n'
                request.session['goldlog'] = newstatus + request.session['goldlog']
            return redirect('/')
    else:
        return redirect (request, '/')
    
def reset(request):
    del request.session['yourgold']
    del request.session['goldlog']
    return redirect('/')