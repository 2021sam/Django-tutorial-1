from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import  login_required
from .models import Post
from .forms import PostForm
from django.utils.dateparse import parse_datetime
from django.http import JsonResponse

@login_required
def delete_post(request, id):
    queryset = Post.objects.filter(author=request.user)
    post = get_object_or_404(queryset, pk=id)
    context = {'post': post}    
    
    if request.method == 'GET':
        return render(request, 'blog/post_confirm_delete.html',context)
    elif request.method == 'POST':
        post.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('posts')        

@login_required    
def edit_post(request, id):
    queryset = Post.objects.filter(author=request.user)
    post = get_object_or_404(queryset, pk=id)

    if request.method == 'GET':
        context = {'form': PostForm(instance=post), 'id': id}
        return render(request,'blog/post_form.html',context)
    
    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been updated successfully.')
            return redirect('posts')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'blog/post_form.html',{'form':form})

@login_required
def create_post(request):
    if request.method == 'GET':
        context = {'form': PostForm()}
        return render(request,'blog/post_form.html',context)
    elif request.method == 'POST':

        # print(HttpRequest.POST)

        form = PostForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            # print(form['date_end'].value())
            date_end_str = form['date_end'].value()
            date_start_str = form['date_start'].value()
            date_end = parse_datetime(date_end_str)
            date_start = parse_datetime(date_start_str)
            duration = date_end - date_start
            user.duration = duration
            user.save()
            messages.success(request, 'The post has been created successfully.')
            return redirect('posts')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'blog/post_form.html',{'form':form})  


def skills(request):
    queryset = Post.objects.filter(author=request.user)
    count = queryset.count()
    print(count)
    d = {}
    d['count'] = count 
    for r in queryset:
        # print(r.skill1)
        # print(r.skill1_months)
        # print(r.skill1_years)
        print(f'{r.skill1}: {r.skill1_years} years, {r.skill1_months} months')
        print(f'{r.skill2}: {r.skill2_years} years, {r.skill2_months} months')
        # if r.skill1 not in d:
        #     d[r.skill1] = r.skill1_years * 12 + r.skill1_months
        # elif r.skill1 in d:
        #     d[r.skill1] += r.skill1_years * 12 + r.skill1_months

        
        # if r.skill1 not in d:
        #     d[r.skill1] = 0
        # d[r.skill1] += r.skill1_years * 12 + r.skill1_months

        # if r.skill2 not in d:
        #     d[r.skill2] = 0
        # d[r.skill2] += r.skill2_years * 12 + r.skill2_months

        # if r.skill3 not in d:
        #     d[r.skill3] = 0
        # d[r.skill3] += r.skill3_years * 12 + r.skill3_months

        d = add_skills(d, r.skill1, r.skill1_years, r.skill1_months)
        d = add_skills(d, r.skill2, r.skill2_years, r.skill2_months)
        d = add_skills(d, r.skill3, r.skill3_years, r.skill3_months)


    return JsonResponse(d, safe=False)


def add_skills(d, skill, years, months):
    if skill:
        skill = skill.lower()
        if skill not in d:
            d[skill] = 0
        d[skill] += years * 12 + months

    return d


def home(request):
    posts = Post.objects.all()
    context = {'posts': posts  }
    return render(request,'blog/home.html', context)   


def about(request):
    return render(request, 'blog/about.html')
