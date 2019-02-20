from django import forms

from .models import Post,OrderPerson

class OrderPersonForm(forms.ModelForm):
    class Meta:
        model = OrderPerson
        fields = ('order_name','order_phone','order_addr1','order_addr2','order_email','order_ea')
"""
good_name = models.ForeignKey(Good, on_delete = models.CASCADE, default=1)
order_phone = models.CharField(max_length=20)
order_addr1 = models.TextField()
order_addr2 = models.TextField()
order_email = models.CharField(max_length=30)
order_ea = models.IntegerField(default=1)
order_confirm = models.BooleanField(default=False)
order_date = models.DateTimeField(
default=timezone.now)"""

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
"""
author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
title = models.CharField(max_length=200)
text = models.TextField()
created_date = models.DateTimeField(
default=timezone.now)
published_date = models.DateTimeField(
blank=True, null=True)
"""