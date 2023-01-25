from django.urls import include, path

from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.post_board, name='boardpage'),  # 포스트 목록
    path('<int:post_id>/', views.post_detail, name='postdetail'),
    path('<int:post_id>/delete', views.post_delete, name='postdelete'),
    path('<int:post_id>/edit', views.post_edit, name='postedit'),
    path('new_post/', views.new_post, name='newpost'),

]

# 순서
# 1. 특정 url로 요청
# 2. urls.py에서 맞는 view 호출
# 3. views.py에서 맞는 view(함수) 기능 실행후 template 반환
# 모든 view 가 각각 다른 template(html 파일)을 반환할 필요는 없음. 리다이렉트, 분기를 통한 동일 템플릿 사용 등 방법 사용
