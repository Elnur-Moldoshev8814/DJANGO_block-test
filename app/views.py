from django.shortcuts import HttpResponse

from .models import Author, Article

def author_list(request):
    authors = Author.objects.all()
    res = ''
    for author in authors:
        res += f"{author.login} <br>"
    return HttpResponse(res)

def article_list(request):
    article_ = Article.objects.all()
    res = ''
    for art_ in article_:
        res += f"{art_.title} <br>"
    return HttpResponse(res)

def author_detail(request, login):
    author = Author.objects.get(login=login)  # SELECT * FROM Author where login = '1ypen'
    return HttpResponse(f"{author.first_name} <br> {author.last_name} <br> {author.bio}")

def article_detail(request, title):
    article_ = Article.objects.get(title=title)
    return HttpResponse(f"<p><b>{article_.title}</b></br>{article_.body}</br>date:{article_.created_date}<br>author:{article_.author}</p>")