# Generated by Django 3.2.8 on 2021-11-30 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidade',
            name='habitantes',
            field=models.IntegerField(blank=True, default=0, help_text='Se você não sabe, informe zero.', null=True),
        ),
        migrations.AlterField(
            model_name='cidade',
            name='nome',
            field=models.CharField(max_length=50, verbose_name='Nome da cidade'),
        ),
        migrations.AlterField(
            model_name='estado',
            name='sigla',
            field=models.CharField(max_length=2, unique=True),
        ),
    ]
