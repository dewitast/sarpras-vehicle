from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Supir(models.Model):
	nama = models.CharField(max_length=100)

class TeleponSupir(models.Model):
	supir = models.ForeignKey(Supir, on_delete=models.CASCADE)
	no_telepon = models.CharField(max_length=100)

class Peminjam(models.Model):
	nama = models.CharField(max_length=100)
	bagian_jurusan = models.CharField(max_length=100)

class TeleponPeminjam(models.Model):
	peminjam = models.ForeignKey(Peminjam, on_delete=models.CASCADE)
	no_telepon = models.CharField(max_length=100)

class Mobil(models.Model):
	no_polisi = models.CharField(max_length=100)
	nama = models.CharField(max_length=100)
	jenis = models.CharField(max_length=100)
	kapasitas = models.IntegerField()
	supir = models.ForeignKey(Supir, on_delete=models.CASCADE)

class FotoMobil(models.Model):
	mobil = models.ForeignKey(Mobil, on_delete=models.CASCADE)
	foto = models.ImageField(upload_to='kendaraan/')

class PeminjamanKendaraan(models.Model):
	supir = models.ForeignKey(Supir, on_delete=models.CASCADE)
	peminjam = models.ForeignKey(Peminjam, on_delete=models.CASCADE)
	mobil = models.ForeignKey(Mobil, on_delete=models.CASCADE)
	bukti_transfer = models.IntegerField()
	foto_bukti_transfer = models.ImageField(upload_to='bukti transfer peminjaman/')
	foto_form_akhir = models.ImageField(upload_to='bukti form akhir/')
	no_surat = models.CharField(max_length=100)
	tanggal_surat = models.DateTimeField()
	tanggal_booking = models.DateTimeField()
	odometer_sebelum = models.FloatField(null=True)
	odometer_sesudah = models.FloatField(null=True)
	acara = models.CharField(max_length=100)
	tujuan = models.CharField(max_length=100)
	tanggal_pemakaian = models.DateTimeField()
	waktu_berangkat = models.TimeField(default='00:00')
	waktu_datang = models.TimeField(default='00:00')
	tanggal_pengembalian = models.DateTimeField()
	tempat_berkumpul = models.CharField(max_length=100)
	keterangan = models.CharField(max_length=200)
	status = models.IntegerField()