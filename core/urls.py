from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from dj_rest_auth.views import LogoutView
from apps.localidades.views import LocalViewSet, CidadeViewSet, PoloViewSet
from apps.equipamentos.views import EquipamentoViewSet, TipoEquipamentoViewSet, FabricanteEquipamentoViewSet, DashboardStatsView
from apps.movimentacao.views import MovimentacaoViewSet
from .views import home

router = routers.DefaultRouter()
router.register(r'polos', PoloViewSet)
router.register(r'cidades', CidadeViewSet)
router.register(r'locais', LocalViewSet)
router.register(r'tipos', TipoEquipamentoViewSet)
router.register(r'fabricantes', FabricanteEquipamentoViewSet)
router.register(r'equipamentos', EquipamentoViewSet)
router.register(r'movimentacoes', MovimentacaoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/dashboard-stats/', DashboardStatsView.as_view(), name='dashboard-stats'),
    path('api/', include(router.urls)),
    path('api/auth/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/logout/', LogoutView.as_view(), name='rest_logout'),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
     path('api/auth/', include('dj_rest_auth.urls'))
]