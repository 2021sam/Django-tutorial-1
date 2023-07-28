from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import  login_required
from django.http import HttpResponse
from django.contrib import messages
from .models import Profile
from .forms import ProfileForm


# Create your views here.
# http://localhost:8000/profile/edit/1
# def profile_edit(request, id):

@login_required
def profile_edit(request):
    queryset = Profile.objects.filter(user=request.user)
        # post = get_object_or_404(queryset, pk=id)
    print(queryset)

    # for e in queryset:
    #     print(e.id)
    #     print(e.user)
    #     id = e.id
    #     print(f'id = {id}')

    return HttpResponse('POST this')
    
    
    # form = get_object_or_404(queryset, pk=id)

    # if request.method == 'GET':
    #     context = {'form': ProfileForm(instance=form), 'id': id}
    #     return render(request,'streetcred/profile_form.html',context)

    #     # return HttpResponse('GET this')

    # # elif request.method == 'POST':
    # #     return HttpResponse('POST this')


    # elif request.method == 'POST':
    #     form = ProfileForm(request.POST, instance=form)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'The post has been updated successfully.')
    #         return redirect('posts')
    #     else:
    #         messages.error(request, 'Please correct the following errors:')
    #         return render(request,'streetcred/profile_form.html',{'form':form})
