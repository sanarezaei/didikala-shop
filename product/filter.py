import django_filters
from django_filters import filters

from .models import Brand
from category.models import Category
from .models import Product
from variant.models import Variants


class CustomField(django_filters.fields.ModelMultipleChoiceField):
    def _check_values(self, value):
        """
        Override the base class' _check_values method so our queryset is not
        empty if one of the items in value is invalid.
        """
        null = self.null_label is not None and value and self.null_value in value
        if null:
            value = [v for v in value if v != self.null_value]
        field_name = self.to_field_name or 'pk'
        result = list(self.queryset.filter(**{'{}__in'.format(field_name): value}))
        result += [self.null_value] if null else []
        return result


class CustomModelMultipleChoiceFilter(django_filters.ModelMultipleChoiceFilter):
    field_class = CustomField


class CustomField_cat(django_filters.fields.ModelMultipleChoiceField):
    def _check_values(self, value):
        """
        Override the base class' _check_values method so our queryset is not
        empty if one of the items in value is invalid.
        """
        null = self.null_label is not None and value and self.null_value in value
        if null:
            value = [v for v in value if v != self.null_value]
        field_name = self.to_field_name or 'pk'
        result = list(self.queryset.filter(**{'{}__in'.format(field_name): value}) .get_descendants(include_self=True))
        result += [self.null_value] if null else []
        return result


class CustomModelMultipleChoiceFilter_cat(\
    django_filters.ModelMultipleChoiceFilter):
    field_class = CustomField_cat


class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    category = CustomModelMultipleChoiceFilter_cat(field_name='category__slug',\
    to_field_name='slug', queryset=Category.objects.all(),conjoined=False, )

    variants__color = CustomModelMultipleChoiceFilter(field_name='variation__color', to_field_name='color',\
        queryset=Variants.objects.all(), conjoined=False, )

    variants__size = CustomModelMultipleChoiceFilter(field_name='variation__size', to_field_name='size',\
        queryset=Variants.objects.all(), conjoined=False, )

    brand = CustomModelMultipleChoiceFilter(field_name='brand__slug',\
        to_field_name='slug', queryset=Brand.objects.all(), conjoined=False, )

    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    amount = filters.NumberFilter(field_name='amount', lookup_expr='gte')
    order_by = filters.CharFilter(field_name="order_by", method='filter_order_by')

    def filter_order_by(self, queryset, name, value):
        if value:
            return queryset.order_by(value)

        return queryset

    class Meta:
        model = Product
        fields = ['title', 'brand', 'category', 'variants__color','variants__size', 'min_price', 'max_price', 'amount', 'order_by']


