from django.shortcuts import render_to_response


def index(request):
    data = {
        'foo': 'hello world'
    }

    return render_to_response('notecard/index.html',
                              data
                              )
