import json
from random import randint
import random
import datetime

from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render

from .models import User

@ensure_csrf_cookie
def login(request):
    if request.method == 'POST':
        if 'username' in request.POST and request.POST['username'] != '':
            umid = request.POST['username']
            user, created = User.objects.get_or_create(username=umid)
            request.session['umid'] = user.username

    return lottery(request)

def logout(request):
    try:
        del request.session['umid']
    except KeyError:
        pass
    return render(request, 'games/Holt-Laury Lottery.html')

@ensure_csrf_cookie
def lottery(request):
    if request.session.get('umid', False) and request.session['umid'] != "":
        request.session['started'] = datetime.datetime.now().strftime("%b %d %Y %I:%M:%S %p")
        umid = request.session['umid']
        user = User.objects.get(username=umid)
        if user.holtlaury_set.count() != 0:
            holtLaury = user.holtlaury_set.all()[0]
            decision = holtLaury.decision
            die = [None]*11
            die[1] = holtLaury.die1
            die[2] = holtLaury.die2
            die[3] = holtLaury.die3
            die[4] = holtLaury.die4
            die[5] = holtLaury.die5
            die[6] = holtLaury.die6
            die[7] = holtLaury.die7
            die[8] = holtLaury.die8
            die[9] = holtLaury.die9
            die[10] = holtLaury.die10
            option = [None]*11
            option[1] = holtLaury.option1
            option[2] = holtLaury.option2
            option[3] = holtLaury.option3
            option[4] = holtLaury.option4
            option[5] = holtLaury.option5
            option[6] = holtLaury.option6
            option[7] = holtLaury.option7
            option[8] = holtLaury.option8
            option[9] = holtLaury.option9
            option[10] = holtLaury.option10
            result = holtLaury.points
            originalPoints = holtLaury.originalPoints
            willingnessNum = holtLaury.willingness
            willingnessRand = holtLaury.willingnessRand
            context = { 'umid': umid, 'decision':decision, 'die':die,
                'option':option, 'result':result,
                'originalPoints':originalPoints, 'willingnessNum':willingnessNum,
                'willingnessRand':willingnessRand }
            return render(request, 'games/Holt-Laury Lottery.html', context)
    
        context = { 'umid': umid }
        return render(request, 'games/Holt-Laury Lottery.html', context)

    context = { 'umid': "" }
    return render(request, 'games/Holt-Laury Lottery.html', context)

def lotterySubmit(request):
    if request.method == 'POST':
        requestPost = json.loads(request.body.decode('utf-8'))
        if ('umid' in request.session and request.session['umid'] != '' and
         'DecisionsOption' in requestPost and requestPost['DecisionsOption'] != ''):
            
            umid = request.session['umid']
            DecisionsOption = requestPost['DecisionsOption']
            user = User.objects.get(username=umid)

            decision = randint(1, 10)
            die = [None]*11
            result = 0

            for index in range(1, 11): 
                die[index] = randint(1, 10)
                if decision == index:
                    if DecisionsOption[decision] == 0:
                        if die[index] <= decision:
                            result = 200
                        else:
                            result = 160
                    else:
                        if die[index] <= decision:
                            result = 385
                        else:
                            result = 10
            
            user.holtlaury_set.update_or_create(decision=decision,
                option1=DecisionsOption[1], option2=DecisionsOption[2],
                option3=DecisionsOption[3], option4=DecisionsOption[4],
                option5=DecisionsOption[5], option6=DecisionsOption[6],
                option7=DecisionsOption[7], option8=DecisionsOption[8],
                option9=DecisionsOption[9], option10=DecisionsOption[10],
                die1=die[1], die2=die[2],
                die3=die[3], die4=die[4],
                die5=die[5], die6=die[6],
                die7=die[7], die8=die[8],
                die9=die[9], die10=die[10],
                points=result, originalPoints=result,
                started=datetime.datetime.strptime(request.session['started'], '%b %d %Y %I:%M:%S %p'),
                finished=datetime.datetime.now())

            return JsonResponse({ 'decision':decision, 
                'die':die[decision], 'result':result })

