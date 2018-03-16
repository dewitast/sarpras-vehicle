from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Supir(models.Model):
	nama = models.CharField(max_length=100)

class TeleponSupir(models.Model):
	supir = models.ForeignKey(Supir, on_delete=models.CASCADE)
	no_telepon = models.CharField(max_length=100)

class Mobil(models.Model):
	no_polisi = models.CharField(max_length=100)
	nama = models.CharField(max_length=100)
	jenis = models.CharField(max_length=100)
	kapasitas = models.IntegerField()

class FotoMobil(models.Model):
	mobil = models.ForeignKey(Mobil, on_delete=models.CASCADE)
	foto = models.ImageField(upload_to='kendaraan/')

class PeminjamanKendaraan(models.Model):
	nama_peminjam = models.CharField(max_length=100)
	no_telp_peminjam = models.CharField(max_length=100)
	bagian_jurusan_peminjam = models.CharField(max_length=100)
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
	biaya_perawatan = models.IntegerField()
	biaya_bbm = models.IntegerField()
	biaya_supir = models.IntegerField()
	biaya_tol = models.IntegerField()
	biaya_parkir = models.IntegerField()
	biaya_penginapan = models.IntegerField()
	foto_bukti_transfer = models.ImageField(null=True,upload_to='bukti_transfer/')
	status = models.IntegerField()

	def getTotalBiaya(self):
		return self.biaya_perawatan + self.biaya_bbm + self.biaya_supir + self.biaya_tol + self.biaya_parkir + self.biaya_penginapan

class MobilPeminjaman(models.Model):
	peminjaman = models.ForeignKey(PeminjamanKendaraan, on_delete=models.CASCADE)
	mobil = models.ForeignKey(Mobil, on_delete=models.CASCADE)
	odometer_sebelum = models.FloatField(null=True)
	odometer_sesudah = models.FloatField(null=True)
	supir = models.ForeignKey(Supir, on_delete=models.CASCADE, null=True)
