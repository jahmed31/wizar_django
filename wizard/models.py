from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.name


class SubCategory(BaseModel):
    name = models.CharField(max_length=128, null=False)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=256, null=False)
    sub_category = models.ForeignKey(SubCategory, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class ProductInfo(BaseModel):
    name = models.CharField(max_length=256, null=False)
    units = models.CharField(max_length=64, null=False)
    purchase_order_no = models.CharField(max_length=128, null=True)
    quantity = models.IntegerField(null=False)
    ref_or_sku = models.CharField(max_length=128, null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    sub_category = models.ForeignKey(SubCategory, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Booking(BaseModel):
    inspection = models.BooleanField(default=True)
    ref_no = models.CharField(max_length=128, null=False)
    contact = models.CharField(max_length=128, null=False)
    mobile = models.CharField(max_length=128, null=False)
    landline = models.CharField(max_length=128, null=False)
    email = models.EmailField(max_length=128, null=False)
    inspection_date = models.DateField(null=False)
    shipment_date = models.DateField(null=False)
    allow_date_change = models.BooleanField(default=False)
    product_info = models.ForeignKey(ProductInfo, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.product_info.name
