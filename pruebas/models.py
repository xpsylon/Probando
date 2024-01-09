from django.db import models

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
    
    
class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title
    
class Articulo(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline