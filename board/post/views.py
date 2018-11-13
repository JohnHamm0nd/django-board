from django.shortcuts import render, redirect, resolve_url
from .forms import PostForm
from .models import Post

# Create your views here.
def list(request):
    return render(request, 'post/list.html')
    
def create(request):
    if request.method == 'POST':
        # 저장로직
        # title, content 에 적었던 내용을 받아옮
        form = PostForm(request.POST)
        
        # 입력 규칙 설정
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
