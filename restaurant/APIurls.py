from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router=DefaultRouter()
router.register(r'tables', views.BookingViewSet)
#api
urlpatterns=[
    
    path('menu', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),

    #booking
    path('booking/', include(router.urls)),

    #auth-token
    path('api-token-auth/', obtain_auth_token),
]