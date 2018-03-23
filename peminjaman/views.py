import csv
import datetime
import os
from calendar import monthrange
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import authenticate, logout
from django.utils.timezone import datetime #important if using timezones
import django_excel as excel
from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT,TA_CENTER
from reportlab.lib.pagesizes import letter, inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import Image, SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
import xlwt

from .models import PeminjamanKendaraan, Mobil, Supir, FotoMobil, TeleponSupir, MobilPeminjaman, PerkiraanBiaya

###################################################################################################################
#
# Global variable
#
###################################################################################################################
MAX_KENDARAAN = 5

###################################################################################################################
#
# Dashboard
#
###################################################################################################################
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('tatacara'))
    else:
        all_peminjaman = PeminjamanKendaraan.objects.all()
        count_booking = {
            'January': 0,
            'February': 0,
            'March': 0,
            'April': 0,
            'May': 0,
            'June': 0,
            'July': 0,
            'August': 0,
            'September': 0,
            'October': 0,
            'November': 0,
            'December': 0,
        }
        count_pemakaian = {
            'January': 0,
            'February': 0,
            'March': 0,
            'April': 0,
            'May': 0,
            'June': 0,
            'July': 0,
            'August': 0,
            'September': 0,
            'October': 0,
            'November': 0,
            'December': 0,
        }
        status_booking_belum_transfer = 0
        status_booking_sudah_transfer = 0
        status_booking_dibatalkan = 0
        status_selesai = 0
        import datetime
        now = datetime.datetime.now()
        for peminjaman in all_peminjaman:
            if str(now.year) == peminjaman.tanggal_pemakaian.strftime('%Y'):
                month_booking = peminjaman.tanggal_booking.strftime('%B')
                month_pemakaian = peminjaman.tanggal_pemakaian.strftime('%B')
                temp = count_booking[month_booking]
                count_booking[month_booking] = temp+1
                temp = count_pemakaian[month_pemakaian]
                count_pemakaian[month_pemakaian] = temp+1

            if peminjaman.status == 0:
                status_booking_belum_transfer += 1
            elif peminjaman.status == 1:
                status_booking_sudah_transfer += 1
            elif peminjaman.status == 2:
                status_selesai += 1
            elif peminjaman.status == 3:
                status_booking_dibatalkan += 1

        years = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027]

        context = {
            'all_peminjaman': all_peminjaman,
            'month_count_booking': count_booking,
            'month_count_pemakaian': count_pemakaian,
            'status_booking_belum_transfer': status_booking_belum_transfer,
            'status_booking_sudah_transfer': status_booking_sudah_transfer,
            'status_selesai': status_selesai,
            'status_booking_dibatalkan': status_booking_dibatalkan,
            'year': now.year,
        }
        return render(request, 'peminjaman/dashboard.html', context)

###################################################################################################################
#
# Tatacara
#
###################################################################################################################
def tatacara(request):
    handle = open(settings.STATIC_ROOT + "\\tatacara.txt",'r+')
    file_perkiraan_biaya = get_object_or_404(PerkiraanBiaya, pk=1)
    var = handle.read()
    handle.close()
    context = {
        'tata_cara' : var,
        'file_perkiraan_biaya': file_perkiraan_biaya
    }
    return render(request, 'peminjaman/tatacara/index.html', context)

def tatacaraEditForm(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        handle = open(settings.STATIC_ROOT + "\\tatacara.txt",'r+')
        var = handle.read()
        handle.close()
        context = {
            'tata_cara' : var,
        }
        return render(request, 'peminjaman/tatacara/edit.html', context)

def tatacaraEdit(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        handle1=open(settings.STATIC_ROOT + "\\tatacara.txt",'r+')
        tata_cara_new = request.POST['textedit']
        handle1.truncate()
        handle1.write(tata_cara_new)
        handle1.close()
        return HttpResponseRedirect(reverse('tatacara'))

def uploadPerkiraanBiaya(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
       # Create new FotoMobil record
        file_perkiraan_biaya = request.FILES.get('file_perkiraan_biaya', False)
        if file_perkiraan_biaya != False:
            file_perkiraan_biaya = PerkiraanBiaya(pdf=request.FILES['file_perkiraan_biaya'],pk=1)
            file_perkiraan_biaya.save()
        return HttpResponseRedirect(reverse('tatacara'))

###################################################################################################################
#
# Peminjaman
#
###################################################################################################################
def peminjaman(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse('login'))
    # else:
    today_month = datetime.today().strftime('%B')
    today_year = datetime.today().strftime('%Y')
    all_peminjaman = PeminjamanKendaraan.objects.all()
    for peminjaman in all_peminjaman:
        data_mobil = MobilPeminjaman.objects.filter(peminjaman_id=peminjaman.id)
        setattr(peminjaman, 'all_kendaraan', data_mobil)
    all_kendaraan = Mobil.objects.all()

    days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    years = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027]
    for peminjaman in all_peminjaman:
        setattr(peminjaman, 'tanggal_booking_formatted', peminjaman.tanggal_booking.strftime('%d %B %Y'))
        setattr(peminjaman, 'tanggal_pemakaian_formatted', peminjaman.tanggal_pemakaian.strftime('%d %B %Y'))
        setattr(peminjaman, 'tanggal_pengembalian_formatted', peminjaman.tanggal_pengembalian.strftime('%d %B %Y'))
        setattr(peminjaman, 'tanggal_surat_formatted', peminjaman.tanggal_surat.strftime('%d %B %Y'))
    context = {
        'days': days,
        'years': years,
        'today_month': today_month,
        'today_year': today_year,
        'all_peminjaman': all_peminjaman,
        'all_kendaraan': all_kendaraan,
    }
    return render(request, 'peminjaman/peminjaman/index.html', context)

def peminjamanDetail(request, peminjaman_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        peminjaman = get_object_or_404(PeminjamanKendaraan, pk=peminjaman_id)
        mobilpeminjaman = MobilPeminjaman.objects.filter(peminjaman_id=peminjaman.id)
        data_mobil = []
        for entry in mobilpeminjaman:
            mobil = Mobil.objects.filter(pk=entry.mobil_id)[0]
            data_mobil.append(mobil)
        setattr(peminjaman, 'tanggal_booking_formatted', peminjaman.tanggal_booking.strftime('%d %B %Y'))
        setattr(peminjaman, 'tanggal_pemakaian_formatted', peminjaman.tanggal_pemakaian.strftime('%d %B %Y'))
        setattr(peminjaman, 'tanggal_pengembalian_formatted', peminjaman.tanggal_pengembalian.strftime('%d %B %Y'))
        setattr(peminjaman, 'tanggal_surat_formatted', peminjaman.tanggal_surat.strftime('%d %B %Y'))
        context = {
            'peminjaman': peminjaman,
            'all_mobil' : data_mobil,
            'mobilpeminjaman' :mobilpeminjaman,
        }
        return render(request, 'peminjaman/peminjaman/detail.html', context)

def peminjamanForm(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        all_mobil = Mobil.objects.all()
        context = {
            'all_mobil': all_mobil,
            'MAX_KENDARAAN' : MAX_KENDARAAN,
            'LOOP_RANGE' : range(MAX_KENDARAAN),
        }
        return render(request, 'peminjaman/peminjaman/create.html', context)

def process_date(date):
    date = date.replace(',', '')
    tokens = date.split(' ')
    if len(tokens[0]) == 1:
        tokens[0] = '0'+tokens[0]
    if tokens[1] == 'January':
        month = '01'
    elif tokens[1] == 'February':
        month = '02'
    elif tokens[1] == 'March':
        month = '03'
    elif tokens[1] == 'April':
        month = '04'
    elif tokens[1] == 'May':
        month = '05'
    elif tokens[1] == 'June':
        month = '06'
    elif tokens[1] == 'July':
        month = '07'
    elif tokens[1] == 'August':
        month = '08'
    elif tokens[1] == 'September':
        month = '09'
    elif tokens[1] == 'October':
        month = '10'
    elif tokens[1] == 'November':
        month = '11'
    elif tokens[1] == 'December':
        month = '12'
    return     tokens[2]+'-'+month+'-'+tokens[0]+' 00:00Z'

def process_time(time):
    t = time.split(' ')
    if t[1] == 'PM':
        x = t[0].split(':')
        hour = int(x[0])
        minute = int(x[1])
        hour += 12
        a = '%s:%s' % (hour, minute)
    else:
        a = t[0]
    return a

def peminjamanCreate(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        try:
            # Create new Peminjam record
            nama_peminjam = request.POST['nama_peminjam']
            no_telp_peminjam = request.POST['no_telepon_peminjam']
            bagian_jurusan_peminjam = request.POST.get('bagian_jurusan', None)

            # Create new Peminjaman Kendaraaan record
            no_surat = request.POST['no_surat']
            tanggal_surat = process_date(request.POST['tanggal_surat'])
            tanggal_booking = process_date(request.POST['tanggal_booking'])
            acara = request.POST['acara']
            tujuan = request.POST['tujuan']
            tanggal_pemakaian = process_date(request.POST['tanggal_pemakaian'])
            waktu_berangkat = process_time(request.POST['waktu_berangkat'])
            waktu_datang = process_time(request.POST['waktu_datang'])
            tanggal_pengembalian = process_date(request.POST['tanggal_pengembalian'])
            tempat_berkumpul = request.POST['tempat_berkumpul']
            keterangan = request.POST.get('keterangan', '')
            biaya_perawatan = request.POST['biaya_perawatan']
            biaya_bbm = request.POST['biaya_bbm']
            biaya_supir = request.POST['biaya_supir']
            biaya_tol = request.POST['biaya_tol']
            biaya_parkir = request.POST['biaya_parkir']
            biaya_penginapan = request.POST['biaya_penginapan']
            STATUS = 0     # status peminjaman
            peminjaman = PeminjamanKendaraan(
                nama_peminjam=nama_peminjam,
                no_telp_peminjam=no_telp_peminjam,
                bagian_jurusan_peminjam=bagian_jurusan_peminjam,
                no_surat=no_surat,
                tanggal_surat=tanggal_surat,
                tanggal_booking=tanggal_booking,
                acara=acara,
                tujuan=tujuan,
                tanggal_pemakaian=tanggal_pemakaian,
                tanggal_pengembalian=tanggal_pengembalian,
                waktu_berangkat=waktu_berangkat,
                waktu_datang=waktu_datang,
                tempat_berkumpul=tempat_berkumpul,
                keterangan=keterangan,
                biaya_perawatan=biaya_perawatan,
                biaya_bbm=biaya_bbm,
                biaya_supir=biaya_supir,
                biaya_tol=biaya_tol,
                biaya_parkir=biaya_parkir,
                biaya_penginapan=biaya_penginapan,
                odometer_sebelum=0,
                odometer_sesudah=0,
                status=STATUS
                )
            peminjaman.save()
            jumlah_kendaraan = int(request.POST['jumlah_kendaraan'])
            for i in range(jumlah_kendaraan):
                mobil_id = request.POST.get('mobil_id' + str(i))
                mobilpeminjaman = MobilPeminjaman(
                    peminjaman_id = peminjaman.id,
                    mobil_id = mobil_id
                    )
                mobilpeminjaman.save()
        except (KeyError):
            # Redisplay the form
            return HttpResponseRedirect(reverse('peminjamanForm'))
        else:
            # Display detail peminjaman
            return HttpResponseRedirect(reverse('peminjamanDetail', args=(peminjaman.id,)))

def peminjamanEditForm(request, peminjaman_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        peminjaman = get_object_or_404(PeminjamanKendaraan, pk=peminjaman_id)
        setattr(peminjaman, 'tanggal_booking_formatted', peminjaman.tanggal_booking.strftime('%Y-%m-%d'))
        setattr(peminjaman, 'tanggal_pemakaian_formatted', peminjaman.tanggal_pemakaian.strftime('%Y-%m-%d'))
        setattr(peminjaman, 'tanggal_pengembalian_formatted', peminjaman.tanggal_pengembalian.strftime('%Y-%m-%d'))
        setattr(peminjaman, 'tanggal_surat_formatted', peminjaman.tanggal_surat.strftime('%Y-%m-%d'))

        mobil_peminjaman = list(MobilPeminjaman.objects.filter(peminjaman_id=peminjaman_id))
        all_mobil = Mobil.objects.all()
        context = {
            'peminjaman': peminjaman,
            'data_mobil': mobil_peminjaman,
            'all_mobil': all_mobil,
            'MAX_KENDARAAN' : MAX_KENDARAAN,
            'LOOP_RANGE' : range(MAX_KENDARAAN),
        }
        return render(request, 'peminjaman/peminjaman/edit.html', context)

def peminjamanEdit(request, peminjaman_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        try:
            # Edit Peminjaman Kendaraaan record
            peminjaman = get_object_or_404(PeminjamanKendaraan, pk=peminjaman_id)

            peminjaman.nama_peminjam = request.POST['nama_peminjam']
            peminjaman.no_telp_peminjam = request.POST['no_telepon_peminjam']
            peminjaman.bagian_jurusan_peminjam = request.POST['bagian_jurusan']

            peminjaman.status = request.POST['status']
            peminjaman.acara = request.POST['acara']
            peminjaman.tujuan = request.POST['tujuan']
            peminjaman.tempat_berkumpul = request.POST['tempat_berkumpul']
            peminjaman.keterangan = request.POST['keterangan']
            peminjaman.no_surat = request.POST['no_surat']
            peminjaman.waktu_berangkat = process_time(request.POST['waktu_berangkat'])
            peminjaman.waktu_datang = process_time(request.POST['waktu_datang'])

            peminjaman.biaya_perawatan = request.POST['biaya_perawatan']
            peminjaman.biaya_bbm = request.POST['biaya_bbm']
            peminjaman.biaya_supir = request.POST['biaya_supir']
            peminjaman.biaya_tol = request.POST['biaya_tol']
            peminjaman.biaya_parkir = request.POST['biaya_parkir']
            peminjaman.biaya_penginapan = request.POST['biaya_penginapan']
            
            status = request.POST['status']                
            if (status == '0'):
              peminjaman.metode_transfer = None
              peminjaman.foto_bukti_transfer = None
            else :
              peminjaman.metode_transfer = request.POST['metode_transfer'] 
              
            metode_transfer = request.POST['metode_transfer'] 
            if (metode_transfer == '6'):
              peminjaman.foto_bukti_transfer = None
              
            tanggal_booking = request.POST['tanggal_booking']
            if '-' not in tanggal_booking:
                peminjaman.tanggal_booking = process_date(tanggal_booking)
            tanggal_pemakaian = request.POST['tanggal_pemakaian']
            if '-' not in tanggal_pemakaian:
                peminjaman.tanggal_pemakaian = process_date(tanggal_pemakaian)
            tanggal_pengembalian = request.POST['tanggal_pengembalian']
            if '-' not in tanggal_pengembalian:
                peminjaman.tanggal_pengembalian = process_date(tanggal_pengembalian)
            tanggal_surat = request.POST['tanggal_surat']
            if '-' not in tanggal_surat:
                peminjaman.tanggal_surat = process_date(tanggal_surat)
            peminjaman.save()
        except (KeyError):
            # Redisplay the form
            return HttpResponseRedirect(reverse('peminjamanEdit'))
        else:
            # Display peminjaman detail
            return HttpResponseRedirect(reverse('peminjamanDetail', args=(peminjaman.id,)))

def peminjamanDelete(request, peminjaman_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        peminjaman = get_object_or_404(PeminjamanKendaraan, pk=peminjaman_id)
        peminjaman.delete()
        return HttpResponseRedirect(reverse('peminjaman'))

def peminjamanCancel(request, peminjaman_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        peminjaman = get_object_or_404(PeminjamanKendaraan, pk=peminjaman_id)
        peminjaman.status = 4;
        peminjaman.save()
        return HttpResponseRedirect(reverse('peminjamanDetail', args=(peminjaman.id,)))

def uploadBuktiTransfer(request, peminjaman_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        # Create new FotoMobil record
        peminjaman = get_object_or_404(PeminjamanKendaraan, pk=peminjaman_id)
        foto_bukti_transfer = request.FILES.get('foto_bukti_transfer', False)
        metode_transfer = request.POST['metode_transfer']
        if foto_bukti_transfer != False:
            if peminjaman.status == 0:
                peminjaman.status = 1
            peminjaman.foto_bukti_transfer = foto_bukti_transfer
            peminjaman.metode_transfer = metode_transfer
            peminjaman.save()
        return HttpResponseRedirect(reverse('peminjamanDetail', args=(peminjaman.id,)))

def deleteBuktiTransfer(request, peminjaman_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        peminjaman = get_object_or_404(PeminjamanKendaraan, pk=peminjaman_id)
        if peminjaman.status == 1:
            peminjaman.status = 0
        peminjaman.foto_bukti_transfer = None
        peminjaman.metode_transfer = None
        peminjaman.save()
        return HttpResponseRedirect(reverse('peminjamanDetail', args=(peminjaman_id,)))

#Form Final
def peminjamanFormFinal(request, peminjaman_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        mobil_peminjaman = list(MobilPeminjaman.objects.filter(peminjaman_id=peminjaman_id))
        all_supir = list(Supir.objects.all());
        context = {
            'mobil_peminjaman' : mobil_peminjaman,
            'peminjaman_id' : peminjaman_id,
            'all_supir': all_supir,
        }
        return render(request, 'peminjaman/peminjaman/formFinal.html', context)

def formFinalEdit(request, peminjaman_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        try:
            # Edit Peminjaman Kendaraaan odomoter record
            Mobil_Peminjaman = list(MobilPeminjaman.objects.filter(peminjaman_id=peminjaman_id))
            counter = 1
            for daftar_mobil in Mobil_Peminjaman:
                daftar_mobil.odometer_sebelum = request.POST['odometer_sebelum'+str(daftar_mobil.mobil.id)]
                daftar_mobil.odometer_sesudah = request.POST['odometer_sesudah'+str(daftar_mobil.mobil.id)]
                supir_id = request.POST['supir_id'+str(counter)]
                counter=counter+1
                supir = get_object_or_404(Supir, pk =supir_id)
                daftar_mobil.supir = supir;
                daftar_mobil.save()
            return HttpResponseRedirect(reverse('peminjaman'))
        except:
            return HttpResponseRedirect(reverse('peminjamanFormFinal', args=(peminjaman_id,)))
###################################################################################################################
#
# Supir
#
###################################################################################################################
def supir(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        all_supir = Supir.objects.all()
        for supir in all_supir:
            setattr(supir, 'no_telepon', get_object_or_404(TeleponSupir, supir_id=supir.id).no_telepon)
        context = {
            'all_supir': all_supir,
        }
        return render(request, 'peminjaman/supir/index.html', context)

def supirForm(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        context = {
        }
        return render(request, 'peminjaman/supir/create.html', context)

def supirCreate(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        try:
            # Create new Supir record
            nama = request.POST['nama']
            supir = Supir(nama=nama)
            supir.save()

            # Create new TeleponSupir record
            supir_id = supir.id
            no_telepon = request.POST['no_telepon']
            telepon_supir = TeleponSupir(supir_id=supir_id, no_telepon=no_telepon)
            telepon_supir.save()
        except (KeyError):
            # Redisplay the form
            return render(request, 'peminjaman/supir/create.html', {
                'error_message': "You didn't fill all the form :("
                })
        else:
            return HttpResponseRedirect(reverse('supir'))

def supirEditForm(request, supir_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        supir = get_object_or_404(Supir, pk=supir_id)
        telepon_supir = get_object_or_404(TeleponSupir, supir_id=supir_id)
        setattr(supir, 'no_telepon', telepon_supir.no_telepon)

        context = {
            'supir': supir,
        }
        return render(request, 'peminjaman/supir/edit.html', context)

def supirEdit(request, supir_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        try:
            # Edit Supir record
            supir = get_object_or_404(Supir, pk=supir_id)
            supir.nama = request.POST['nama']
            supir.save()

            telepon_supir = get_object_or_404(TeleponSupir, supir_id=supir_id)
            telepon_supir.no_telepon = request.POST['no_telepon']
            telepon_supir.save()
        except (KeyError):
            # Redisplay the form
            return render(request, 'peminjaman/supir/edit.html', {
                'error_message': "You didn't fill all the form :("
                })
        else:
            return HttpResponseRedirect(reverse('supir'))

def supirDelete(request, supir_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        supir = get_object_or_404(Supir, pk=supir_id)
        supir.delete()
        return HttpResponseRedirect(reverse('supir'))

###################################################################################################################
#
# Kendaraan
#
###################################################################################################################
def kendaraan(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse('login'))
    # else:
    all_kendaraan = Mobil.objects.all()
    fotos = []
    for kendaraan in all_kendaraan:
        try:
            all_foto = FotoMobil.objects.filter(mobil_id=kendaraan.id)
            k = {}
            k['id'] = kendaraan.id
            f = []
            count = 0
            for foto in all_foto:
                f.append(foto)
                count += 1
            k['count'] = count
            k['foto'] = f
            fotos.append(k)
        except FotoMobil.DoesNotExist:
            comment = None
    context = {
        'all_kendaraan': all_kendaraan,
        'foto': fotos,
    }
    return render(request, 'peminjaman/kendaraan/index.html', context)

def kendaraanDetail(request, kendaraan_id):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse('login'))
    # else:
    mobil = get_object_or_404(Mobil, pk=kendaraan_id)
    all_foto = FotoMobil.objects.filter(mobil_id=kendaraan_id)
    context = {
        'kendaraan': mobil,
        'all_foto': all_foto,
    }
    return render(request, 'peminjaman/kendaraan/detail.html', context)

def kendaraanForm(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'peminjaman/kendaraan/create.html')

def kendaraanCreate(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        try:
            # Create new Kendaraan record
            nama = request.POST['nama']
            jenis = request.POST['jenis']
            no_polisi = request.POST['no_polisi']
            kapasitas = request.POST['kapasitas']
            mobil = Mobil(nama=nama, jenis=jenis, no_polisi=no_polisi, kapasitas=kapasitas)
            mobil.save()

            foto = request.FILES.get('foto', False)
            if foto != False:
                foto_mobil = FotoMobil(foto=request.FILES['foto'], mobil_id=mobil.id)
                foto_mobil.save()

        except KeyError as e:
            # Redisplay the form
            return HttpResponseRedirect(reverse('peminjamanForm'))
        else:
            return HttpResponseRedirect(reverse('kendaraan'))

def kendaraanEditForm(request, kendaraan_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        mobil = get_object_or_404(Mobil, pk=kendaraan_id)
        context = {
            'kendaraan': mobil,
        }
        return render(request, 'peminjaman/kendaraan/edit.html', context)

def kendaraanEdit(request, kendaraan_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        try:
            # Edit Kendaraaan record
            kendaraan = get_object_or_404(Mobil, pk=kendaraan_id)
            kendaraan.nama = request.POST['nama']
            kendaraan.jenis = request.POST['jenis']
            kendaraan.kapasitas = request.POST['kapasitas']
            kendaraan.no_polisi = request.POST['no_polisi']
            kendaraan.save()
        except (KeyError):
            # Redisplay the form
            return HttpResponseRedirect(reverse('kendaraanEditForm'))
        else:
            return HttpResponseRedirect(reverse('kendaraanDetail', args=(kendaraan_id,)))

def kendaraanDelete(request, kendaraan_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        kendaraan = get_object_or_404(Mobil, pk=kendaraan_id)
        kendaraan.delete()
        return HttpResponseRedirect(reverse('kendaraan'))

def kendaraanCekKetersediaan(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        context = {
        }
        return render(request, 'peminjaman/kendaraan/cekKetersediaan.html', context)

def kendaraanUploadFoto(request, kendaraan_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        # Create new FotoMobil record
        foto = request.FILES.get('foto', False)
        if foto != False:
            foto_mobil = FotoMobil(foto=request.FILES['foto'], mobil_id=kendaraan_id)
            foto_mobil.save()
        return HttpResponseRedirect(reverse('kendaraanDetail', args=(kendaraan_id,)))

def kendaraanDeleteFoto(request, kendaraan_id, foto_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        foto_mobil = get_object_or_404(FotoMobil, pk=foto_id)
        foto_mobil.delete()
        return HttpResponseRedirect(reverse('kendaraanDetail', args=(kendaraan_id,)))

###################################################################################################################
#
# AUTHENTICATION
#
###################################################################################################################
def loginForm(request):
    return render(request, 'peminjaman/login.html')

###################################################################################################################
#
# REPORT / FORM
#
###################################################################################################################
def export_pdf_peminjaman(request, peminjaman_id):
    # Set Response
    FILENAME = 'Surat_Perizinan_' + peminjaman_id;
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="' + FILENAME + '.pdf"'

    # Database
    peminjaman = get_object_or_404(PeminjamanKendaraan, pk=peminjaman_id)

    # Size
    FONT_SIZE = 12
    LINE_WIDTH = .3
    LINE_DIFF = FONT_SIZE + int(LINE_WIDTH * FONT_SIZE)

    # Setup
    can = canvas.Canvas(response)
    can.setLineWidth(LINE_WIDTH)

    # Content
    ditsarpras = 'Direktorat Sarana dan Prasarana'
    institut = 'Institut Teknologi Bandung'
    alamat = 'JL. Ganesha 10 Bandung. Telp (022) 86010100'
    title = 'FORMULIR PERSETUJUAN PEMINJAMAN KENDARAAN'
    nomor = 'Nomor : '
    content_left = ['No. Booking', 'Pemohon', 'Unit Kerja', 'Hari', 'Tanggal', 'Tujuan', 'Acara']
    day = datetime.strptime(peminjaman.tanggal_pemakaian.strftime('%d %B %Y'), '%d %B %Y').strftime('%A')
    peminjaman_left = [str(peminjaman.id)+'/BK/TR/2018', peminjaman.nama_peminjam, peminjaman.bagian_jurusan_peminjam,dayToHari(day), peminjaman.tanggal_pemakaian.strftime('%d/%m/%Y') +
                        ' s.d. ' + peminjaman.tanggal_pengembalian.strftime('%d/%m/%Y'), peminjaman.tujuan, peminjaman.acara]
    content_right = ['No. Surat Pemohon', 'Contact Person', 'Telp.', 'Pukul']
    peminjaman_right = [peminjaman.no_surat, peminjaman.nama_peminjam, peminjaman.no_telp_peminjam, str(peminjaman.waktu_berangkat)]
    rincian_biaya = 'Rincian biaya :'
    content_biaya = ['Biaya Perawatan', 'BBM', 'Uang Lelah Sopir', 'Tol', 'Parkir', 'Penginapan', 'Jumlah Total']
    peminjaman_biaya = [peminjaman.biaya_perawatan, peminjaman.biaya_bbm, peminjaman.biaya_supir, peminjaman.biaya_tol,
                        peminjaman.biaya_parkir, peminjaman.biaya_penginapan, peminjaman.getTotalBiaya()]
    disetujui = 'Disetujui/Tidak disetujui'
    posisi_penanda_tangan = 'Direktorat Sarana dan Prasarana'
    nama_penanda_tangan = 'Wahyu Srigutomo.,S.Si.,M.Si.,Ph.D.'
    nip_penanda_tangan = 'NIP. ' + '197007131997021001'
    jumlah = 'Jumlah*       = Rp. '
    keterangan_jumlah1 = '* Nominal yang ditransfer ke rekening'
    keterangan_jumlah2 = 'penampungan kemitraan ITB'
    nama_transfer = 'Penampungan Kemitraan ITB'
    nomor_rekening = '0900002017'
    footer = [['Mohon semua penyelesaian administrasi dapat dilunasi sebelum penggunaan ke '],
                [nama_transfer, ' rekening nomor : ', nomor_rekening, ' pada PT Bank Negara'],
                ['Indonesia (BNI Persero) tbk. Cabang ITB Jl. Tamansari No.80 Bandung dan BNI-Kampus'],
                ['ITB. Untuk meudahkan penelusuran, fotocopy bukti pembayaran mohon dikirim kepada'],
                ['Direktorat Sarana dan Prasarana Jl. Ganesha 10 Bandung. Tlp (022) 2507910']]

    # Position
    x = 72
    y = 778
    xpos = 0 # X-Position of colon

    # Header
    xoffset = 60
    can.setFont('Helvetica-Bold', FONT_SIZE + 3)
    can.drawString(x+xoffset, y, ditsarpras)
    y -= LINE_DIFF
    can.setFont('Helvetica-Bold', FONT_SIZE + 2)
    can.drawString(x+xoffset, y, institut)
    y -= LINE_DIFF
    can.setFont('Helvetica-Bold', FONT_SIZE + 1)
    can.drawString(x+xoffset, y, alamat)

    # Logo
    base_url = '{0}://{1}{2}logo.png'.format(request.scheme, request.get_host(), settings.MEDIA_URL)
    logo = ImageReader(base_url)
    width, height = logo.getSize()
    aspect = height / float(width)
    logo_img = Image(base_url, width=width/4, height = width*aspect/4)
    y -= LINE_DIFF / 2
    logo_img.drawOn(can, x, y)
    y -= LINE_DIFF / 2

    # Title
    y -= 3*LINE_DIFF
    x += 220
    can.setFont('Helvetica-Bold', FONT_SIZE + 2)
    can.drawCentredString(x, y, title)
    y -= LINE_DIFF
    can.setFont('Helvetica-Bold', FONT_SIZE)
    can.drawCentredString(x, y, nomor + peminjaman_id)
    y -= 2*LINE_DIFF
    tempy = y;
    x += 10

    # Form
    can.setFont('Helvetica', FONT_SIZE)
    xpos = 0
    for content in content_right:
        can.drawString(x, tempy, content)
        tempy -= LINE_DIFF
        xpos = max(xpos, stringWidth(content, 'Helvetica', FONT_SIZE))
    x += xpos + 1
    tempy = y
    for fill in peminjaman_right:
        can.drawString(x, tempy, ':')
        can.drawString(x+5, tempy, fill)
        tempy -= LINE_DIFF
    x -= 230
    x -= xpos + 1
    xpos = 0
    tempy = y
    for content in content_left:
        can.drawString(x, tempy, content)
        tempy -= LINE_DIFF
        xpos = max(xpos, stringWidth(content, 'Helvetica', FONT_SIZE))
    x += xpos + 1
    for fill in peminjaman_left:
        can.drawString(x, y, ':')
        can.drawString(x+5, y, fill)
        y -= LINE_DIFF
    y -= LINE_DIFF
    x -= xpos + 1

    # Biaya
    can.drawString(x, y, rincian_biaya)
    can.setFont('Helvetica-Bold', FONT_SIZE)
    y -= 2*LINE_DIFF
    xpos = 0
    tempy = y
    for biaya in content_biaya:
        can.drawString(x, tempy, biaya)
        tempy -= LINE_DIFF
        xpos = max(xpos, stringWidth(biaya, 'Helvetica', FONT_SIZE))
    x += xpos + 1
    for fill in peminjaman_biaya:
        can.drawString(x+50, y, ': Rp. ')
        can.drawString(x+80, y, '{:,}'.format(fill))
        y -= LINE_DIFF
    x -= xpos + 1

    # Tanda Tangan
    xoffset = 105
    can.setFont('Helvetica-Bold', FONT_SIZE)
    y -= 3*LINE_DIFF
    can.drawCentredString(x+xoffset, y, disetujui)
    can.drawString(x+2.2*xoffset, y, jumlah)
    can.drawString(x+2.2*xoffset+stringWidth(jumlah, 'Helvetica-Bold', FONT_SIZE)+1, y, '{:,}'.format(peminjaman.getTotalBiaya()))
    y -= LINE_DIFF
    can.drawCentredString(x+xoffset, y, posisi_penanda_tangan)
    y -= LINE_DIFF
    can.setFont('Helvetica', FONT_SIZE)
    can.drawString(x+2.2*xoffset, y, keterangan_jumlah1)
    y -= LINE_DIFF
    can.drawString(x+2.2*xoffset, y, keterangan_jumlah2)
    can.setFont('Helvetica-Bold', FONT_SIZE)
    y -= 4*LINE_DIFF
    can.drawCentredString(x+xoffset, y, nama_penanda_tangan)
    nama_length = stringWidth(nama_penanda_tangan, 'Helvetica-Bold', FONT_SIZE)
    can.line(x+xoffset-nama_length//2, y-2, x+xoffset+nama_length//2, y-2)
    y -= LINE_DIFF
    can.drawCentredString(x+xoffset, y, nip_penanda_tangan)

    # Keterangan
    can.setFont('Helvetica', FONT_SIZE-1)
    y -= 3*LINE_DIFF
    for line in footer:
        xtemp = x
        for sentence in line:
            if sentence == nama_transfer or sentence == nomor_rekening:
                can.setFont('Helvetica-Bold', FONT_SIZE-1)
                can.drawString(xtemp, y, sentence)
                xtemp += stringWidth(sentence, 'Helvetica-Bold', FONT_SIZE-1)
            else:
                can.setFont('Helvetica', FONT_SIZE-1)
                can.drawString(xtemp, y, sentence)
                xtemp += stringWidth(sentence, 'Helvetica', FONT_SIZE-1)
        y -= LINE_DIFF

    # Finish
    can.showPage()
    can.save()
    return response

def export_pdf_surat_tugas(request, peminjaman_id):
    # Set Response
    FILENAME = 'Surat_Tugas_' + peminjaman_id;
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="' + FILENAME + '.pdf"'

    # Database
    peminjaman = get_object_or_404(PeminjamanKendaraan, pk=peminjaman_id)
    all_mobil = MobilPeminjaman.objects.filter(peminjaman_id=peminjaman_id)

    # Setup
    elements = []
    doc = SimpleDocTemplate(response, pagesize=letter)
    big_space = Spacer(1, 0.2*inch)

    count = 0
    for i in all_mobil : 
        mobil = get_object_or_404(Mobil, pk=all_mobil[count].mobil_id)
        namasupir =''
        odometersebelum = ''
        odometersesudah =''

        if all_mobil[count].supir is not None:
            namasupir = all_mobil[count].supir.nama
            odometersebelum = all_mobil[count].odometer_sebelum
            odometersesudah = all_mobil[count].odometer_sesudah

        #logo
        base_url = '{0}://{1}{2}logo.png'.format(request.scheme, request.get_host(), settings.MEDIA_URL)
        logo = ImageReader(base_url)
        width, height = logo.getSize()
        aspect = height / float(width)
        logo_img = Image(base_url, width=width/7, height = width*aspect/7)
        
        # Content
        institut = 'INSTITUT TEKNOLOGI BANDUNG'
        alamat = 'Jalan Tamansari No. 73 Telp. (022) 2509179, 2501645, Pos. 6708 BANDUNG 4011 '
        title_surat = 'SURAT TUGAS'
        
        #day to hari
        day = str(datetime.strptime(peminjaman.tanggal_pemakaian.strftime('%d %B %Y'), '%d %B %Y').strftime('%A'))
        form_surat = [['Nama Pengemudi',': '+namasupir],
                ['Jenis Kendaraan', ': '+mobil.jenis+' No Polisi : '+mobil.no_polisi],
                ['', ''],
                ['Untuk Melaksanakan tugas', ': Dinas / Sosial / Rekreasi dengan'],
                ['Nama',': '+peminjaman.nama_peminjam],
                ['Bagian/Jurusan',': '+peminjaman.bagian_jurusan_peminjam],
                ['Tujuan',': '+peminjaman.tujuan],
                ['Hari / Tanggal', ': '+dayToHari(day)+' / '+peminjaman.tanggal_pemakaian.strftime('%d/%m/%Y')],
                ['Berangkat pukul/ Dari',': '+str(peminjaman.waktu_berangkat)+' / '+peminjaman.tempat_berkumpul],
                ['Pulang Pukul',': '+str(peminjaman.waktu_datang)],
                ['Odometer Awal',': '+ str(odometersebelum)],
                ['Odometer Akhir',': '+ str(odometersesudah)]]
        
        # for entry in biaya:
        #     entry[1] = '{:,}'.format(entry[1]) # Thousands comma delimiter
        
        isi_surat = 'Demikian surat tugas ini kami buat, dengan harapan yang bersangkutan dapat melaksanakan tugasnya dengan rasa penuh tanggung jawab, dan kepada yang berwajib kami mohon bantuan seperlunya bila terjadi hal hal yang tidak kami inginnkan. Terima kasih.'
        pengantar_surat = 'Yang bertanda tangan dibawah ini, Kasi Transportasi memberikan tugas kepada:'
        catatan_title = 'Catatan:'
        catatan_data = ['Harap Surat Tugas ini dikembalikan ke Kasie bilamana tugas ini selesai']
        pengguna = 'Pengguna :'
        waktu_tempat = 'Bandung, ' + getTanggal(datetime.today())
        posisi_penanda_tangan = 'Kepala Seksi Transportasi'
        nama_penanda_tangan = 'Ade Sumarna'
        nip_penanda_tangan = 'NIP. 197810272014091004'
        nama_pengendara = namasupir

        # Size
        TAB_WIDTH = 2.6
        TAB_HEIGHT = 0.2
        COL_NUM = 2
        BIAYA_ROW = len(form_surat)

        # Style
        tab_style = TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.white),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.white)],)
        par_title_style = ParagraphStyle(
                    name='Normal',
                    fontName='Helvetica-Bold',
                    fontSize=14,
                    alignment=TA_CENTER,
                )
        par_subtitle_style = ParagraphStyle(
                    name='Normal',
                    fontName='Helvetica-Bold',
                    fontSize=12,
                    alignment=TA_CENTER,
                )
        par_style = ParagraphStyle(
                    name='Normal',
                    fontName='Helvetica',
                    fontSize=9,
                )
        par_address_style = ParagraphStyle(
                    name='Normal',
                    fontName='Helvetica',
                    fontSize=6,
                    alignment=TA_CENTER,
                )        
        par_right_style = ParagraphStyle(
                    name='Normal',
                    fontName='Helvetica',
                    fontSize=10,
                    alignment=TA_RIGHT,
                )
        par_left_style = ParagraphStyle(
                    name='Normal',
                    fontName='Helvetica',
                    fontSize=10,
                )
        par_center_style = ParagraphStyle(
                    name='Normal',
                    fontName='Helvetica',
                    fontSize=9,
                    alignment=TA_CENTER,
                )
        par_right_bold_style = ParagraphStyle(
                    name='Normal',
                    fontName='Helvetica-Bold',
                    fontSize=10,
                    alignment=TA_RIGHT,
                )
        
        # Elements
        institut_par = Paragraph(institut,par_title_style)
        alamat_par = Paragraph(alamat,par_address_style)
        title_surat_par = Paragraph(title_surat,par_subtitle_style)
        pengantar_surat_par = Paragraph(pengantar_surat,par_left_style) 
        isi_surat_par = Paragraph(isi_surat,par_left_style)
        tab_form_surat = Table(form_surat, COL_NUM*[TAB_WIDTH*inch], BIAYA_ROW*[TAB_HEIGHT*inch])
        tab_form_surat.setStyle(tab_style)
        catatan_title_par = Paragraph(catatan_title, par_style)
        waktu_tempat_par = Paragraph(waktu_tempat, par_right_style)
        kosong_par = Paragraph('',par_left_style)
        posisi_penanda_tangan_par = Paragraph(posisi_penanda_tangan, par_right_style)
        nama_penanda_tangan_par = Paragraph(nama_penanda_tangan, par_right_bold_style)
        nama_pengendara_par = Paragraph(nama_pengendara, par_left_style)
        nip_penanda_tangan_par = Paragraph(nip_penanda_tangan, par_right_style)
        pengguna_par = Paragraph(pengguna,par_left_style)

        tbl_data = [[logo_img,institut_par],
                    [kosong_par,alamat_par]]

        tbl = Table(tbl_data, colWidths=[0,400])
        
        tbl1_data = [[kosong_par, waktu_tempat_par],
                    [pengguna_par, posisi_penanda_tangan_par]]

        tbl1 = Table(tbl1_data)
        
        tbl2_data = [[nama_pengendara_par,nama_penanda_tangan_par],
                    [kosong_par,nip_penanda_tangan_par]]
        tbl2= Table(tbl2_data)

        # Append
        elements.append(tbl)
        elements.append(big_space)
        elements.append(title_surat_par)
        elements.append(big_space)
        elements.append(pengantar_surat_par)
        elements.append(big_space)
        elements.append(tab_form_surat)
        elements.append(big_space)
        elements.append(isi_surat_par)
        elements.append(big_space)
        elements.append(tbl1)
        elements.append(big_space)
        elements.append(big_space)
        elements.append(big_space)
        elements.append(big_space)
        elements.append(tbl2)
        elements.append(catatan_title_par)
        for catatan in catatan_data:
            elements.append(Paragraph('* ' + catatan, par_style))
        

        elements.append(big_space)
        elements.append(big_space)
        elements.append(big_space)
        elements.append(big_space)
        elements.append(big_space)
        elements.append(big_space)
        elements.append(big_space)
        elements.append(big_space)


        day = str(datetime.strptime(peminjaman.tanggal_pemakaian.strftime('%d %B %Y'), '%d %B %Y').strftime('%A'))
        title_biaya = 'Perincian Biaya Perjalanan'
        biaya = [['Jenis Kendaraan', ': '+mobil.jenis],
                ['Sebanyak', ': '+ str(len(all_mobil))],
                ['Hari / Tanggal Pemakaian',': '+ dayToHari(day) +' / '+peminjaman.tanggal_pemakaian.strftime('%d/%m/%Y')],
                ['Asal',': '+peminjaman.tempat_berkumpul],
                ['Tujuan',': '+peminjaman.tujuan],
                ['Acara',': '+peminjaman.acara],
                ['Pengguna / No.Kontak',': '+peminjaman.nama_peminjam+' / '+peminjaman.no_telp_peminjam],
                ['Pengemudi',': '+namasupir],
                [''],
                ['BBM (Rp.)', peminjaman.biaya_bbm],
                ['Uang Lelah Sopir (Rp.)', peminjaman.biaya_supir],
                ['Tol (Rp.)', peminjaman.biaya_tol],
                ['Parkir (Rp.)', peminjaman.biaya_parkir],
                ['Penginapan (Rp.)', peminjaman.biaya_penginapan],
                [Paragraph('Jumlah Akomodasi(Rp.)',ParagraphStyle(name='Normal',fontName='Helvetica-Bold',)), peminjaman.getTotalBiaya()-peminjaman.biaya_perawatan]]
        harga = 0
        for entry in biaya:
            if (harga > 8) :
                entry[1] = '{:,}'.format(entry[1]) # Thousands comma delimiter
            
            harga= harga+1

        catatan_title = 'Catatan:'
        catatan_data = ['Harap surat perincian ini dikembalikan ke Kas ie bilamana tugas sudah selesai',
                    'Semua bukti akomodasi(Uang lelah Sopir, Tol, Parkir,dll agar disetorkan ke Kasie']

        waktu_tempat = 'Bandung, ' + getTanggal(datetime.today())
        posisi_penanda_tangan = 'Kepala Seksi Transportasi'
        nama_penanda_tangan = 'Ade Sumarna'
        nip_penanda_tangan = 'NIP. 197810272014091004'


        # Size
        TAB_WIDTH = 3.2
        TAB_HEIGHT = 0.3
        COL_NUM = 2
        BIAYA_ROW = len(biaya)

        # Style
        tab_style = TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black)
            ])
        title_style = ParagraphStyle(
                    name='Normal',
                    fontName='Helvetica-Bold',
                    fontSize=12,
                )
        par_style = ParagraphStyle(
                    name='Normal',
                    fontName='Helvetica',
                    fontSize=9,
                )
        par_right_style = ParagraphStyle(
                    name='Normal',
                    fontName='Helvetica',
                    fontSize=10,
                    alignment=TA_RIGHT,
                )
        par_right_bold_style = ParagraphStyle(
                    name='Normal',
                    fontName='Helvetica-Bold',
                    fontSize=10,
                    alignment=TA_RIGHT,
                )

        # Elements
        title_biaya_par = Paragraph(title_biaya, title_style)
        tab_biaya = Table(biaya, COL_NUM*[TAB_WIDTH*inch], BIAYA_ROW*[TAB_HEIGHT*inch])
        tab_biaya.setStyle(tab_style)
        catatan_title_par = Paragraph(catatan_title, par_style)
        waktu_tempat_par = Paragraph(waktu_tempat, par_right_style)
        posisi_penanda_tangan_par = Paragraph(posisi_penanda_tangan, par_right_style)
        nama_penanda_tangan_par = Paragraph(nama_penanda_tangan, par_right_bold_style)
        nip_penanda_tangan_par = Paragraph(nip_penanda_tangan, par_right_style)

        # Append
        elements.append(title_biaya_par)
        elements.append(big_space)
        elements.append(tab_biaya)
        elements.append(big_space)
        elements.append(catatan_title_par)
        for catatan in catatan_data:
            elements.append(Paragraph('* ' + catatan, par_style))
        elements.append(big_space)
        elements.append(waktu_tempat_par)
        elements.append(posisi_penanda_tangan_par)
        elements.append(big_space)
        elements.append(big_space)
        elements.append(big_space)
        elements.append(big_space)
        elements.append(nama_penanda_tangan_par)
        elements.append(nip_penanda_tangan_par)
        elements.append(big_space)
        elements.append(big_space)
        elements.append(big_space)
        elements.append(big_space)
        elements.append(big_space)
        elements.append(big_space)
        elements.append(big_space)
        elements.append(big_space)

        count=count+1

    doc.build(elements)
    return response

def export_pdf_konfirmasi_booking(request, peminjaman_id):
    # Set Response
    FILENAME = 'Konfirmasi_Booking_' + peminjaman_id;
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="' + FILENAME + '.pdf"'

    # Database
    peminjaman = get_object_or_404(PeminjamanKendaraan, pk=peminjaman_id)
    all_mobil = MobilPeminjaman.objects.filter(peminjaman_id=peminjaman_id)
    mobil = get_object_or_404(Mobil, pk=all_mobil[0].mobil_id)

    # Content
    title_booking = 'BOOKING KENDARAAN'
    booking = [['No. Booking', peminjaman_id + '/BK/TR/2018'],
               ['Tanggal Booking', getTanggal(peminjaman.tanggal_booking)],
               ['Jenis Kendaraan', mobil.jenis],
               ['Sebanyak', len(all_mobil)],
               ['Rencana Tanggal Pemakaian', getTanggal(peminjaman.tanggal_pemakaian) + ' s.d. ' + getTanggal(peminjaman.tanggal_pengembalian)],
               ['Asal', peminjaman.tempat_berkumpul],
               ['Tujuan', peminjaman.tujuan],
               ['Acara', peminjaman.acara],
               ['Nama Pengguna/No. Kontak', peminjaman.nama_peminjam + '/' + peminjaman.no_telp_peminjam]]

    title_biaya = 'RINCIAN PERKIRAAN BIAYA PERJALANAN'
    biaya = [['Biaya Perawatan (Rp.)', peminjaman.biaya_perawatan],
             ['BBM (Rp.)', peminjaman.biaya_bbm],
             ['Uang Lelah Sopir (Rp.)', peminjaman.biaya_supir],
             ['Tol (Rp.)', peminjaman.biaya_tol],
             ['Parkir (Rp.)', peminjaman.biaya_parkir],
             ['Penginapan (Rp.)', peminjaman.biaya_penginapan],
             ['Jumlah Total (Rp.)', peminjaman.getTotalBiaya()]]
    for entry in biaya:
        entry[1] = '{:,}'.format(entry[1]) # Thousands comma delimiter

    catatan_title = 'Catatan:'
    catatan_data = ['Perincian biaya ini sifatnya tidak baku, bisa berubah sesuai rundown terakhir.',
                'Perincian biaya ini bukan merupakan alat bukti pembayaran.',
                'Bilamana sudah fix dan sepakat silahkan buatkan Surat Permohonan Peminjaman Kendaraan ditujukan kepada Direktur Sarana dan Prasarana ITB.',
                'Mengambil Formulir Persetujuan Peminjaman, yang telah ditandatangani/disetujui oleh Direktur Sarana dan Prasarana ITB.',
                'Mekanisme pembayaran (Nilai Nominal dan No. Rekening Pembayaran) akan tertera pada Formulir Persetujuan Peminjaman.']

    waktu_tempat = 'Bandung, ' + getTanggal(datetime.today())
    posisi_penanda_tangan = 'Kepala Seksi Transportasi'
    nama_penanda_tangan = 'Ade Sumarna'
    nip_penanda_tangan = 'NIP. 197810272014091004'

    # Setup
    elements = []
    doc = SimpleDocTemplate(response, pagesize=letter)
    big_space = Spacer(1, 0.2*inch)
    small_space = Spacer(1, 0.05*inch)

    # Size
    TAB_WIDTH = 3.2
    TAB_HEIGHT = 0.3
    COL_NUM = 2
    BOOKING_ROW = len(booking)
    BIAYA_ROW = len(biaya)

    # Style
    tab_style = TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black)
        ])
    title_style = ParagraphStyle(
                name='Normal',
                fontName='Helvetica-Bold',
                fontSize=12,
            )
    par_style = ParagraphStyle(
                name='Normal',
                fontName='Helvetica',
                fontSize=9,
            )
    par_right_style = ParagraphStyle(
                name='Normal',
                fontName='Helvetica',
                fontSize=10,
                alignment=TA_RIGHT,
            )
    par_right_bold_style = ParagraphStyle(
                name='Normal',
                fontName='Helvetica-Bold',
                fontSize=10,
                alignment=TA_RIGHT,
            )

    # Elements
    title_booking_par = Paragraph(title_booking, title_style)
    tab_booking = Table(booking, COL_NUM*[TAB_WIDTH*inch], BOOKING_ROW*[TAB_HEIGHT*inch])
    tab_booking.setStyle(tab_style)
    title_biaya_par = Paragraph(title_biaya, title_style)
    tab_biaya = Table(biaya, COL_NUM*[TAB_WIDTH*inch], BIAYA_ROW*[TAB_HEIGHT*inch])
    tab_biaya.setStyle(tab_style)
    catatan_title_par = Paragraph(catatan_title, par_style)
    waktu_tempat_par = Paragraph(waktu_tempat, par_right_style)
    posisi_penanda_tangan_par = Paragraph(posisi_penanda_tangan, par_right_style)
    nama_penanda_tangan_par = Paragraph(nama_penanda_tangan, par_right_bold_style)
    nip_penanda_tangan_par = Paragraph(nip_penanda_tangan, par_right_style)

    # Append
    elements.append(title_booking_par)
    elements.append(small_space)
    elements.append(tab_booking)
    elements.append(big_space)
    elements.append(title_biaya_par)
    elements.append(small_space)
    elements.append(tab_biaya)
    elements.append(big_space)
    elements.append(catatan_title_par)
    for catatan in catatan_data:
        elements.append(Paragraph('* ' + catatan, par_style))
    elements.append(big_space)
    elements.append(waktu_tempat_par)
    elements.append(posisi_penanda_tangan_par)
    elements.append(big_space)
    elements.append(big_space)
    elements.append(big_space)
    elements.append(big_space)
    elements.append(nama_penanda_tangan_par)
    elements.append(nip_penanda_tangan_par)


    doc.build(elements)
    return response

def download_report(request, month, year):
    all_kendaraan = Mobil.objects.all()
    all_peminjaman = PeminjamanKendaraan.objects.all()
    for peminjaman in all_peminjaman:
    	peminjam = get_object_or_404(Peminjam, pk=peminjaman.peminjam_id)
    	setattr(peminjaman, 'nama_peminjam', peminjam.nama)
    	setattr(peminjaman, 'bagian_jurusan_peminjam', peminjam.bagian_jurusan)
    	supir = get_object_or_404(Supir, pk=peminjaman.supir_id)
    	setattr(peminjaman, 'nama_supir', supir.nama)

    filename = 'Report_'+month+'-'+year

    data = []
    # header
    header = ['No', 'Jenis Kendaraan', 'Nama Kendaraan', 'Nopol', 'Pengemudi']
    for i in range(1, 32):
        header.append(i)
    data.append(header)
    # body
    count = 1
    if len(str(month)) == 1:
        month = '0'+str(month)
    for kendaraan in all_kendaraan:
        supir = get_object_or_404(Supir, pk=kendaraan.supir_id)
        item = [str(count), kendaraan.jenis, kendaraan.nama, kendaraan.no_polisi, supir.nama]
        for day in range(1, 32):
            text = ''
            if day < 10:
                day = '0'+str(day)
            for peminjaman in all_peminjaman:
                if peminjaman.tanggal_pemakaian.strftime('%m') == month \
                            and peminjaman.tanggal_pemakaian.strftime('%Y') == year:
                    if peminjaman.mobil_id == kendaraan.id:
                        if str(day) == peminjaman.tanggal_pemakaian.strftime('%d'):
                            text = 'Pengguna: '+peminjaman.nama_peminjam+'('+peminjaman.bagian_jurusan_peminjam+')'+' Tujuan: '+peminjaman.tujuan+' Pengemudi: '+peminjaman.nama_supir
            item.append(text)
        data.append(item)
        count += 1
    return excel.make_response_from_array(
        data, 'xlsx', file_name=filename)

def download_peminjaman_report(request, month, year):
    all_kendaraan = Mobil.objects.all()
    for kendaraan in all_kendaraan:
        setattr(kendaraan, 'nama_supir', get_object_or_404(Supir, pk=kendaraan.supir_id).nama)
    all_peminjaman = PeminjamanKendaraan.objects.all()
    for peminjaman in all_peminjaman:
        peminjam = get_object_or_404(Peminjam, pk=peminjaman.peminjam_id)
        setattr(peminjaman, 'nama_peminjam', peminjam.nama)
        setattr(peminjaman, 'bagian_jurusan_peminjam', peminjam.bagian_jurusan)
        supir = get_object_or_404(Supir, pk=peminjaman.supir_id)
        setattr(peminjaman, 'nama_supir', supir.nama)

    filename = 'Report_'+month+'-'+year

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename='+ filename +'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("%s %s" % (intToMonth(int(month)), year))

    header_font = xlwt.XFStyle()
    header_font.alignment.horz = header_font.alignment.HORZ_CENTER

    borders = xlwt.Borders()
    borders.left = xlwt.Borders.THIN
    borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN

    header_font.borders = borders

    ws.write(0,0, 'No', header_font)
    ws.write(0,1, 'Jenis Kendaraan', header_font)
    ws.write(0,2, 'Nama Kendaraan', header_font)
    ws.write(0,3, 'Nopol', header_font)
    ws.write(0,4, 'Pengemudi', header_font)

    days = monthrange(int(year), int(month))[1]
    i = 1
    while i < days+1:
        ws.write(0,i+4, str(i), header_font)
        i += 1

    content_font = xlwt.XFStyle()
    content_font.borders = borders

    i = 1
    for kendaraan in all_kendaraan:
        ws.write(i, 0, str(i), content_font)
        ws.write(i, 1, kendaraan.jenis, content_font)
        ws.write(i, 2, kendaraan.nama, content_font)
        ws.write(i, 3, kendaraan.no_polisi, content_font)
        ws.write(i, 4, kendaraan.nama_supir, content_font)
        day = 1
        while day < days+1:
            hit = False
            for peminjaman in all_peminjaman:
                # a = int(peminjaman.tanggal_pemakaian.strftime('%m'))
                # b = int(peminjaman.tanggal_pemakaian.strftime('%Y'))
                if peminjaman.mobil_id == kendaraan.id and int(peminjaman.tanggal_pemakaian.strftime('%d')) == day \
                    and int(peminjaman.tanggal_pemakaian.strftime('%m')) == int(month) \
                    and int(peminjaman.tanggal_pemakaian.strftime('%Y')) == int(year):
                    hit = True
            if not hit:
                ws.write(i, day+4, '', content_font)
            else:
                text = 'Pengguna: '+peminjaman.nama_peminjam+'('+peminjaman.bagian_jurusan_peminjam+')'+' Tujuan: '+peminjaman.tujuan+' Pengemudi: '+peminjaman.nama_supir
                ws.write(i, day+4, text, content_font)
            day += 1
        i += 1


    wb.save(response)
    return response


def format(time):
    return str(time)

def download_car_report(request, kendaraan_id):

    mobil = get_object_or_404(Mobil, pk=kendaraan_id)

    peminjaman = PeminjamanKendaraan.objects.filter(mobil_id=mobil.id).exclude(status=3)

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=report_'+ mobil.nama +'.xls'
    wb = xlwt.Workbook(encoding='utf-8')

    for month in range(1, 13):
        ws = wb.add_sheet(intToMonth(month))

        row_num = 0

        #####################
        # HEADER FILE
        ####################
        ws.write_merge(0, 0, 0, 15, "LEMBAR KENDALI KENDARAAN OPERASIONAL ITB")
        ws.write_merge(2, 2, 0, 15, "Bulan : " + intToMonth(month))
        ws.write_merge(3, 3, 0, 15, "Jenis Kendaraan : " + mobil.nama)
        ws.write_merge(4, 4, 0, 15, "Nopol : " + mobil.no_polisi)
        row_num += 6
        ####### end header file ######

        #####################
        # HEADER TABEL
        ####################
        header_font = xlwt.XFStyle()
        header_font.alignment.horz = header_font.alignment.HORZ_CENTER

        borders = xlwt.Borders()
        borders.left = xlwt.Borders.THIN
        borders.right = xlwt.Borders.THIN
        borders.top = xlwt.Borders.THIN
        borders.bottom = xlwt.Borders.THIN

        header_font.borders = borders

        ws.write_merge(6, 8, 0, 0, "No", header_font)
        ws.col(0).width = (len("No. ")*367)

        ws.write_merge(6, 6, 1, 2, "Pemesanan", header_font)
        ws.write_merge(7, 8, 1, 1, "Hari", header_font)
        ws.col(1).width = (len("Minggu--")*367)
        ws.write_merge(7, 8, 2, 2, "Tanggal", header_font)
        ws.col(2).width = (len("33 Desember 20")*367)

        ws.write_merge(6, 6, 3, 8, "Pelaksanaan", header_font)
        ws.write_merge(7, 8, 3, 3, "Hari", header_font)
        ws.col(3).width = (len("Minggu--")*367)
        ws.write_merge(7, 8, 4, 4, "Tanggal", header_font)
        ws.col(4).width = (len("33 Desember 20")*367)
        ws.write_merge(7, 8, 5, 5, "Nama Pemohon", header_font)
        ws.col(5).width = (len("Nama Pemohon Pemohon")*367)
        ws.write_merge(7, 8, 6, 6, "Unit/Alamat", header_font)
        ws.col(6).width = (len("UnitAlamat")*367)
        ws.write_merge(7, 8, 7, 7, "Tujuan", header_font)
        ws.col(7).width = (len("Tujuan---")*367)
        ws.write_merge(7, 8, 8, 8, "Nama Pengemudi", header_font)
        ws.col(8).width = (len("Nama Pengemudi")*367)

        ws.write_merge(6, 6, 9, 12, "Kendaraan", header_font)
        ws.write_merge(7, 7, 9, 10, "Waktu", header_font)
        #ws.col(7).width = (len("Waktu")*367)
        ws.write_merge(7, 7, 11, 12, "Posisi Odometer", header_font)
        #ws.col().width = (len("Posisi Odometer")*367)
        ws.write_merge(8, 8, 9, 9, "Berangkat", header_font)
        ws.col(9).width = (len("33 Desember 20")*367)
        ws.write_merge(8, 8, 10, 10, "Datang", header_font)
        ws.col(10).width = (len("33 Desember 20")*367)
        ws.write_merge(8, 8, 11, 11, "Awal", header_font)
        ws.col(11).width = (len("--Awal--")*367)
        ws.write_merge(8, 8, 12, 12, "Akhir", header_font)
        ws.col(12).width = (len("--Awal--")*367)

        ws.write_merge(6, 6, 13, 14, "Bukti Biaya Perawatan", header_font)
        #ws.col(11).width = (len("Bukti Biaya Perawatan")*367)
        ws.write_merge(7, 8, 13, 13, "Ada", header_font)
        ws.col(13).width = (len("Ada Ada")*367)
        ws.write_merge(7, 8, 14, 14, "Tidak", header_font)
        ws.col(14).width = (len("Ada Ada")*367)

        ws.write_merge(6, 8, 15, 15, "Nomor Surat", header_font)
        ws.col(15).width = (len("Nomor Surat")*367)
        ws.write_merge(6, 8, 16, 16, "Tanggal Surat", header_font)
        ws.col(16).width = (len("Tanggal Surat")*367)

        ws.write_merge(6, 8, 17, 17, "Keterangan", header_font)
        ws.col(17).width = (len("Keterangan")*367)
        ##### end header table #######

        #############################
        # CONTENT
        ############################
        content_font = xlwt.XFStyle()
        content_font.borders = borders
        row_num = 9
        no = 1

        for pinjam in peminjaman:

            bulan_pinjam = pinjam.tanggal_pemakaian.strftime('%B')
            if pinjam.bukti_transfer == 0:
                ada = ''
                tidak_ada = 'v'
            else:
                ada = 'v'
                tidak_ada = ''

            if int(mapMonth(bulan_pinjam)) == month :

                supir = get_object_or_404(Supir, pk=pinjam.supir_id)
                peminjam = get_object_or_404(Peminjam, pk=pinjam.peminjam_id)

                day_pemesanan = datetime.strptime(pinjam.tanggal_booking.strftime('%d %B %Y'), '%d %B %Y').strftime('%A')
                day_pelaksanaan = datetime.strptime(pinjam.tanggal_pemakaian.strftime('%d %B %Y'), '%d %B %Y').strftime('%A')

                ws.write(row_num, 0, no, content_font)  # No

                ws.write(row_num, 1, dayToHari(day_pemesanan), content_font)  # Hari
                ws.write(row_num, 2, pinjam.tanggal_booking.strftime('%d %B %Y'), content_font)  # Tanggal

                ws.write(row_num, 3, dayToHari(day_pelaksanaan), content_font)  # Hari
                ws.write(row_num, 4, pinjam.tanggal_pemakaian.strftime('%d %B %Y'), content_font)  # Tanggal
                ws.write(row_num, 5, peminjam.nama, content_font)  # Nama Pemohon
                ws.write(row_num, 6, peminjam.bagian_jurusan, content_font)  # Unit / Alamat
                ws.write(row_num, 7, pinjam.tujuan, content_font)  # Tujuan
                ws.write(row_num, 8, supir.nama, content_font)  # Nama Pengemudi

                ws.write(row_num, 9, format(pinjam.waktu_berangkat), content_font)  # Waktu : Berangkat
                ws.write(row_num, 10, format(pinjam.waktu_datang), content_font)  # Waktu : Datang
                ws.write(row_num, 11, pinjam.odometer_sebelum, content_font)  # Odometer : Awal
                ws.write(row_num, 12, pinjam.odometer_sesudah, content_font)  # Odometer : Akhir

                ws.write(row_num, 13, ada, content_font)  # Perawatan : Ada
                ws.write(row_num, 14, tidak_ada, content_font)  # Perawatan : Tidak

                ws.write(row_num, 15, pinjam.no_surat, content_font)  # Nomor Surat
                ws.write(row_num, 16, pinjam.tanggal_surat.strftime('%d %B %Y'), content_font)  # Tanggal Surat
                ws.write(row_num, 17, pinjam.keterangan, content_font)  # Keterangan

                no += 1
                row_num += 1

    wb.save(response)
    return response

def cek(request):
    tanggal_pemakaian = request.POST['date']
    year = tanggal_pemakaian.replace(',', '').split(' ')[2]
    month = mapMonth(tanggal_pemakaian.replace(',', '').split(' ')[1])
    day = tanggal_pemakaian.replace(',', '').split(' ')[0]
    if len(day) == 1:
        day = '0'+day
    date = year+'-'+month+'-'+day+' 00:00Z'
    mobil_id = request.POST['mobil_id']
    all_peminjaman = MobilPeminjaman.objects.filter(mobil_id=mobil_id);
    for peminjaman in all_peminjaman:
        detail_peminjaman = PeminjamanKendaraan.filter(pk=peminjaman.peminjaman_id, tanggal_pemakaian=date).exclude(status=3)
        if len(detail_peminjaman)>0:
            return HttpResponse("False")
    return HttpResponse("True")

def mapMonth(name):
	if name == "Januari":
		return '01'
	elif name == "Februari":
		return '02'
	elif name == "Maret":
		return '03'
	elif name == "April":
		return '04'
	elif name == "Mei":
		return '05'
	elif name == "Juni":
		return '06'
	elif name == "Juli":
		return '07'
	elif name == "Agustus":
		return '08'
	elif name == "September":
		return '09'
	elif name == "Oktober":
		return '10'
	elif name == "November":
		return '11'
	elif name == "Desember":
		return '12'

def intToMonth(bulan):
	if bulan == 1:
		return "Januari"
	elif bulan == 2:
		return "Februari"
	elif bulan == 3:
		return "Maret"
	elif bulan == 4:
		return "April"
	elif bulan == 5:
		return "Mei"
	elif bulan == 6:
		return "Juni"
	elif bulan == 7:
		return "Juli"
	elif bulan == 8:
		return "Agustus"
	elif bulan == 9:
		return "September"
	elif bulan == 10:
		return "Oktober"
	elif bulan == 11:
		return "November"
	elif bulan == 12:
		return "Desember"

def dayToHari(day):
	if day == "Sunday":
		return "Minggu"
	elif day == "Monday":
		return "Senin"
	elif day == "Tuesday":
		return "Selasa"
	elif day == "Wednesday":
		return "Rabu"
	elif day == "Thursday":
		return "Kamis"
	elif day == "Friday":
		return "Jum'at"
	elif day == "Saturday":
		return "Sabtu"

def getTanggal(date):
    tanggal = ''
    tanggal += str(date.strftime('%d') + ' ')
    tanggal += str(intToMonth(int(date.strftime('%m'))) + ' ')
    tanggal += str(date.strftime('%Y'))
    return tanggal
