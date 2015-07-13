from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=128,
                             help_text="The title of this blog post, keep it relevant")
    body = models.TextField(help_text="The body of the post, go crazy")
    tags = models.CharField(max_length=128,
                     			help_text="Any tags for this post")