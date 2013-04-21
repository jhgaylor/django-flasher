from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'notecard.views.list_decks', name='index'),
    url(r'^decks/$', 'notecard.views.list_decks', name='decks'),
    url(r'^decks/(?P<deck_id>\d+)/$', 'notecard.views.list_cards_in_deck', name='deck_details'),
    url(r'^cards/(?P<card_id>\d+)/$', 'notecard.views.notecard_details', name='card_details'),
    url(r'^decks/new/$', 'notecard.views.create_deck', name='create_deck'),
    url(r'^cards/new/(?P<deck_id>\d+)/$', 'notecard.views.create_card', name='create_card'),
    # url(r'^flasher/', include('flasher.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
)
