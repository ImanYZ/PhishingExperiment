import json
from random import randint
import random
import datetime
import time

from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from .models import HoltLaury
from .models import Gamble
from .models import Investment
from .models import Pretest
from .models import Thankyou

@ensure_csrf_cookie
def login(request):
    if request.method == 'POST':
        if 'username' in request.POST and request.POST['username'] != '':
            umid = request.POST['username']
            user, created = User.objects.get_or_create(username=umid)
            request.session['umid'] = user.username

    return welcome(request)

def logout(request):
    try:
        del request.session['umid']
    except KeyError:
        pass
    return render(request, 'games/Holt-Laury Lottery.html')

def welcome(request):
    if (request.session.get('umid', False)):
        umid = request.session['umid']
    else:
        umid = ""
    context = { 'umid': umid, 'welcomepage': 1 }
    return render(request, 'games/Welcome.html', context)

@ensure_csrf_cookie
def pretest(request, question):
    if request.session.get('umid', False) and request.session['umid'] != "":
        request.session['started'] = datetime.datetime.now().strftime("%b %d %Y %I:%M:%S %p")
        umid = request.session['umid']
        user = User.objects.get(username=umid)
        if user.pretest_set.count() != 0:
            if question == "":
                question = "1"
            question = int(question)
            pretest = user.pretest_set.all()[0]
            for i in range(1, question + 1):
                if i == 1:
                    answer = pretest.question1
                    correct = pretest.correct1
                elif i == 2:
                    answer = pretest.question2
                    correct = pretest.correct2
                elif i == 3:
                    answer = pretest.question3
                    correct = pretest.correct3
                elif i == 4:
                    answer = pretest.question4
                    correct = pretest.correct4
                elif i == 5:
                    answer = pretest.question5
                    correct = pretest.correct5
                elif i == 6:
                    answer = pretest.question6
                    correct = pretest.correct6
                elif i == 7:
                    answer = pretest.question7
                    correct = pretest.correct7
                if answer == -1:
                    question = i
                    context = { 'umid': umid, 'answer':answer, 'question':question, 'welcomepage':1 }
                    return render(request, 'games/Pretest.html', context)
            context = { 'umid': umid, 'answer':answer, 'question':question, 'correct':correct, 'welcomepage':1 }
            return render(request, 'games/Pretest.html', context)

        context = { 'umid': umid, 'question':1, 'welcomepage':1 }
        return render(request, 'games/Pretest.html', context)

    context = { 'umid': "" }
    return render(request, 'games/Pretest.html', context)

