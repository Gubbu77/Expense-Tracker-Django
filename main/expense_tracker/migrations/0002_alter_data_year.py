# Generated by Django 4.1.4 on 2022-12-20 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='year',
            field=models.CharField(choices=[('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027'), ('2028', '2028'), ('2029', '2029')], max_length=4),
        ),
    ]
