from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from users.models import User

# Create your views here.
from .models import Article, Post


def post_board(request):

    post_list = Post.objects.all()
    # 만약 10개정도씩 끊어서 줄거라면?

    return render(request, 'blog/board.html', {'post_list': post_list})


def post_detail(request, post_id):

    chosen_post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'post': chosen_post})


@login_required
def new_post(request):

    if request.method == 'GET':
        return render(request, 'blog/new_post.html')
    elif request.method == 'POST':

        # 사용자가 html에 채워넣은 데이터 -> value 가 list면 문제가 생김(나중에 수정)
        post_data = request.POST
        new_article = Article(title=post_data['title'], text=post_data['text'])

        # user 정보 어떻게 갖고옴?

        _new_post = Post(article=new_article, owner=request.user)

        new_article.save()
        _new_post.save()

        # ALERT NEW POST COMPLETE
        return redirect('blog:boardpage')


@ login_required
def post_delete(request, post_id):

    # DELETE ALERT
    # authentication needed -> 글을 쓴 사용자가 현재 로그인해서 글을 삭제하려는 사람과 같은지 확인
    # 같다면 아래의 코드 실행
    chosen_post = get_object_or_404(Post, pk=post_id)

    if chosen_post.owner == request.user or request.user.is_superuser:
        chosen_post.delete()
        return redirect('blog:boardpage')
    else:
        print("글을 작성한 사용자가 아닙니다!")
        messages.warning(request, "자신이 작성한 글만 삭제할 수 있습니다!")
        return redirect('blog:postdetail', post_id)


@ login_required
def post_edit(request, post_id):

    # EDIT ALERT
    # authenticate needed -> 글을 쓴 사용자가 현재 로그인해서 글을 수정하려는 사람과 같은지 확인
    # 같다면 아래의 코드 실행
    if request.method == 'GET':
        chosen_post = get_object_or_404(Post, pk=post_id)

        print(chosen_post.owner == request.user)

        if chosen_post.owner == request.user or request.user.is_superuser:
            return render(request, 'blog/modify.html', {'post': chosen_post})
        else:
            print("글을 작성한 사용자가 아닙니다!")
            messages.warning(request, "자신이 작성한 글만 수정할 수 있습니다!")
            return redirect("blog:postdetail", post_id)

    if request.method == 'POST':

        edit_data = request.POST
        chosen_post = get_object_or_404(Post, pk=post_id)

        chosen_post.article.title = edit_data['title']
        chosen_post.article.text = edit_data['text']
        chosen_post.article.save()
        chosen_post.save()

        # COMPLETE ALERT

        return render(request, 'blog/detail.html', {'post': chosen_post})