def pretestsubmit(request):
    if request.method == 'POST':
        if (request.session.get('umid', False) and request.session['umid'] != '' and
         'answer' in request.POST and request.POST['answer'] != '' and
         'questionclicked' in request.POST and request.POST['questionclicked'] != '' and
         'questionrightclicked' in request.POST and request.POST['questionrightclicked'] != '' and
         'questionhovered' in request.POST and request.POST['questionhovered'] != '' and
         'questionhoveredseconds' in request.POST and request.POST['questionhoveredseconds'] != '' and
         'question' in request.POST and request.POST['question'] != ''):
            
            umid = request.session['umid']
            answer = int(request.POST['answer'])
            questionclicked = int(request.POST['questionclicked'])
            questionrightclicked = int(request.POST['questionrightclicked'])
            questionhovered = int(request.POST['questionhovered'])
            questionhoveredseconds = float(request.POST['questionhoveredseconds'])
            question = int(request.POST['question'])
            user = User.objects.get(username=umid)
            pretest = None
            if user.pretest_set.count() != 0:
                pretest = user.pretest_set.all()[0]
            if question == 1:
                if answer == 0:
                    correct1 = 1
                else:
                    correct1 = 2
                if pretest == None:
                    user.pretest_set.create(
                        question1=answer,
                        correct1=correct1,
                        questionclicked1=questionclicked,
                        questionrightclicked1=questionrightclicked,
                        questionhovered1=questionhovered,
                        questionhoveredseconds1=questionhoveredseconds,
                        startedquestion1=datetime.datetime.strptime(request.session['started'], '%b %d %Y %I:%M:%S %p'),
                        finishedquestion1=datetime.datetime.now())
                return redirect('../pretest/2/')
            if question == 2:
                if answer == 1:
                    correct2 = 1
                else:
                    correct2 = 2
                if pretest.question2 == -1:
                    user.pretest_set.update(
                        question2=answer,
                        correct2=correct2,
                        questionclicked2=questionclicked,
                        questionrightclicked2=questionrightclicked,
                        questionhovered2=questionhovered,
                        questionhoveredseconds2=questionhoveredseconds,
                        startedquestion2=datetime.datetime.strptime(request.session['started'], '%b %d %Y %I:%M:%S %p'),
                        finishedquestion2=datetime.datetime.now())
                return redirect('../pretest/3/')
            if question == 3:
                if answer == 0:
                    correct3 = 1
                else:
                    correct3 = 2
                if pretest.question3 == -1:
                    user.pretest_set.update(
                        question3=answer,
                        correct3=correct3,
                        questionclicked3=questionclicked,
                        questionrightclicked3=questionrightclicked,
                        questionhovered3=questionhovered,
                        questionhoveredseconds3=questionhoveredseconds,
                        startedquestion3=datetime.datetime.strptime(request.session['started'], '%b %d %Y %I:%M:%S %p'),
                        finishedquestion3=datetime.datetime.now())
                return redirect('../pretest/4/')
            if question == 4:
                if answer == 0:
                    correct4 = 1
                else:
                    correct4 = 2
                if pretest.question4 == -1:
                    user.pretest_set.update(
                        question4=answer,
                        correct4=correct4,
                        questionclicked4=questionclicked,
                        questionrightclicked4=questionrightclicked,
                        questionhovered4=questionhovered,
                        questionhoveredseconds4=questionhoveredseconds,
                        startedquestion4=datetime.datetime.strptime(request.session['started'], '%b %d %Y %I:%M:%S %p'),
                        finishedquestion4=datetime.datetime.now())
                return redirect('../pretest/5/')
            if question == 5:
                if answer == 1:
                    correct5 = 1
                else:
                    correct5 = 2
                if pretest.question5 == -1:
                    user.pretest_set.update(
                        question5=answer,
                        correct5=correct5,
                        questionclicked5=questionclicked,
                        questionrightclicked5=questionrightclicked,
                        questionhovered5=questionhovered,
                        questionhoveredseconds5=questionhoveredseconds,
                        startedquestion5=datetime.datetime.strptime(request.session['started'], '%b %d %Y %I:%M:%S %p'),
                        finishedquestion5=datetime.datetime.now())
                return redirect('../pretest/6/')
            if question == 6:
                if answer == 0:
                    correct6 = 1
                else:
                    correct6 = 2
                if pretest.question6 == -1:
                    user.pretest_set.update(
                        question6=answer,
                        correct6=correct6,
                        questionclicked6=questionclicked,
                        questionrightclicked6=questionrightclicked,
                        questionhovered6=questionhovered,
                        questionhoveredseconds6=questionhoveredseconds,
                        startedquestion6=datetime.datetime.strptime(request.session['started'], '%b %d %Y %I:%M:%S %p'),
                        finishedquestion6=datetime.datetime.now())
                return redirect('../pretest/7/')
            if question == 7:
                if answer == 0:
                    correct7 = 1
                else:
                    correct7 = 2
                if pretest.question7 == -1:
                    user.pretest_set.update(
                        question7=answer,
                        correct7=correct7,
                        questionclicked7=questionclicked,
                        questionrightclicked7=questionrightclicked,
                        questionhovered7=questionhovered,
                        questionhoveredseconds7=questionhoveredseconds,
                        startedquestion7=datetime.datetime.strptime(request.session['started'], '%b %d %Y %I:%M:%S %p'),
                        finishedquestion7=datetime.datetime.now())
                return redirect('../pretest/results')
    context = { 'umid': "" }
    return render(request, 'games/pretest.html', context)

