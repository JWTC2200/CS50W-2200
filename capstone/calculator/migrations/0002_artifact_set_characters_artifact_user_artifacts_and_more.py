# Generated by Django 4.1.7 on 2023-04-23 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artifact_Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_name', models.CharField(max_length=50)),
                ('bonus_two', models.CharField(max_length=50)),
                ('bonus_value', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('bonus_full', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Characters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('slot', models.CharField(max_length=10)),
                ('base_stat', models.CharField(max_length=50)),
                ('base_value', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('attack', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('attackper', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('defence', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('defenceper', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('health', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('healthper', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('elemental_mastery', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('crit_rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('crit_damage', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('healing_bonus', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('energy_recharge', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('bonus_anemo', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('bonus_cryo', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('bonus_dendro', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('bonus_electro', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('bonus_geo', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('bonus_hydro', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('bonus_physical', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('bonus_pyro', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.artifact_set')),
            ],
            options={
                'ordering': ['-datetime'],
            },
        ),
        migrations.AddField(
            model_name='user',
            name='artifacts',
            field=models.ManyToManyField(blank=True, to='calculator.artifact'),
        ),
        migrations.AddField(
            model_name='user',
            name='characters',
            field=models.ManyToManyField(blank=True, to='calculator.characters'),
        ),
    ]