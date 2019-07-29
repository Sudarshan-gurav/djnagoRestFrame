from multiselectfield import MultiSelectField
from django.db import migrations, models



# Create your models here.
class AllFeilds_1(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=20)
    email = models.EmailField()
    web = models.URLField('Web Address')
    # dop = models.DateField(default=True)
    city = (
        ('pune', 'Pune'),
        ('mumbai', 'Mumbai'),
        ('nashik', 'Nashik'),
    )
    city = models.CharField(max_length=50, choices=city)

    languages = ((1, 'C'),
               (2, 'C++'),
               (3, 'Python'),
               (4, 'Django'),
               (5, 'JavaScript'),)
    languages = MultiSelectField(choices=languages)

    upload = models.FileField(upload_to='uploads/',default='')

    description = models.TextField(blank=True)

    gender= [
    ('male', 'Male'),
    ('female', 'Female'),
    ]
    gender= models.CharField(choices=gender,max_length=20)

    def __str__(self):
        return self.name


    

# class Employee(models.Model):
#     name = models.CharField(max_length=50)
#     degnation = models.CharField(max_length=20)
#     mobile = models.IntegerField()
#     email = models.EmailField()
#     dop = models.DateField(default=True)
#     city = (('pune', 'Pune'),('mumbai', 'Mumbai'),('nashik', 'Nashik'),)
#     city = models.CharField(max_length=50, choices=city)
#     languages = ((1, 'C'),(2, 'C++'),(3, 'Python'),(4, 'Django'),(5, 'JavaScript'))
#     languages = MultiSelectField(choices=languages)
#     upload = models.FileField(upload_to='uploads/')

#     def __str__(self):
#         return self.name


