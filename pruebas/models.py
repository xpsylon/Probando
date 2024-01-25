from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# MANY TO MANY RELATIONSHIPS------------------------
class Person(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self) -> str:
        return self.name
    
class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')
    
    def __str__(self) -> str:
        return self.name
    
class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    instrument = models.CharField(max_length=64)
    
    def __str__(self) -> str:
        return f' {self.person.name} joined {self.group.name} on {self.date_joined} plays {self.instrument}'
# --------------------------------------------------

# ONE TO ONE RELATIONSHIP---------------------------
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    
    def __str__(self) -> str:
        return f'{self.name} the place'
    

class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.place.name} the restaurant'
    
class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} the waiter at {self.restaurant}'
# --------------------------------------------------

# MANY TO ONE (FOREIGN KEY) RELATIONSHIP------------
class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.headline
    
    class Meta:
        ordering = ['headline']
    
# MANY TO MANY RELATIOHSHIP-------------------------
class Publication(models.Model): # REVERSE SIDE (use articulo_set)
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title
    
class Articulo(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication) # FORWARD SIDE (use this field name)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline

# FROM MAKING QUERIES:------------------------------
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name
    

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline

# ANOTHER MANY TO MANY RELATION:
class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    buyers = models.ManyToManyField(Buyer, through='BuyerProduct')

    def __str__(self):
        return self.name
    

class BuyerProduct(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    purchase_date = models.DateField()

class Review(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    review_date = models.DateField()

    class Meta:
        unique_together = ('buyer', 'product')
    """ You’re correct. The current Review model doesn’t prevent a user from reviewing a product they haven’t purchased. To enforce this rule, you could add a check in your view or model to ensure that a UserProduct instance exists for the user and product before a review is saved.
    Here’s an example of how you could modify the save method of the Review model to include this check: """
    
    def clean (self):
        buyer_product_exists = Buyer.objects.filter(buyer=self.buyer, product=self.product).exists
        if not buyer_product_exists:
            raise ValidationError('Buyer didnt buy that product!')
    