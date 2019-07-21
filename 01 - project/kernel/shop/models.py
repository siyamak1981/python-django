import uuid
import secrets
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from painless.models import choices as options
from painless.models.mixins import OrganizedMixin
from painless.models.mixins import TimeStampedMixin
from ckeditor_uploader.fields import RichTextUploadingField
# from django.core.urlresolvers import reverse
from django.urls import reverse

status = options.PostStatus(is_charfield = False)
size = options.SizeLevel(is_charfield = False)
class Category(OrganizedMixin):
    discount = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        ordering = ['-created']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

    def get_absolute_url (self):
        return reverse('shop:product_list_by_category', args=[self.slug])

COLOR_CHOICES = (
        ('RED', 'red'),
        ('WHITE', 'white'),
        ('BLUE', 'blue'),
    )

class Product(TimeStampedMixin):
  
    # sku = models.CharField(primary_key = True, default = secrets.token_urlsafe(16), max_length = 32, editable = False )
    name = models.CharField(max_length = 128, unique_for_month='published_at', help_text = 'must be unique')
    slug = models.CharField(max_length = 128, unique_for_month='published_at')
    banner = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    banner1 = models.ImageField(upload_to='slider1/%Y/%m/%d', blank=True)
    banner2 = models.ImageField(upload_to='slider2/%Y/%m/%d', blank=True)
    content = RichTextUploadingField()
    summary = models.CharField(max_length = 128)
    price = models.DecimalField(default='0.0', max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    status = models.PositiveSmallIntegerField(choices = status.get_status(), default = status.DRAFT)
    discount = models.DecimalField(decimal_places=2, max_digits=10)
    size = models.IntegerField( choices=size.get_size(), default = size.SMALL)
    color = models.CharField(max_length=5, choices=COLOR_CHOICES, default='RED')

    published_at = models.DateTimeField(default=timezone.now())
    category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE)
    
    
    def get_all_discounts(self):
        all_fields = self._meta.get_fields()
        discounts = []
        for field in all_fields:
            if field.get_internal_type() == 'ForeignKey':
                field_ref = getattr(self, field.name)
                if hasattr(field_ref, 'discount'):
                    discounts.append(field_ref.discount)

        return discounts

    def get_final_discount(self):
        return max(self.get_all_discounts())



    class Meta:
        ordering = ['-published_at', 'name']
        verbose_name = 'product'
        verbose_name_plural = 'products'
        get_latest_by = ['-published_at']
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url (self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


class ProductType(models.Model):
    uid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False )
    name = models.CharField(max_length = 128)
    description = models.TextField()
    product=models.ForeignKey(Product,  on_delete=models.CASCADE , related_name='+') 
    
    
    class Meta:
        verbose_name = 'product-type'
        verbose_name_plural = 'product-types'
        

    def __str__(self):
        return self.name

class ProductTypeAttr(models.Model):
    uid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    fk_product_type = models.ForeignKey("ProductType",related_name='+', on_delete = models.CASCADE)
    fk_product_attr = models.ForeignKey("Attributes", related_name='+', on_delete = models.CASCADE)

class Attributes(models.Model):
    uid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length = 128)
    description = models.TextField()
    productattrvalue = models.ManyToManyField(Product, related_name = 'attrvalue')
    
class AttrValues(models.Model):
    uid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    fk_attr = models.ForeignKey("Attributes",related_name='+', on_delete = models.CASCADE)
    name = models.CharField(max_length = 128)
    description = models.TextField()


