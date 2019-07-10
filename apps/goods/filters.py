# -*- coding: utf-8 -*-
import django_filters
from django_filters.rest_framework import FilterSet
from django.db.models import Q

from .models import Goods


class GoodsFilter(FilterSet):
    """
    自定义商品过滤
    """
    price_min = django_filters.NumberFilter(field_name='shop_price', help_text="最低价格", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='shop_price', help_text="最高价格", lookup_expr='lte')
    top_category = django_filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(
            Q(category_id=value) |
            Q(category__parent_category_id=value) |
            Q(category__parent_category__parent_category_id=value)
        )

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max', 'is_hot', 'is_new']



