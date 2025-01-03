from django.urls import path, include
from .views import AllView, SearchByTitle

urlpatterns = [
    path('all/', AllView.as_view()),
    path('', SearchByTitle.as_view()), 
    path('accounts/', include('allauth.urls'))
]
