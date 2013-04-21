from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from notecard.models import Deck
from notecard.models import Notecard

@login_required
def index(request):
    data = {
        'foo': 'hello world'
    }

    return render_to_response('notecard/index.html',
                              data,
                              context_instance=RequestContext(request)
                              )

def list_decks(request):
    decks = Deck.objects.filter(owner=request.user)
    data = {
        'decks':decks,
    }
    return render_to_response('notecard/deck_list.html',
                              data,
                              context_instance=RequestContext(request)
                              )

def list_cards_in_deck(request,deck_id):
    cards = Notecard.objects.filter(deck_id=deck_id)
    data = {
            'cards':decks,
    }

def view_notecard(request,id):
    notecard = Notecard.objects.filter(id=id)
    data = {
        'notecard':notecard
    }
    return render_to_response('notecard/view_card.html',
                             data,
                             context_instance=RequestContext(request)
                             )

def create_notecard(request,deck_id):
    if request.POST:
        #this was a form submission
        card = Notecard()
        card.name = request.POST['name']
        card.owner = request.user
        card.front = request.POST['front']
        card.back = request.POST['back']
        card.save()
        deck_object = deck.objects.get(pk=deck_id)
        card.decks.add(deck_object)
        return redirect(reverse(deck_object))
    else:
        #we need to render the template w/ the form on it
        return HttpResponse('notecard/new_card.html',
                            context_instance=RequestContext(request)
                            )

def create_deck(request):
    if rquest.POST:
        deck = Deck()
        deck.owner = request.user
        deck.name = reqest.POST['name']
        deck.save()
    else:
        #we need to render the template w/ the form on it
        return HttpResponse('notecard/new_deck.html',
                            context_instance=RequestContext(request)
                            )
