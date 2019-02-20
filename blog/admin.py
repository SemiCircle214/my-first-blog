from django.contrib import admin
from .models import Post,Good, OrderPerson,OrderDash

#admin 페이지에서 컬럼 추가 https://wayhome25.github.io/django/2017/03/22/django-ep8-django-admin/
class GoodAdmin(admin.ModelAdmin):
    list_display = ['id','good_name', 'ea' ]
    #장고 p71

class OrderPersonAdmin(admin.ModelAdmin):
    list_display = ['good_name','order_name','order_confirm',
                    'order_ea','order_phone',
                    'order_date',
                    'order_addr1','order_addr2',
                    'order_email']
    search_fields = ('good_name','order_name','order_phone',
                    'order_addr1','order_addr2',
                    'order_email','order_ea','order_confirm')

class OrderDashAdmin(admin.ModelAdmin):
    list_display = ['good_name','ea','total_order_ea','inventory']

# admin.site.register(Post)
admin.site.register(Good,GoodAdmin)
admin.site.register(OrderPerson,OrderPersonAdmin)
admin.site.register(OrderDash,OrderDashAdmin)
