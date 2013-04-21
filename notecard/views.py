from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    data = {
        'foo': 'hello world'
    }

    return render_to_response('notecard/index.html',
                              data,
                              context_instance=RequestContext(request)
                              )
