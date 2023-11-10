from django.urls import path
from .views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', landing, name='landing'),
    path('signup/', signup, name='signup'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('home/', home, name='home'),
    path('reporting/', report, name='report' ),
    path('registerUnits/', registerUnits, name='registerUnits'),
    path('unitsHistory/', unitsHistory, name='unitsHistory'),
    path('examCard/', examCard, name='examCard' ),
    path('statement/', feesStatement, name='statement'),
    path('profile/', user_profile, name='profile'),
    path('edit/', edit_profile, name='edit'),
    path('events/', events, name='events' ),

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)