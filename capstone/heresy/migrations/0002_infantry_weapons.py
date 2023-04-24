# Generated by Django 4.1.7 on 2023-04-24 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heresy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Infantry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('movement', models.IntegerField(default=7)),
                ('weapon_skill', models.IntegerField(default=4)),
                ('ballistic_skill', models.IntegerField(default=4)),
                ('strength', models.IntegerField(default=4)),
                ('toughness', models.IntegerField(default=4)),
                ('wounds', models.IntegerField(default=1)),
                ('initiative', models.IntegerField(default=4)),
                ('attacks', models.IntegerField(default=1)),
                ('leadership', models.IntegerField(default=7)),
                ('armour_save', models.IntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='Weapons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('distance', models.IntegerField(default=24)),
                ('strength', models.IntegerField(default=4)),
                ('armour_pen', models.IntegerField(default=0)),
            ],
        ),
    ]