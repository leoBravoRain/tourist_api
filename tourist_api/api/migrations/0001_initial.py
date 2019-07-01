# Generated by Django 2.2.2 on 2019-06-29 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('latitude', models.DecimalField(decimal_places=15, max_digits=30)),
                ('longitude', models.DecimalField(decimal_places=15, max_digits=30)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Videos_Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=500)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Location')),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Place'),
        ),
    ]
