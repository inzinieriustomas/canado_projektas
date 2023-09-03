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

    start_time = models.DateTimeField(verbose_name='Darbo pradžios laikas')
    end_time = models.DateTimeField(verbose_name='Darbo pabaigos laikas')

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