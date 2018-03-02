from django.conf.urls import url

from . import views

urlpatterns = [
	###################################################################################################################
	#
	# URL DASHBOARD
	#
	###################################################################################################################
	# ex:/
	url(r'^$', views.index, name='index'),

	###################################################################################################################
	#
	# URL TATACARA
	#
	###################################################################################################################
	# ex:/tatacara
	url(r'^tatacara/$', views.tatacara, name='tatacara'),

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
    # ex: /peminjaman/5/uploadFoto
    url(r'^peminjaman/(?P<peminjaman_id>[0-9]+)/uploadFoto/$', views.uploadBuktiTransfer, name='uploadBuktiTransfer'),
	# ex: /peminjaman/5/uploadFormAkhir
    url(r'^peminjaman/(?P<peminjaman_id>[0-9]+)/uploadFormAkhir/$', views.uploadFormAkhir, name='uploadFormAkhir'),
    # ex: /peminjaman/5/deleteFoto
    url(r'^peminjaman/(?P<peminjaman_id>[0-9]+)/deleteFoto/$', views.deleteBuktiTransfer, name='deleteBuktiTransfer'),
	# ex: /peminjaman/5/deleteFormAkhir
    url(r'^peminjaman/(?P<peminjaman_id>[0-9]+)/deleteFormAkhir/$', views.deleteFormAkhir, name='deleteFormAkhir'),

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
    # url(r'^kendaraan/(?P<kendaraan_id>[0-9]+)/delete/$', views.kendaraanDelete, name='kendaraanDelete'),
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

	url(r'^download_report/(?P<month>[0-9]+)/(?P<year>[0-9]+)/$', views.download_peminjaman_report, name='download_report'),
	url(r'^download_car_report/(?P<kendaraan_id>[0-9]+)/$', views.download_car_report, name='download_car_report'),
	url(r'^cek/$', views.cek, name='cek'),
]
