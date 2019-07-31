from django.shortcuts import render, redirect,get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.contrib.auth.models import User

def visitor(request):
    posts = Post.objects.all()
    return render(request, 'world/visitor.html', {"posts":posts})
    
def gallery(request):
    return render(request, 'world/gallery.html')

def create(request):
    return render(request, 'world/create.html')
    
def new(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False) # form을 당장 저장하지 않음. 데이터 저장 전 뭔가 하고 싶을 때 사용.
            form.user = request.user
            form.save()
            return redirect('world:visitor')
    return render(request, 'world/new.html', {'form': form})
    
    
    

    
def show(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'world/show.html', {"post": post})
    
def update(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post.title = title
        post.content = content
        post.save()
        return redirect('world:show', post.id)
    return render(request, 'world/update.html', {"post": post})
    
def delete(request, id):
     post = get_object_or_404(Post, pk=id)
     post.delete()
     return redirect('world:visitor')
    
# Comment

def create_comment(request, id):
    form = CommentForm()
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('world:show', post.id)
    return render(request, 'world/new_comment.html', {'form': form})
    

def new_comment(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'world/new_comment.html', {'post': post})
    
def delete_comment(request, id):
    comment = get_object_or_404(Comment, pk=id)
    post = comment.post
    comment.delete()
    return redirect('world:show', post.id)
    
# Like

def favourite(request):
    return render(request, 'world/favourite.html')
    


def like(request, id):
    user = request.user #로그인한 유저를 가져옴
    post = get_object_or_404(Post, pk=id)  #넘겨받은 id값을 다시Post에 넘겨줘서 id를 찾도록
    if request.method == 'POST':
        if post.likes.filter(id = user.id).exists(): #해당 post에 로그인한 유저가 like 컬럼에 존재하면
            post.likes.remove(user) #like 컬럼에서 해당 유저를 지운다. 즉 이미 좋아요를 눌렀는지 안눌렀는지 찾고 눌렀다면 지워줌(좋아요 취소)
        else:
            post.likes.add(user) #그 외의 경우 추가한다.
    return redirect('world:show', post.id) 
    