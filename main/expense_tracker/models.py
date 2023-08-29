from django.db import models
from datetime import date

# Create your models here.
class Data(models.Model):
    category_items = (
        ("Meal","Meal"),
        ("Vehicle", "Vehicle"),
        ("Shopping", "Shopping"),
        ("Grocery", "Grocery"),
        ("Utility", "Utility"),
        ("Online Shopping", "Online Shopping"),
        ("Gain", "Gain"),
        ("Others", "Others"),

    )
    year_list = (
        ("2020", "2020"),
         ("2021", "2021"),
          ("2022", "2022"),
           ("2023", "2023"),
            ("2024", "2024"),
             ("2025", "2025"),
              ("2026", "2026"),
               ("2027", "2027"),
                ("2028", "2028"),
                 ("2029", "2029"),
    )

    month_list = (
        ('Jan', 'Jan'),
        ('Feb', 'Feb'),
        ('Mar', 'Mar'),
        ('Apr', 'Apr'),
        ('May', 'May'),
        ('Jun', 'Jun'),
        ('Jul', 'Jul'),
        ('Aug', 'Aug'),
        ('Sep', 'Sep'),
        ('Oct', 'Oct'),
        ('Nov', 'Nov'),
        ('Dec', 'Dec'),
    )
    name = models.CharField(max_length=100)
    category = models.CharField(max_length= 100, choices= category_items)
    amount = models.IntegerField(null= True)
    note = models.CharField(max_length= 300)
    year = models.CharField(max_length=4, choices= year_list)
    month = models.CharField(max_length=10, choices= month_list)
    dateandtime = models.DateField()
    time =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name