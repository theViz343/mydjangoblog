from django.db import models
import datetime

# Create your models here.
GENERAL = "General"
POLITICS = "Politics"
ENTERTAINMENT = "Entertainment"
TECHNOLOGY = "Technology"
BUSINESS = "Business"
color={
    GENERAL: 'gray',
    POLITICS: 'orange',
    ENTERTAINMENT: 'tomato',
    TECHNOLOGY: 'dodgerblue',
    BUSINESS: "mediumseagreen",
       }
tag_choices = (
    (GENERAL, "General"),
    (POLITICS, "Politics"),
    (ENTERTAINMENT, "Entertainment"),
    (TECHNOLOGY, "Technology"),
    (BUSINESS, "Business"),
)

class BlogPost( models.Model ) :
    post_title = models.CharField( max_length=200, default="Blog post", primary_key=True )
    post_desc = models.TextField( 'Short description', max_length=100 )
    post_text = models.TextField()
    post_date = models.DateField( 'Date published' )
    post_img = models.ImageField(  null=True )
    post_tag = models.CharField( max_length=20, choices=tag_choices, default=GENERAL )
    featured = models.BooleanField(default=False)

    def __str__(self) :
        return self.post_title

    def get_tag_color(self):
        return color[self.post_tag]

    def arrange_row_wise(cards_per_row) :
        latest_blogs = BlogPost.objects.order_by( '-post_date' )[:10]
        row_wise_blogs = []
        for i in range( 0, len( latest_blogs ), cards_per_row ) :
            if len( latest_blogs ) - i >= cards_per_row :
                row_wise_blogs.append( latest_blogs[i :i + cards_per_row] )
            else :
                row_wise_blogs.append( latest_blogs[i : len( latest_blogs )] )
        return row_wise_blogs

    def get_text_timestamp(self) :
        timestamp = self.post_date.strftime( "%d %b, %Y" )
        text_timestamp = "Posted on " + timestamp
        return text_timestamp

    def get_from_year(year):
        blogs_in_year=BlogPost.objects.filter(date__year=year)
