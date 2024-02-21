# Generated by Django 5.0.2 on 2024-02-21 08:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0005_remove_author_paper_paper_authors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='authors',
        ),
        migrations.AddField(
            model_name='author',
            name='paper',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='papers.paper'),
            preserve_default=False,
        ),
    ]
