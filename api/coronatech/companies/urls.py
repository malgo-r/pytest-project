from rest_framework import routers

from api.coronatech.companies.views import CompanyViewSet

companies_router = routers.DefaultRouter()
companies_router.register(
    prefix="companies", viewset=CompanyViewSet, basename="companies"
)
