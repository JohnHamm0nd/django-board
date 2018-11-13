from django.shortcuts import render, redirect, resolve_url
from .forms import PostForm
from .models import Post

# Create your views here.
def list(request):
    posts = Post.objects.all()
    return render(request, 'post/list.html', {'posts':posts})
    
def create(request):
    if request.method == 'POST':
        # 저장로직
        # title, content 에 적었던 내용을 받아옮
        form = PostForm(request.POST)
        
        # 입력 규칙 설정(서버)
        # html 상의 규칙설정은 사용자가 html 코드를 수정하면 검증할 수 없다
        if form.is_valid():
            title = form.cleaned_data['title']
            # title = form.cleand_data.get('title')
            content = form.cleaned_data['content']
            Post.objects.create(title=title, content=content)    
            return redirect(resolve_url('post:list'))
            
    else:
        # 사용자에게 입력할 수 있는 폼 리턴
        form = PostForm()
    return render(request, 'post/create.html', {'form': form})

def detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post/detail.html', {'post':post})