# Generated by Django 4.0.2 on 2022-02-17 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.IntegerField(blank=True, null=True)),
                ('holder_name', models.CharField(blank=True, max_length=200, null=True)),
                ('balance_amount', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('transaction_detail', models.CharField(blank=True, max_length=100, null=True)),
                ('value_date', models.DateField(blank=True, null=True)),
                ('currency', models.CharField(choices=[('INR', 'INR'), ('USD', 'USD')], default='INR', max_length=50)),
                ('transaction_type', models.CharField(choices=[('CR', 'CREDIT'), ('DR', 'DEBIT')], default='DR', max_length=50)),
                ('transaction_amount', models.FloatField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_app.account')),
            ],
        ),
    ]