def pretestresults(request):
    if request.session.get('umid', False) and request.session['umid'] != "":
        umid = request.session['umid']
        user = User.objects.get(username=umid)
        if user.pretest_set.count() != 0:
            question = 7
            pretest = user.pretest_set.all()[0]
            correct = [-1]*8
            for i in range(1, question + 1):
                if i == 1:
                    answer = pretest.question1
                    correct[1] = pretest.correct1
                elif i == 2:
                    answer = pretest.question2
                    correct[2] = pretest.correct2
                elif i == 3:
                    answer = pretest.question3
                    correct[3] = pretest.correct3
                elif i == 4:
                    answer = pretest.question4
                    correct[4] = pretest.correct4
                elif i == 5:
                    answer = pretest.question5
                    correct[5] = pretest.correct5
                elif i == 6:
                    answer = pretest.question6
                    correct[6] = pretest.correct6
                elif i == 7:
                    answer = pretest.question7
                    correct[7] = pretest.correct7
                if answer == -1:
                    question = i
                    context = { 'umid': umid, 'answer':answer, 'question':question, 'welcomepage':1 }
                    return render(request, 'games/Pretest.html', context)
            correctResult = 0
            wrongResult = 0
            for i in range(1, 8):
                if correct[i] == 1:
                    correctResult = correctResult + 1
                elif correct[i] == 2:
                    wrongResult = wrongResult + 1
            context = { 'umid': umid, 'answer':answer, 'question':question, 
                'correctResult':correctResult, 'wrongResult':wrongResult, 'welcomepage':1 }
            return render(request, 'games/Pretest Results.html', context)

        return redirect('../1/')

    context = { 'umid': "" }
    return render(request, 'games/Pretest.html', context)

