# Generated by Django 5.2 on 2025-05-12 10:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investment_type', models.CharField(choices=[('SIP', 'SIP'), ('Mutual Funds', 'Mutual Funds'), ('Stocks', 'Stocks'), ('Fixed Deposit', 'Fixed Deposit'), ('Gold', 'Gold'), ('Crypto', 'Crypto')], max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('investment_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
