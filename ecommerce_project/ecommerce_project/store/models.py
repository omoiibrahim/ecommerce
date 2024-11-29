from django.db import models

class Customer(models.Model):
    # Customer information
    name = models.CharField(max_length=100, verbose_name="Customer Name")
    email = models.EmailField(unique=True, verbose_name="Email Address")

    def __str__(self):
        return self.name


class Order(models.Model):
    # A customer can place multiple orders, each order relates to one customer
    customer = models.ForeignKey(
        Customer,  # This links the order to a customer (One-to-Many relationship)
        on_delete=models.CASCADE,  # Deletes the order if the customer is deleted
        related_name='orders',  # Allows reverse lookup: customer.orders.all()
        verbose_name="Customer"
    )
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="Order Date")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total Amount")

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"
