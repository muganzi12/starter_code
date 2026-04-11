import uuid 
#used to generate unique IDs (more secure than incremental IDs)
from django.db import models
#Django’s ORM for defining database tables
from django.contrib.auth.models import AbstractUser
#base class for customizing the default user model.

#You are extending Django’s built-in user.
class User(AbstractUser):
    pass #do nothing for now.

class  Product(models.Model):
    name= models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveBigIntegerField()
    image= models.ImageField(upload_to='products/',blank=True,null=True)

    @property
    def in_stock(self):
        return self.stock > 0
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
        class StatusChoices(models.TextChoices):
            PENDING= 'Pending'
            CONFIRMED= 'Confrimed'
            CANCELLED= 'Cancelled'

        id = models.UUIDField(primary_key =True, default=uuid.uuid4)
        user= models.ForeignKey(User, on_delete=models.CASCADE)
        created_at = models.DateTimeField(auto_now=True)
        status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.PENDING)

        products = models.ManyToManyField(Product, through="OrderItem")

        def __str__(self):
            return f"Order {self.id} by {self.user.username}"

class OrderItem(models.Model):
     order= models.ForeignKey(Order, on_delete=models.CASCADE)
     product= models.ForeignKey(Product,on_delete=models.CASCADE)
     quantity= models.PositiveIntegerField()

     @property
     def item_subtotal(self):
          return self.product.price * self.quantity
     
     def __str__(self):
          return f"{self.quantity} x {self.product.name} in Order {self.order.id}"
