from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.good_list, name='good_list'),
    url(r'^good/(?P<pk>\d+)/$', views.good_order, name='good_order'),
    url(r'^good/order_detail/$', views.order_detail, name='order_detail'),
    # url(r'^$', views.post_list, name='post_list'),
    # url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    # url(r'^post/new/$', views.post_new, name='post_new'),
]

"""
^post/(?P<pk>\d+)/$부분이 복잡하게 보이지만, 걱정하지 마세요. 하나씩 차근차근 알아봅시다.

^은 "시작"을 뜻합니다.
post/란 URL이 post 문자를 포함해야 한다는 것을 말합니다. 아직 할 만하죠?
(?P<pk>\d+)는 조금 까다롭습니다. 이 정규표현식은 장고가 pk변수에 모든 값을 넣어 뷰로 전송하겠다는 뜻입니다. \d은 문자를 제외한 숫자 0부터 9 중, 한 가지 숫자만 올 수 있다는 것을 말합니다. +는 하나 또는 그 이상의 숫자가 올 수 있습니다.. 따라서 http://127.0.0.1:8000/post/라고 하면 post/ 다음에 숫자가 없으므로 해당 사항이 아니지만, http://127.0.0.1:8000/post/1234567890/는 완벽하게 매칭됩니다.
/은 다음에 / 가 한 번 더 와야 한다는 의미입니다.
$는 "마지막"을 말합니다. 그 뒤로 더는 문자가 오면 안 됩니다.
브라우저에 http://127.0.0.1:8000/post/5/라고 입력하면, 장고는 post_detail 뷰를 찾아 매개변수 pk가 5인 값을 찾아 뷰로 전달합니다.

pk는 primary key의 약자로, 장고에서 많이 사용되는 변수명입니다. 변수명은 내가 원하는 것으로 변경할 수 있어요. (변수명에 공백문자는 사용할 수 없으며 소문자와 _를 사용할 수 있음을 주의하세요) 예를 들어, (?P<pk>\d+)변수를 post_id으로 바꾸면, 정규표현식도 (?P<post_id>\d+)으로 바뀌게 됩니다.
"""