from django.urls import path
from . import views
from .tasks import payment_completed

app_name = 'orders'

urlpatterns =[

    path('', views.getOrders, name='orders'),
    path('add/', views.addOrderItems, name='orders-add'),
    path('myorders/', views.getMyOrders, name='myorders'),
    path('csv/', views.export_to_csv, name='myorders'),
    path('<int:order_id>/pdf/', views.render_pdf_view, name='admin_order_pdf'),
    path('<int:order_id>/mail/', payment_completed , name='admin_order_pdf'),
    #path('<int:order_id>/pdf/',views.admin_order_pdf, name='admin_order_pdf'),
    path('<str:pk>/deliver/', views.updateOrderToDelivered, name='order-delivered'),

    path('<str:pk>/', views.getOrderById, name='user-order'),
    path('<str:pk>/pay/', views.updateOrderToPaid, name='pay'),
]