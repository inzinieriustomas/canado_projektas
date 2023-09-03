from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.CharField(
         max_length=256)
    project_resume = models.CharField(
         max_length=256)

    UTL_CHOICES = [
        ("Audi", "Audi"),
        ("BMW", "BMW"),
        ("Dodge", "Dodge"),
        ("Fiat", "Fiat"),
        ("Ford", "Ford"),
        ("Honda", "Honda"),
        ("Hyundai", "Hyundai"),
        ("Jaguar", "Jaguar"),
        ("Jeep", "Jeep"),
        ("Kia", "Kia"),
        ("Lexus", "Lexus"),
        ("Mazda", "Mazda"),
        ("Mercedes-Benz", "Mercedes-Benz"),
        ("Mitsubishi", "Mitsubishi"),
        ("Nissan", "Nissan"),
        ("Opel", "Opel"),
        ("Peugeot", "Peugeot"),
        ("Porsche", "Porsche"),
        ("Renault", "Renault"),
        ("Seat", "Seat"),
        ("Skoda", "Skoda"),
        ("Subaru", "Subaru"),
        ("Suzuki", "Suzuki"),
        ("Toyota", "Toyota"),
        ("Volkswagen", "Volkswagen"),
        ("Volvo", "Volvo"),
        ("-", "-")
        ]

    UTL_CHOICES2 = [
        ("Red", "Red"),
        ("Blue", "Blue"),
        ("Green", "Green"),
        ("Yellow", "Yellow"),
        ("Black", "Black"),
        ("White", "White"),
        ("Grey", "Grey"),
        ("-", "-")]

    UTL_CHOICES3 = [
        (str(i / 10), str(i / 10)) for i in range(10, 61)]
    UTL_CHOICES4 = [
        (str(i), str(i) + 'kW') for i in range(10, 601, 10)]
    UTL_CHOICES5 = [
        (str(i), str(i)) for i in range(1980, 2024)]

    Gamintojas = models.CharField(
        max_length=20,
        choices=UTL_CHOICES,
        blank=True)

    Marke = models.CharField(
        max_length=10,
        blank=True)

    Variklis = models.CharField(
        max_length=3,
        choices=UTL_CHOICES3,
        blank=True)

    Galia = models.CharField(
        max_length=6,
        choices=UTL_CHOICES4,
        blank=True)

    Spalva = models.CharField(
        max_length=20,
        choices=UTL_CHOICES2,
        blank=True)

    Metai = models.CharField(
        max_length=4,
        choices=UTL_CHOICES5,
        blank=True)


    project_start_date = models.DateField(
        blank=False
    )

    PSTATUS_CHOICES = [
        ('K', "Kuriamas"),
        ('U', "Užbaigtas")]

    project_status = models.CharField(
        max_length= 1,
        choices= PSTATUS_CHOICES,
        blank=False
        )

    c_remarks = models.CharField(max_length=256, verbose_name='Pastabos', default='-')
    # darbas =models.ForeignKey(Darbas, default=None, on_delete=models.CASCADE, related_name='darbas') is darbas appso
    c_created_at = models.DateTimeField(auto_now_add=True)
    c_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.title}, {self.project_resume}, {self.project_start_date}"

class Image(models.Model):
    Car = models.ForeignKey(Car, default=None, on_delete=models.CASCADE, related_name='images')
    Image = models.ImageField(upload_to="car_images/", blank=True, verbose_name='car image')

