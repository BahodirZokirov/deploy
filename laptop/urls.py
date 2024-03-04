from django.urls import path
from .views import LaptopListView, LaptopDetailView, LaptopView
# from .views import , LaptopView
# from .views import laptop_detail, laptop_info

urlpatterns = [
    # path("adsfasdf", LaptopView.as_view(), name='laptop-view'),
    path("", LaptopView.as_view()),
    path("a", LaptopListView.as_view(), name = "laptop-info"),
    path("<int:pk>/", LaptopDetailView.as_view(), name='laptop-detail-view')
    # path("<int:pk>/", laptop_detail, name='laptop-detail'),
    # path("laptop-info", laptop_info, name='laptop-info')
]