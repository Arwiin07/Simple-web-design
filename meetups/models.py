from django.db import models
class Locations(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}{self.address}'

class participant(models.Model):
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Meetup(models.Model):
    title=models.CharField(max_length=200)
    organizer_email=models.EmailField()
    date=models.DateField()
    slug=models.SlugField(unique=True)
    description=models.TextField()
    image=models.ImageField(upload_to="images")
    location=models.ForeignKey(Locations,on_delete=models.CASCADE)
    participant=models.ManyToManyField(participant,blank=True,null=True)

    def __str__(self):
        return f'{self.title} -{self.slug }'
# Create your models here.