def training(request):
    if (request.session.get('umid', False)):
        umid = request.session['umid']
    else:
        umid = ""
    context = { 'umid': umid }
    return render(request, 'games/Training.html', context)

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
        if (request.session.get('umid', False) and request.session['umid'] != '' and
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
                            result = 5
                        else:
                            result = 4
                    else:
                        if die[index] <= decision:
                            result = 9.5
                        else:
                            result = 1
            
            if user.holtlaury_set.count() == 0:
                user.holtlaury_set.create(decision=decision,
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
    context = { 'umid': "" }
    return render(request, 'games/Holt-Laury Lottery.html', context)

def lotteryWillingness(request):
    if request.method == 'POST':
        requestPost = json.loads(request.body.decode('utf-8'))
        if (request.session.get('umid', False) and request.session['umid'] != '' and
         'willingnessNum' in requestPost and requestPost['willingnessNum'] != ''):
            
            umid = request.session['umid']
            willingnessNum = requestPost['willingnessNum']
            user = User.objects.get(username=umid)

            willingnessRand = round(randint(0, int((1 - 0) / 0.01)) * 0.01 + 0, 2)

            holtLaury = user.holtlaury_set.all()[0]
            result = holtLaury.points
            originalPoints = holtLaury.originalPoints
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
                'option':option, 'die':die, 'result':result, 'originalPoints':originalPoints })
    context = { 'umid': "" }
    return render(request, 'games/Holt-Laury Lottery.html', context)

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
        if (request.session.get('umid', False) and request.session['umid'] != '' and
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
                        result = 4 + 1 * (index - 1)
                    else:
                        result = 4 - 0.5 * (index - 1)
            
            if user.gamble_set.count() == 0:
                user.gamble_set.create(chosen=chosen,
                    coin1=coin[1], coin2=coin[2],
                    coin3=coin[3], coin4=coin[4],
                    coin5=coin[5], coin6=coin[6],
                    coin7=coin[7], coin8=coin[8],
                    coin9=coin[9], points=result, originalPoints=result,
                    started=datetime.datetime.strptime(request.session['started'], '%b %d %Y %I:%M:%S %p'),
                    finished=datetime.datetime.now())

            return JsonResponse({ 'chosen':chosen, 
                'coin':coin[chosen], 'result':result })
    context = { 'umid': "" }
    return render(request, 'games/Eckel-Grossman Gamble.html', context)

def gambleWillingness(request):
    if request.method == 'POST':
        requestPost = json.loads(request.body.decode('utf-8'))
        if (request.session.get('umid', False) and request.session['umid'] != '' and
         'willingnessNum' in requestPost and requestPost['willingnessNum'] != ''):
            
            umid = request.session['umid']
            willingnessNum = requestPost['willingnessNum']
            user = User.objects.get(username=umid)

            willingnessRand = round(randint(0, int((1 - 0) / 0.01)) * 0.01 + 0, 2)

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
    context = { 'umid': "" }
    return render(request, 'games/Eckel-Grossman Gamble.html', context)

@ensure_csrf_cookie
def investment(request):
    if request.session.get('umid', False) and request.session['umid'] != "":
        request.session['started'] = datetime.datetime.now().strftime("%b %d %Y %I:%M:%S %p")
        umid = request.session['umid']
        user = User.objects.get(username=umid)
        if user.investment_set.count() != 0:
            investment = user.investment_set.all()[0]
            invested = investment.invested

            if investment.otherreturned != -1 or investment.otherinvested != -1:
                context = { 'umid': umid, 'invested':invested, 'finished':1 }
                return render(request, 'games/Trust Game.html', context)

            context = { 'umid': umid, 'invested':invested }
            return render(request, 'games/Trust Game.html', context)
    
        context = { 'umid': umid }
        return render(request, 'games/Trust Game.html', context)

    context = { 'umid': "" }
    return render(request, 'games/Trust Game.html', context)

def investmentSubmit(request):
    if request.method == 'POST':
        if (request.session.get('umid', False) and request.session['umid'] != '' and
         'invested' in request.POST and request.POST['invested'] != ''):
            
            umid = request.session['umid']
            invested = request.POST['invested']
            user = User.objects.get(username=umid)

            if user.investment_set.count() == 0:
                user.investment_set.create(invested=invested,
                    startedinvested=datetime.datetime.strptime(request.session['started'], '%b %d %Y %I:%M:%S %p'),
                    finishedinvested=datetime.datetime.now())
            else:
                user.investment_set.update(invested=invested,
                    startedinvested=datetime.datetime.strptime(request.session['started'], '%b %d %Y %I:%M:%S %p'),
                    finishedinvested=datetime.datetime.now())

            return redirect('../returning/2/')
    context = { 'umid': "" }
    return render(request, 'games/Trust Game.html', context)

@ensure_csrf_cookie
def returned(request, part):
    if request.session.get('umid', False) and request.session['umid'] != "":
        request.session['started'] = datetime.datetime.now().strftime("%b %d %Y %I:%M:%S %p")
        umid = request.session['umid']
        user = User.objects.get(username=umid)
        if user.investment_set.count() != 0:
            if part == "":
                return redirect('../investment')
            part = int(part)
            if part >= 2 and part <= 7:
                investment = user.investment_set.all()[0]
                for i in range(2, part + 1):
                    if i == 2:
                        returned = investment.returned0
                    elif i == 3:
                        returned = investment.returned1
                    elif i == 4:
                        returned = investment.returned2
                    elif i == 5:
                        returned = investment.returned3
                    elif i == 6:
                        returned = investment.returned4
                    elif i == 7:
                        returned = investment.returned5
                    if returned == -1:
                        part = i
                        context = { 'umid': umid, 'returned':returned, 'part':part }
                        return render(request, 'games/Trust Game.html', context)
                if investment.otherreturned != -1 or investment.otherinvested != -1:
                    context = { 'umid': umid, 'returned':returned, 'part':part, 'finished':1 }
                    return render(request, 'games/Trust Game.html', context)
                context = { 'umid': umid, 'returned':returned, 'part':part }
                return render(request, 'games/Trust Game.html', context)
            else:
                return redirect('../investment')

        context = { 'umid': umid }
        return render(request, 'games/Trust Game.html', context)

    context = { 'umid': "" }
    return render(request, 'games/Trust Game.html', context)

def returnedSubmit(request):
    if request.method == 'POST':
        if (request.session.get('umid', False) and request.session['umid'] != '' and
         'returned' in request.POST and request.POST['returned'] != '' and
         'part' in request.POST and request.POST['part'] != ''):
            
            umid = request.session['umid']
            returned = int(request.POST['returned'])
            part = int(request.POST['part'])
            user = User.objects.get(username=umid)
            if part == 2:
                user.investment_set.update(
                    returned0=returned,
                    startedreturned0=datetime.datetime.strptime(request.session['started'], '%b %d %Y %I:%M:%S %p'),
                    finishedreturned0=datetime.datetime.now())
                return redirect('../returning/3/')
            if part == 3:
                user.investment_set.update(
                    returned1=returned,
                    startedreturned1=datetime.datetime.strptime(request.session['started'], '%b %d %Y %I:%M:%S %p'),
                    finishedreturned1=datetime.datetime.now())
                return redirect('../returning/4/')
            if part == 4:
                user.investment_set.update(
                    returned2=returned,
                    startedreturned2=datetime.datetime.strptime(request.session['started'], '%b %d %Y %I:%M:%S %p'),
                    finishedreturned2=datetime.datetime.now())
                return redirect('../returning/5/')
            if part == 5:
                user.investment_set.update(
                    returned3=returned,
                    startedreturned3=datetime.datetime.strptime(request.session['started'], '%b %d %Y %I:%M:%S %p'),
                    finishedreturned3=datetime.datetime.now())
                return redirect('../returning/6/')
            if part == 6:
                user.investment_set.update(
                    returned4=returned,
                    startedreturned4=datetime.datetime.strptime(request.session['started'], '%b %d %Y %I:%M:%S %p'),
                    finishedreturned4=datetime.datetime.now())
                return redirect('../returning/7/')
    context = { 'umid': "" }
    return render(request, 'games/Trust Game.html', context)

@ensure_csrf_cookie
def final(request):
    if request.method == 'POST':
        requestPost = json.loads(request.body.decode('utf-8'))
        if (request.session.get('umid', False) and request.session['umid'] != '' and
         'returned' in requestPost and requestPost['returned'] != ''):
            
            umid = request.session['umid']
            returned = int(requestPost['returned'])
            part = 7
            user = User.objects.get(username=umid)
            if user.investment_set.count() != 0:
                investment = user.investment_set.all()[0]
                if investment.otherreturned == -1 and investment.otherinvested == -1:
                    for i in range(2, part + 1):
                        if i == 2:
                            returned = investment.returned0
                        elif i == 3:
                            returned = investment.returned1
                        elif i == 4:
                            returned = investment.returned2
                        elif i == 5:
                            returned = investment.returned3
                        elif i == 6:
                            returned = investment.returned4
                        elif i == 7:
                            returned = int(requestPost['returned'])
                            user.investment_set.update(
                                returned5=returned,
                                startedreturned5=datetime.datetime.strptime(request.session['started'], '%b %d %Y %I:%M:%S %p'),
                                finishedreturned5=datetime.datetime.now())
                        if returned == -1:
                            part = i
                            context = { 'umid': umid, 'returned':returned, 'part':part }
                            return render(request, 'games/Trust Game.html', context)
                    
                    otherPlayer = None
                    otherPlayers = Investment.objects.filter(otherreturned=-1).filter(otherinvested=-1).exclude(user=user)
                    for other in otherPlayers:
                        if other.invested != -1 and other.returned5 != -1:
                            otherPlayer = other
                            break
                    print("otherPlayer: " + str(otherPlayer))
                    if otherPlayer == None:
                        return JsonResponse({ 'found':0 })
                    InvestOrReturn = random.getrandbits(1)
                    if InvestOrReturn:
                        investAmount = investment.invested
                        if investAmount == 0:
                            returnAmount = otherPlayer.returned0
                        elif investAmount == 1:
                            returnAmount = otherPlayer.returned1
                        elif investAmount == 2:
                            returnAmount = otherPlayer.returned2
                        elif investAmount == 3:
                            returnAmount = otherPlayer.returned3
                        elif investAmount == 4:
                            returnAmount = otherPlayer.returned4
                        elif investAmount == 5:
                            returnAmount = otherPlayer.returned5
                        investment.otherreturned = returnAmount
                        otherPlayer.otherinvested = investAmount

                        investment.points = 5 - investAmount + returnAmount
                        otherPlayer.points = 5 + (3 * investAmount) - returnAmount

                    else:
                        investAmount = otherPlayer.invested
                        if investAmount == 0:
                            returnAmount = investment.returned0
                        elif investAmount == 1:
                            returnAmount = investment.returned1
                        elif investAmount == 2:
                            returnAmount = investment.returned2
                        elif investAmount == 3:
                            returnAmount = investment.returned3
                        elif investAmount == 4:
                            returnAmount = investment.returned4
                        elif investAmount == 5:
                            returnAmount = investment.returned5
                        otherPlayer.otherreturned = returnAmount
                        investment.otherinvested = investAmount

                        otherPlayer.points = 5 - investAmount + returnAmount
                        investment.points = 5 + (3 * investAmount) - returnAmount

                    investment.otheruser = otherPlayer.user
                    otherPlayer.otheruser = user
                    investment.save()
                    otherPlayer.save()

                    return JsonResponse({ 'InvestOrReturn':InvestOrReturn, 
                        'found': 1, 'returnAmount':returnAmount, 
                        'investAmount':investAmount, 'points':investment.points })
                else:
                    if investment.otherreturned != -1:
                        return JsonResponse({ 'InvestOrReturn':True, 
                            'found': 1, 'returnAmount':investment.otherreturned, 
                            'investAmount':investment.invested, 'points':investment.points })
                    elif investment.otherinvested != -1:
                        return JsonResponse({ 'InvestOrReturn':False, 'found': 1, 
                            'returnAmount':investment.otheruser.investment_set.all()[0].otherreturned, 
                            'investAmount':investment.otherinvested, 'points':investment.points })
            context = { 'umid': umid }
            return render(request, 'games/Trust Game.html', context)

    context = { 'umid': "" }
    return render(request, 'games/Trust Game.html', context)

@ensure_csrf_cookie
def thankyou(request):
    if (request.session.get('umid', False)):
        umid = request.session['umid']
        context = { 'umid': umid }
        return render(request, 'games/Thankyou.html', context)
    context = { 'umid': "" }
    return render(request, 'games/Thankyou.html', context)

def thankyousubmit(request):
    if request.method == 'POST':
        if ('trainingComment' in request.POST and 'gamesComment' in request.POST and 
            request.session.get('umid', False) and request.session['umid'] != ''):
            umid = request.session['umid']
            trainingComment = request.POST['trainingComment']
            gamesComment = request.POST['gamesComment']

            user = User.objects.get(username=umid)
            if user.thankyou_set.count() == 0:
                user.thankyou_set.create(trainingComment=trainingComment,
                    gamesComment=gamesComment)
            else:
                user.thankyou_set.update(trainingComment=trainingComment,
                    gamesComment=gamesComment)

            return JsonResponse({  })
    context = { 'umid': "" }
    return render(request, 'games/Trust Game.html', context)

