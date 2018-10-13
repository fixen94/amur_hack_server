# Generated by Django 2.1.2 on 2018-10-13 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypesUrn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Тип мусора')),
            ],
            options={
                'verbose_name': 'Тип мусорки',
                'verbose_name_plural': 'Типы мусорок',
            },
        ),
        migrations.AddField(
            model_name='urn',
            name='types',
            field=models.ForeignKey(default=1, on_delete='CASCADE', related_name='type_urns', to='main.TypesUrn', verbose_name='Тип'),
            preserve_default=False,
        ),
    ]