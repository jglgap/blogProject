from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse
# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class Tag(models.Model):
     caption = models.CharField(max_length=20)
     def __str__(self):
         return f'{self.caption}'

class Post(models.Model):
    title = models.CharField(max_length=100)
    exceptText = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts",null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.OneToOneField(Author, null=True, on_delete=models.SET_NULL,related_name='fkbooks')
    tag = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse("blog:blogDetail",args=[self.slug])


    def __str__(self):
        return f'{self.title} {self.exceptText} {self.image} {self.date} {self.slug} {self.content} {self.author} {self.tag} '
    
class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    text = models.TextField(max_length=400)
    email = models.EmailField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")