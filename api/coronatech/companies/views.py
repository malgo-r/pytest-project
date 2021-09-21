from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from django.core.mail import send_mail

from api.coronatech.companies.models import Company
from api.coronatech.companies.serializers import CompanySerializer


# Create your views here.
class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination


@api_view(http_method_names=['POST'])
def send_company_email(request:Request) -> Response:
    """
    Send enami with request payload
    sender: malgor.test@gmail.com
    receiver: malgor.test@gmail.com
    """
    send_mail(subject=request.data.get("subject"), message=request.data.get("message"), from_email="malgor.test@gmail.com", recipient_list=["malgor.test@gmail.com"])
    return Response({"status": "success", "info": "email sent successfully"}, status=200)