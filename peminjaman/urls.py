from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    ###################################################################################################################
    #
    # URL Home
    #
    ###################################################################################################################
    # ex:/
    url(r'^$',views.tatacara,name='index'),
	###################################################################################################################
	#
	# URL DASHBOARD
	#
	###################################################################################################################
	# ex:/dashboard
	url(r'^dashboard/$', views.index, name='dashboard'),

	###################################################################################################################
    #
	# URL TATACARA
	#
	###################################################################################################################
	# ex:/tatacara
    url(r'^tatacara/$', views.tatacara, name='tatacara'),
    # ex:/tatacara/edit
    url(r'^tatacara/edit$', views.tatacaraEditForm, name='tatacaraEditForm'),
    # ex:/tatacara/change
    url(r'^tatacara/change$', views.tatacaraEdit, name='tatacaraEdit'),

	###################################################################################################################
	#
	# URL PEMINJAMAN
	#
	###################################################################################################################
	# ex:/peminjaman
	url(r'^peminjaman/$', views.peminjaman, name='peminjaman'),
	# ex: /peminjaman/5/
    url(r'^peminjaman/(?P<peminjaman_id>[0-9]+)/$', views.peminjamanDetail, name='peminjamanDetail'),
    # ex: /peminjaman/form
    url(r'^peminjaman/form/$', views.peminjamanForm, name='peminjamanForm'),
    # ex: /peminjaman/create
    url(r'^peminjaman/create/$', views.peminjamanCreate, name='peminjamanCreate'),
    # ex: /peminjaman/5/edit
    url(r'^peminjaman/(?P<peminjaman_id>[0-9]+)/edit/$', views.peminjamanEditForm, name='peminjamanEditForm'),
    # ex: /peminjaman/5/change
    url(r'^peminjaman/(?P<peminjaman_id>[0-9]+)/change/$', views.peminjamanEdit, name='peminjamanEdit'),
    # ex: /peminjaman/5/delete
    url(r'^peminjaman/(?P<peminjaman_id>[0-9]+)/delete/$', views.peminjamanDelete, name='peminjamanDelete'),
    # ex: /peminjaman/5/cancel
    url(r'^peminjaman/(?P<peminjaman_id>[0-9]+)/cancel/$', views.peminjamanCancel, name='peminjamanCancel'),
    # ex: /peminjaman/5/uploadBukti
    url(r'^peminjaman/(?P<peminjaman_id>[0-9]+)/uploadBukti/$', views.uploadBuktiTransfer, name='uploadBuktiTransfer'),
    # ex: /peminjaman/5/deleteBukti
    url(r'^peminjaman/(?P<peminjaman_id>[0-9]+)/deleteBukti/$', views.deleteBuktiTransfer, name='deleteBuktiTransfer'),
    # ex: /peminjaman/5/formfinal
    url(r'^peminjaman/(?P<peminjaman_id>[0-9]+)/formfinal/$', views.peminjamanFormFinal, name='peminjamanFormFinal'),
    # ex; /peminjaman/5/formFinalEdit
    url(r'^peminjaman/(?P<peminjaman_id>[0-9]+)/formFinalEdit/$', views.formFinalEdit, name='formFinalEdit'),
    ###################################################################################################################
    #
    # URL SUPIR
    #
    ###################################################################################################################
    # ex:/supir
    url(r'^supir/$', views.supir, name='supir'),
    # ex: /supir/5/
    # url(r'^supir/(?P<supir_id>[0-9]+)/$', views.supirDetail, name='supirDetail'),
    # ex: /supir/form
    url(r'^supir/form/$', views.supirForm, name='supirForm'),
    # ex: /supir/create
    url(r'^supir/create/$', views.supirCreate, name='supirCreate'),
    # ex: /supir/5/edit
    url(r'^supir/(?P<supir_id>[0-9]+)/edit/$', views.supirEditForm, name='supirEditForm'),
    # ex: /supir/5/change
    url(r'^supir/(?P<supir_id>[0-9]+)/change/$', views.supirEdit, name='supirEdit'),
    # ex: /supir/5/delete
    # url(r'^supir/(?P<supir_id>[0-9]+)/delete/$', views.supirDelete, name='supirDelete'),

    ###################################################################################################################
	#
	# URL KENDARAAN
	#
	###################################################################################################################
	# ex: /kendaraan
    url(r'^kendaraan/$', views.kendaraan, name='kendaraan'),
    # ex: /kendaraan/5/
    url(r'^kendaraan/(?P<kendaraan_id>[0-9]+)/$', views.kendaraanDetail, name='kendaraanDetail'),
	# ex: /kendaraan/form
    url(r'^kendaraan/form/$', views.kendaraanForm, name='kendaraanForm'),
    # ex: /kendaraan/create
    url(r'^kendaraan/create/$', views.kendaraanCreate, name='kendaraanCreate'),
    # ex: /kendaraan/5/edit
    url(r'^kendaraan/(?P<kendaraan_id>[0-9]+)/edit/$', views.kendaraanEditForm, name='kendaraanEditForm'),
    # ex: /kendaraan/5/change
    url(r'^kendaraan/(?P<kendaraan_id>[0-9]+)/change/$', views.kendaraanEdit, name='kendaraanEdit'),
    # ex: /kendaraan/5/delete
    url(r'^kendaraan/(?P<kendaraan_id>[0-9]+)/delete/$', views.kendaraanDelete, name='kendaraanDelete'),
    # ex: /kendaraan/check
    url(r'^kendaraan/check/$', views.kendaraanCekKetersediaan, name='kendaraanCekKetersediaan'),
    # ex: /kendaraan/5/uploadFoto
    url(r'^kendaraan/(?P<kendaraan_id>[0-9]+)/uploadFoto/$', views.kendaraanUploadFoto, name='kendaraanUploadFoto'),
    # ex: /kendaraan/5/deleteFoto
    url(r'^kendaraan/(?P<kendaraan_id>[0-9]+)/deleteFoto/(?P<foto_id>[0-9]+)$', views.kendaraanDeleteFoto, name='kendaraanDeleteFoto'),

	###################################################################################################################
	#
	# AUTHENTICATION
	#
	###################################################################################################################
	url(r'^loginForm/$', views.loginForm, name='loginForm'),

    ###################################################################################################################
    #
    # REPORT / FORM
    #
    ###################################################################################################################
    url(r'^export/peminjaman/(?P<peminjaman_id>[0-9]+)/$', views.export_pdf_peminjaman, name='export_pdf_peminjaman'),
    url(r'^export/konfirmasi/(?P<peminjaman_id>[0-9]+)/$', views.export_pdf_konfirmasi_booking, name='export_pdf_konfirmasi_booking'),
    url(r'^export/surattugas/(?P<peminjaman_id>[0-9]+)/$', views.export_pdf_surat_tugas, name='export_pdf_surat_tugas'),
	url(r'^download_report/(?P<month>[0-9]+)/(?P<year>[0-9]+)/$', views.download_peminjaman_report, name='download_report'),
	url(r'^download_car_report/(?P<kendaraan_id>[0-9]+)/$', views.download_car_report, name='download_car_report'),
	url(r'^cek/$', views.cek, name='cek'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
