from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from cake_app.views import *
from cakesite import settings
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('', CakeListView.as_view(), name='index'),
    path('onlycakes/<int:type>/', OnlyCakeListView.as_view(),
         name='onlycakes'),
    # path('', cache_page(60)(CakeListView.as_view()), name='index'),
    path('<slug:slug>/<int:size>/', CakeDetailsView.as_view(),
         name='show_one_cake'),
    path('addproduct/', AddProductView.as_view(), name='add_product'),
    path('addcake/', AddCakeView.as_view(), name='add_cake'),
    path('addtechcard/', AddTechCardView.as_view(), name='add_techcard'),
    path('allproducts/', ProductsListView.as_view(), name='all_products'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about')
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path('__debug__/',
                        include(debug_toolbar.urls))] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
