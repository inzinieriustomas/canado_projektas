from django.db import models
# Create your models here.
class Works(models.Model):

    UTL_CHOICES2 = [
        ("dazytojas", "dazytojas"),
        ("mechanikas", "mechanikas"),
        ("elektrikas", "elektrikas"),
        ("saltkalvis", "saltkalvis"),
        ("vadybininkas", "vadybininkas"),
    ]

    pareigos = models.CharField(
        max_length=20,
        choices=UTL_CHOICES2,
        blank=True)

    darbas = models.CharField( max_length=254,blank=False)


    c_remarks = models.CharField(max_length=256, verbose_name='Pastabos', default='-')

    valandinis_ikainis = models.DecimalField(
        max_digits=10, decimal_places=2,
        verbose_name='Valandinis įkainis', default=0.00
    )

    car = models.ForeignKey(
        'car.Car',
        on_delete=models.SET_NULL,
        verbose_name='Automobilis',
        related_name='works',
        null=True
    )

    darbuotojas = models.ForeignKey(
        'app_canado.User',
        on_delete=models.SET_NULL,
        verbose_name='Darbuotojas',
        related_name='works',
        null=True
    )
    start_time = models.DateTimeField(verbose_name='Darbo pradžios laikas',blank=True, null=True)
    end_time = models.DateTimeField(verbose_name='Darbo pabaigos laikas',blank=True, null=True)

    def skaiciuoti_uzmokesti(self):
        if self.start_time and self.end_time and self.valandinis_ikainis:
            skirtumas = self.end_time - self.start_time
            valandos = skirtumas.total_seconds() / 3600
            uzmokestis = valandos * float(self.valandinis_ikainis)
            galutinis_uzmokestis = round(uzmokestis, 2)
            return galutinis_uzmokestis
        return 0

    def __str__(self):
        return f" {self.darbas}, {self.pareigos}, {self.start_time}, {self.end_time}"