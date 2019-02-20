from django.shortcuts import render
from django.utils import timezone
from .models import Post,Good,OrderPerson,OrderDash
from django.shortcuts import render, get_object_or_404
from .forms import PostForm,OrderPersonForm
from django.shortcuts import redirect

#상품 관련 view정의
def good_list(request):
    dashs = OrderDash.objects.all()
    return render(request, 'blog/good_list.html', {'dash': dashs})

#상품 구매 페이지 view정의
"""
def good_order(request, pk):
    dashs = get_object_or_404(OrderDash, pk=pk)
    form = OrderPersonForm()
    return render(request, 'blog/good_order.html', {'dash': dashs,'form':form})
"""

def good_order(request, pk):
    if request.method == "POST":
        # print("ccccccccc1")
        form = OrderPersonForm(request.POST)

        if form.is_valid():
            # print("c2")
            #잔고량 체크
            inventory = OrderDash.objects.filter(id=1).values_list('inventory',flat=True).get(pk=1)
            if int(request.POST['order_ea'])>inventory:
                dashs = OrderDash.objects.all()
                return render(request, 'blog/order_detail_fail.html', {'dash': dashs})

            orderperson = form.save(commit=False)
            orderperson.order_date = timezone.now()
            orderperson.order_confirm=False
            orderperson.save()
            dashs = OrderDash.objects.all()

            #성공 경우
            result = OrderPerson.objects.filter(order_date=orderperson.order_date)
            # print(result.values())
            print(result.values())
            print(dashs.values())
            return render(request, 'blog/order_detail.html', {'dash': dashs,'od':result})
        else:
            dashs = OrderDash.objects.all()
            return render(request, 'blog/order_detail_fail.html')
    else:
        dashs = get_object_or_404(OrderDash, pk=pk)
        form = OrderPersonForm()
        return render(request, 'blog/good_order.html', {'dash': dashs, 'form': form})




def order_detail(request):
    if request.method == "POST":
        form = OrderPersonForm(request.POST)
        if form.is_valid():
            orderperson = form.save(commit=False)
            orderperson.order_date = timezone.now()
            orderperson.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    #작성후
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:#작성전
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})