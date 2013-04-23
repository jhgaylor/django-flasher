from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from notecard.models import Deck
from notecard.models import Notecard
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


@login_required
def index(request):
    data = {
        'foo': 'hello world'
    }

    return render_to_response('notecard/index.html',
                              data,
                              context_instance=RequestContext(request)
                              )


@login_required
def list_decks(request):
    decks = Deck.objects.filter(owner=request.user)
    data = {
        'decks': decks,
    }
    return render_to_response('notecard/list_decks.html',
                              data,
                              context_instance=RequestContext(request)
                              )


@login_required
def list_cards_in_deck(request, deck_id):
    cards = Notecard.objects.filter(deck=deck_id)
    data = {
        'cards': cards,
        'deck_id': deck_id
    }
    return render_to_response('notecard/list_cards_in_deck.html',
                              data,
                              context_instance=RequestContext(request)
                              )


@login_required
def notecard_details(request, card_id):
    card = Notecard.objects.get(pk=card_id)
    data = {
        'card': card
    }
    return render_to_response('notecard/view_card.html',
                              data,
                              context_instance=RequestContext(request)
                              )


@login_required
def create_card(request, deck_id):
    deck_object = Deck.objects.get(pk=deck_id)
    if request.POST:
        card = Notecard()
        card.name = request.POST['name']
        card.owner = request.user
        card.front = request.POST['front']
        card.back = request.POST['back']
        card.save()
        card.deck.add(deck_object)
    return redirect(deck_object.get_absolute_url())


@login_required
def create_deck(request):
    if request.POST:
        deck = Deck()
        deck.owner = request.user
        deck.name = request.POST['name']
        deck.save()
    return redirect(reverse('decks'))

@login_required    
def delete_card(request,card_id):
    card = Notecard.objects.get(pk=request.POST['card_id']).delete()
    return render_to_response("notecard/list_decks",
                        context_instance=RequestContext(request)
                        )
@login_required
def edit_deck(request):
    deck = Deck.objects.get(pk=request.POST['deck_id'])        
    deck.name = request.POST['name']
    deck.save()
    return redirect(reverse('decks'))



@login_required
def delete_deck(request,deck_id):
    deck = Deck.objects.get(pk=request.POST['deck_id']).delete()
    return render_to_response("notecard/list_decks",
                        context_instance=RequestContext(request)
                        )
@login_required
def modify_card(request):
    """
    This code retreives cards infromation then updates the card
    """
    card = Notecard.objects.get(pk=request.POST['card_id'])
    if "name" in request POST:
        card.name = request.POST['name']
    if "front" in request POST:
        card.name = request.POST['front']
    if "back" in request POST:
        card.name = request.POST['back']
    if "deck" in request POST:
        deck_ids = request.POST['deck'].split(",")
        for _id in deck_ids:
            card.decks.add(Deck.objects.get(pk=_id)
    card.save()
    return render_to_response("notecard/deck_list",
                            context_instance=RequestContext(request)
                            )
    



    





