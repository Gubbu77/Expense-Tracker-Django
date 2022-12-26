# Generated by Django 4.1.4 on 2022-12-20 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Meal', 'Meal'), ('Vehicle', 'Vehicle'), ('Shopping', 'Shopping'), ('Grocery', 'Grocery'), ('Utility', 'Utility'), ('Online Shopping', 'Online Shopping'), ('Gain', 'Gain'), ('Others', 'Others')], max_length=100)),
                ('amount', models.DecimalField(decimal_places=10, max_digits=100)),
                ('note', models.CharField(max_length=300)),
                ('year', models.CharField(choices=[(2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029)], max_length=1)),
                ('month', models.CharField(choices=[('Jan', 'Jan'), ('Feb', 'Feb'), ('Mar', 'Mar'), ('Apr', 'Apr'), ('May', 'May'), ('Jun', 'Jun'), ('Jul', 'Jul'), ('Aug', 'Aug'), ('Sep', 'Sep'), ('Oct', 'Oct'), ('Nov', 'Nov'), ('Dec', 'Dec')], max_length=10)),
                ('dateandtime', models.DateTimeField(auto_now_add=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
