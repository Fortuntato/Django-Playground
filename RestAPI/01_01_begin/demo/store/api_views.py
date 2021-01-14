from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

from store.serializers import ProductSerializer
from store.models import Product

class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,) #WHY THE BLOODY COMMA?
    filter_fields = ('id',) #DANK FARRIK WHY THE BLOODY COMMA AT THE END??

    def get_queryset(self):
        on_sale = self.request.query_params.get('on_sale',None)
        if on_sale is None:
            return super().get_queryset()
        queryset = Product.objects.all()
        if on_sale.upper() == 'TRUE':
            from django.utils import timezone
            now = timezone.now()
            return queryset.filter(
                sale_start__lte=now,
                sale_end__gte=now,
            )
        return queryset