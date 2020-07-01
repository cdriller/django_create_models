from django.db import models
from django.core.validators import RegexValidator

class Company(models.Model):
	name = models.CharField(max_length=80)
	strasse = models.CharField(max_length=80)
	plz = models.CharField(max_length=20)
	ort = models.CharField(max_length=80)
	land = models.CharField(max_length=2,validators=[RegexValidator(regex='^.{2}$', message='Length has to be 2', code='nomatch')])

class Contact(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	anrede = models.CharField(max_length=80)
	vorname = models.CharField(max_length=80)
	zuname = models.CharField(max_length=80)
	abteilung = models.CharField(max_length=80)
	telefon = models.CharField(max_length=80)
	fax = models.CharField(max_length=80)
	email = models.EmailField()
	extranet_id = models.CharField(max_length=8)

class Report(models.Model):
	absender = models.ForeignKey(
		Company,  
		null=True, 
		on_delete=models.SET_NULL,
		related_name="absender"
	)
	absender_kontakt = models.ForeignKey(
		Contact,
		null=True,
		on_delete=models.SET_NULL,
		related_name="absender_kontakt"
	)
	ersteller = models.ForeignKey(
		Company, 
		null=True, 
		on_delete=models.SET_NULL,
		related_name="ersteller"
	)
	ersteller_kontakt = models.ForeignKey(
		Contact,
		null=True,
		on_delete=models.SET_NULL,
		related_name="ersteller_kontakt"
	)
	melder = models.ForeignKey(
		Company,
		on_delete=models.CASCADE,
		related_name="melder"
	)
	melder_kontakt = models.ForeignKey(
		Contact,
		null=True,
		on_delete=models.SET_NULL,
		related_name="melder_kontakt"
	)

	kommentar = models.TextField()
	meldetermin = models.PositiveSmallIntegerField()
	bilanzstichtag = models.DateField()

class K3(models.Model):
	report = models.ForeignKey(Report, null=True, on_delete=models.SET_NULL)
	firma = models.ForeignKey(Company, on_delete=models.CASCADE)

class Balance_Sheet(models.Model):
	k3 = models.OneToOneField(
		K3,
		on_delete=models.SET_NULL,
		null=True
	)
	P01 = models.IntegerField()

# class K4(models.Model):