from django.contrib import admin
from .models import *
# Register your models here.
import csv
import datetime
from django.http import HttpResponse
from django.urls import reverse
from django.utils.safestring import mark_safe


def order_pdf(obj):
    url = reverse('orders:admin_order_pdf', args=[obj._id])
    return mark_safe(f'<a href="{url}">PDF</a>')
order_pdf.short_description = 'Invoice'


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    content_disposition = 'attachment; filename={opts.name}.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = content_disposition
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not \
    field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
        return response


export_to_csv.short_description = 'Export to CSV'



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['_id', 'user', 'shippingPrice', 'totalPrice', 'isDelivered', 'taxPrice', 'isPaid', 'createdAt', 'deliveredAt', order_pdf]   #, order_detail, order_pdf]
    list_filter = ['isPaid', 'createdAt', 'deliveredAt']
    #inlines = [OrderItemInline]
    actions = [export_to_csv]










admin.site.register(OrderItem)
admin.site.register(ShippingAddress)