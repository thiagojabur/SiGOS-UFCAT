from django.urls import path

from orders import views

app_name = "orders"

# fmt: off
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("api/ordens/", views.WorkOrderListViewJSONResponse.as_view(), name="workorder_list_json"),
    path("ordens/", views.WorkOrderListView.as_view(), name="workorder_list"),
    path("ordens/<int:pk>", views.WorkOrderDetailView.as_view(), name="workorder_detail"),
    path("ordens/<int:pk>/deletar/", views.WorkOrderDeleteViewJSONResponse.as_view(), name="workorder_delete"),
    path("ordens/<int:pk>/editar/", views.WorkOrderUpdateView.as_view(), name="workorder_update"),
    path("ordens/novo/", views.WorkOrderCreateView.as_view(), name="workorder_create"),
    path("api/historico/", views.WorkOrderHistoryListViewJSONResponse.as_view(), name="history_json"),
    path("ordens/historico/", views.WorkOrderHistoryListView.as_view(), name="history"),
]
