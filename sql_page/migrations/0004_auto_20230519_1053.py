# Generated by Django 3.2.19 on 2023-05-19 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sql_page', '0003_auto_20230519_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='champion',
            name='name',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sql_page.user', unique=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='author',
            field=models.TextField(),
        ),
    ]
