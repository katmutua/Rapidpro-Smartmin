# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'The title of this blog post, keep it relevant', max_length=128)),
                ('body', models.TextField(help_text=b'The body of the post, go crazy')),
                ('tags', models.CharField(help_text=b'Any tags for this post', max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
