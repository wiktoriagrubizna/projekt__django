# Generated by Django 4.1.4 on 2022-12-27 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=45)),
                ('nazwisko', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=45)),
                ('nazwisko', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Ocena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wartosc', models.CharField(max_length=45)),
                ('user', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=45)),
                ('opis', models.TextField()),
                ('srednia_ocena', models.CharField(max_length=45)),
                ('created', models.CharField(max_length=45)),
                ('uploated', models.CharField(max_length=45)),
                ('ilosc_ocen', models.CharField(max_length=45)),
                ('aktorzy', models.ManyToManyField(to='recenzje.director')),
                ('rezyserzy', models.ManyToManyField(to='recenzje.actor')),
            ],
        ),
    ]
