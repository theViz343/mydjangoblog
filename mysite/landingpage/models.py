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
    def arrange_row_wise(cards_per_row):
        latest_blogs = BlogPost.objects.order_by( '-post_date' )[:10]
        row_wise_blogs = []
        for i in range( 0, len( latest_blogs ), cards_per_row ) :
            if len(latest_blogs)-i>=cards_per_row:
                row_wise_blogs.append(latest_blogs[i :i + cards_per_row])
            else:
                row_wise_blogs.append( latest_blogs[i : len(latest_blogs)] )
        return row_wise_blogs

