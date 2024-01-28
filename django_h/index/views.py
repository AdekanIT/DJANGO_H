from django.shortcuts import render, redirect
from .forms import SearchForm, CommentsForm, TitleForm, SignUpForm
from .models import Category, Title, Comments
from django.contrib.auth import login


# Create your views here.
def home(request):
    search_bar = SearchForm()
    states_all = Title.objects.all()
    category_all = Category.objects.all()
    context = {'form': search_bar,
               'states': states_all,
               'category': category_all}
    return render(request, 'home.html', context)


def register(request):
    error = ''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            error = 'Invalid type'

    form = SignUpForm()
    context = {'form': form,
               'error': error}
    return render(request, 'registration/register.html', context)


def regist_states(request):
    error = ''
    if request.method == 'POST':
        form = TitleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)
            error = 'Invalid text'
    form = TitleForm()
    context = {'form': form,
               'error': error}
    return render(request, 'regist_state.html', context)


def get_all_category(request, pk):
    category = Category.objects.get(id=pk)
    states = Title.objects.filter(category_name=category)
    context = {'states': states}
    return render(request, 'category.html', context)


def get_all_states(request, pk):
    states = Title.objects.get(id=pk)
    comment = Comments.objects.all()
    context = {'states': states,
               'comment': comment}
    return render(request, 'states.html', context)


def search_state(request):
    if request.method == 'POST':
        get_states = request.POST.get('search_state')

        try:
            except_states = Title.objects.get(title__icontains=get_states)

            return redirect(f'states/{except_states.id}')
        except:
            return redirect('/states-not-found')


def state_not_found(request):
    return render(request, 'not_found.html')


def add_comment(request):
    error = ''
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Invalid comment'
    form = CommentsForm()
    context = {'form': form,
               'error': error}
    return render(request, 'add_comment.html', context)

# def get_user_comment(request):
#     comment = Comments.objetcs.all()
#     context = {'comment': comment}
#     return render(request, 'comments.html', context)


# def dell_comment(request, pk):
#     dell_comments = Comments.objects.get(id=pk)
#     Comments.objects.filter(user_id=request.user.id,
#                             user_comment=dell_comments).delete()
#     return redirect('/')

































