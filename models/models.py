from django.db import models

class Company(models.Model):

class Report(models.Model):

	absender = models.ForeignKey(Company, on_delete=models.SET_NULL)
	ersteller = models.ForeignKey(Company, on_delete=models.SET_NULL)
	melder = models.ForeignKey(Company, on_delete=models.SET_NULL)

	kommentar = models.TextField()
	meldetermin =
	bilanzstichtag =
	formular

	class Meta:
		abstract = True

class K3(Report):

class K4(Report):