def lotteryWillingness(request):
    if request.method == 'POST':
        requestPost = json.loads(request.body.decode('utf-8'))
        if ('umid' in request.session and request.session['umid'] != '' and
         'willingnessNum' in requestPost and requestPost['willingnessNum'] != ''):
            
            umid = request.session['umid']
            willingnessNum = requestPost['willingnessNum']
            user = User.objects.get(username=umid)

            willingnessRand = round(randint(0, int((15 - 0) / 0.01)) * 0.01 + 0, 2)

            holtLaury = user.holtlaury_set.all()[0]
            result = holtLaury.points
            if willingnessRand <= willingnessNum:
                result = holtLaury.points - willingnessRand
            decision = holtLaury.decision

            die = [None]*11
            die[1] = holtLaury.die1
            die[2] = holtLaury.die2
            die[3] = holtLaury.die3
            die[4] = holtLaury.die4
            die[5] = holtLaury.die5
            die[6] = holtLaury.die6
            die[7] = holtLaury.die7
            die[8] = holtLaury.die8
            die[9] = holtLaury.die9
            die[10] = holtLaury.die10
            option = [None]*11
            option[1] = holtLaury.option1
            option[2] = holtLaury.option2
            option[3] = holtLaury.option3
            option[4] = holtLaury.option4
            option[5] = holtLaury.option5
            option[6] = holtLaury.option6
            option[7] = holtLaury.option7
            option[8] = holtLaury.option8
            option[9] = holtLaury.option9
            option[10] = holtLaury.option10

            user.holtlaury_set.update(willingness=willingnessNum, willingnessRand=willingnessRand,
                points=result)

            return JsonResponse({ 'decision':decision, 'willingnessRand':willingnessRand,
                'option':option, 'die':die, 'result':result })

@ensure_csrf_cookie
def gamble(request):
    if request.session.get('umid', False) and request.session['umid'] != "":
        request.session['started'] = datetime.datetime.now().strftime("%b %d %Y %I:%M:%S %p")
        umid = request.session['umid']
        user = User.objects.get(username=umid)
        if user.gamble_set.count() != 0:
            gamble = user.gamble_set.all()[0]
            chosen = gamble.chosen
            coin = [None]*10
            coin[1] = gamble.coin1
            coin[2] = gamble.coin2
            coin[3] = gamble.coin3
            coin[4] = gamble.coin4
            coin[5] = gamble.coin5
            coin[6] = gamble.coin6
            coin[7] = gamble.coin7
            coin[8] = gamble.coin8
            coin[9] = gamble.coin9
            result = gamble.points
            originalPoints = gamble.originalPoints
            willingnessNum = gamble.willingness
            willingnessRand = gamble.willingnessRand
            context = { 'umid': umid, 'chosen':chosen, 'coin':coin, 'result':result,
                'originalPoints':originalPoints, 'willingnessNum':willingnessNum,
                'willingnessRand':willingnessRand }
            return render(request, 'games/Eckel-Grossman Gamble.html', context)
    
        context = { 'umid': umid }
        return render(request, 'games/Eckel-Grossman Gamble.html', context)

    context = { 'umid': "" }
    return render(request, 'games/Eckel-Grossman Gamble.html', context)

def gambleSubmit(request):
    if request.method == 'POST':
        requestPost = json.loads(request.body.decode('utf-8'))
        if ('umid' in request.session and request.session['umid'] != '' and
         'chosen' in requestPost and requestPost['chosen'] != ''):
            
            umid = request.session['umid']
            chosen = requestPost['chosen']
            user = User.objects.get(username=umid)

            coin = [None]*11
            result = 0

            for index in range(1, 10): 
                coin[index] = random.getrandbits(1)
                if chosen == index:
                    if coin[index]:
                        result = 160 + 40 * (index - 1)
                    else:
                        result = 160 - 20 * (index - 1)
            
            user.gamble_set.update_or_create(chosen=chosen,
                coin1=coin[1], coin2=coin[2],
                coin3=coin[3], coin4=coin[4],
                coin5=coin[5], coin6=coin[6],
                coin7=coin[7], coin8=coin[8],
                coin9=coin[9], points=result, originalPoints=result,
                started=datetime.datetime.strptime(request.session['started'], '%b %d %Y %I:%M:%S %p'),
                finished=datetime.datetime.now())

            return JsonResponse({ 'chosen':chosen, 
                'coin':coin[chosen], 'result':result })

def gambleWillingness(request):
    if request.method == 'POST':
        requestPost = json.loads(request.body.decode('utf-8'))
        if ('umid' in request.session and request.session['umid'] != '' and
         'willingnessNum' in requestPost and requestPost['willingnessNum'] != ''):
            
            umid = request.session['umid']
            willingnessNum = requestPost['willingnessNum']
            user = User.objects.get(username=umid)

            willingnessRand = round(randint(0, int((15 - 0) / 0.01)) * 0.01 + 0, 2)

            gamble = user.gamble_set.all()[0]
            result = gamble.points
            if willingnessRand <= willingnessNum:
                result = gamble.points - willingnessRand
            chosen = gamble.chosen

            coin = [None]*10
            coin[1] = gamble.coin1
            coin[2] = gamble.coin2
            coin[3] = gamble.coin3
            coin[4] = gamble.coin4
            coin[5] = gamble.coin5
            coin[6] = gamble.coin6
            coin[7] = gamble.coin7
            coin[8] = gamble.coin8
            coin[9] = gamble.coin9

            user.gamble_set.update(willingness=willingnessNum, willingnessRand=willingnessRand,
                points=result)

            return JsonResponse({ 'chosen':chosen, 'willingnessRand':willingnessRand,
                'coin':coin, 'result':result })

