from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from products.models import Product

can_read_edit_product = Permission.objects.create(
    codename='can_read_edit_product',
    name='Can Read and Edit Product',
)

can_read_product = Permission.objects.create(
    codename='can_read_product',
    name='Can Read Product',
)

content_type = ContentType.objects.get_for_model(Product)
content_type.permissions.add(can_read_edit_product, can_read_product)

