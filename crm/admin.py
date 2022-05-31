from django.contrib import admin
from .models import Order, StatusCrm, ComentCrm

#удобное добавление комментариев
class Coment(admin.StackedInline):
    model = ComentCrm
    fields = ('coment_dt', 'coment_text')
    readonly_fields = ('coment_dt', )
    extra = 1




class OrderAdm(admin.ModelAdmin):
    # Поля выводимые в CRM в заказах
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt')
    # Активные поля
    list_display_links = ('id', 'order_name')
    # Поля для поика
    search_fields = ('id', 'order_name', 'order_phone', 'order_dt')
    # фильтрация в правом верхнем углу
    list_filter = ('order_status',)
    # Изменяемые полтя
    list_editable = ('order_status', 'order_phone')
    # количетсво строк заказов на странице
    list_per_page = 10
    list_max_show_all = 100
    # очередность полей страницы CRM, в случае ошибки readonly
    fields = ('id', 'order_status', 'order_dt', 'order_name', 'order_phone')
    readonly_fields = ('id', 'order_dt')
    inlines = [Coment, ]



# Register your models here.
admin.site.register(Order, OrderAdm)
admin.site.register(StatusCrm)
admin.site.register(ComentCrm)
