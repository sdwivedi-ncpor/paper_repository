# Generated by Django 5.0.2 on 2024-02-28 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0008_alter_paper_doi'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paper',
            options={'ordering': ('-date_created',)},
        ),
    ]
