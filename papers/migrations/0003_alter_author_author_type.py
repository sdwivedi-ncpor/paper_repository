# Generated by Django 5.0.2 on 2024-02-20 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0002_author_author_type_alter_paper_doi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_type',
            field=models.CharField(choices=[('FIRST', 'First Author'), ('CO', 'Co-Author')], default='JANUARY', max_length=9),
        ),
    ]
