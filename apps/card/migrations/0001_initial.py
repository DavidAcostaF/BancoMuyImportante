# Generated by Django 5.0.6 on 2024-07-10 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, unique=True)),
                ('opening_date', models.DateField()),
                ('status', models.CharField(max_length=20)),
                ('cardholder_name', models.CharField(max_length=100)),
                ('expiration_date', models.DateField()),
                ('cvv', models.CharField(max_length=4)),
                ('card_type', models.CharField(choices=[('credit', 'Credit'), ('debit', 'Debit')], max_length=10)),
            ],
        ),
    ]