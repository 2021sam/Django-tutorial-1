from django.shortcuts import render

# Create your views here.
@login_required
def profile_edit(request):
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        pass
