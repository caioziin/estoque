# Generated by Django 5.0.6 on 2024-05-27 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_remove_produto_cliente_remove_produto_vendedor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='produtos'),
        ),
    ]
