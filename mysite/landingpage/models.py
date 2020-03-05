from django.db import models

# Create your models here.
class BlogPost(models.Model):
    post_title=models.CharField(max_length=200,default="Blog post",primary_key=True)
    post_desc=models.TextField('Short description',max_length=100)
    post_text=models.TextField()
    post_date=models.DateField('Date published')
    post_img=models.ImageField('post img',null=True)

    def __str__(self) :
        return self.post_title
