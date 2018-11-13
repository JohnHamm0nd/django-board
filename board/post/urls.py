from django.urls import path
from . import views



# url 요청 작업시 실수를 줄이기 위해 사용 - 변수를 만들어 변수명을 주소대신 사용
app_name = 'post'

urlpatterns = [
    path('', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('<int:id>/detail/', views.detail, name='detail')
    ]