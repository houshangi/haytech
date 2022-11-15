from django.urls import path
from .views import CategoryAPIView, SignUpSalesmanAPIView, ProductAPIView, CategoryDetailAPIView, WareHouseAPIView, \
    ProductDetailAPIView, WareHouseDetailAPIView, OrderProductAPIView, CustomerOrderReportView, AdminOrderReportView, \
    AdminReportTotalView, CustomerReportTotalView, OrderDetailView
from .views.signup_view import SignUpCustomerAPIView

urlpatterns = [
    path('category',
         CategoryAPIView.as_view(),
         name='category_view'),
    path('product',
         ProductAPIView.as_view(),
         name="product_view"),
    path('product/<int:pk>',
         ProductDetailAPIView.as_view(),
         name="detail_product_view"),
    path('warehouse',
         WareHouseAPIView.as_view(),
         name="warehouse_view"),
    path('warehouse/<int:pk>',
         WareHouseDetailAPIView.as_view(),
         name="detail_warehouse_view"),
    path('category/<int:pk>',
         CategoryDetailAPIView.as_view(),
         name="detail_category_view"),
    path('signup/salesman',
         SignUpSalesmanAPIView.as_view(),
         name='signup_salesman'),
    path('signup/customer',
         SignUpCustomerAPIView.as_view(),
         name='signup_customer'),
    path('order',
         OrderProductAPIView.as_view(),
         name='customer_order'),
    path('customer-report',
         CustomerOrderReportView.as_view(),
         name='customer_report'),
    path('admin-report',
         AdminOrderReportView.as_view(),
         name='admin_report'),
    path('admin-report-total',
         AdminReportTotalView.as_view(),
         name='admin_report_total'),
    path('customer-report-total',
         CustomerReportTotalView.as_view(),
         name ='customer_report_total'
         ),
    path('order/<int:pk>',
         OrderDetailView.as_view(),
         name ='customer_report_total'
         ),
]
