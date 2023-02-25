from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import News, Comment


# Create your views here.
def index(request):
    news = News.objects.all()
    context = {
        'newsData': news
    }
    return render(request, 'index.html', context)


def details(request, id):
    if request.method == 'POST':
        body = request.POST.get('body')
        user = request.user
        news = News.objects.get(id=id)
        parent_id = request.POST.get('parent')
        if parent_id:
            parent = Comment.objects.get(id=parent_id)
            Comment.objects.create(body=body, user=user, news=news, parent=parent)
            back = request.META.get('HTTP_REFERER')
            return redirect(back)
        else:
            Comment.objects.create(body=body, user=user, news=news)
            back = request.META.get('HTTP_REFERER')
            return redirect(back)

    else:
        news = News.objects.get(id=id)
    context = {
        'news': news,
    }
    return render(request, 'details.html', context)
