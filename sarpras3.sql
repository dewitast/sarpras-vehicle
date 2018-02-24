-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 25, 2017 at 01:09 PM
-- Server version: 10.1.21-MariaDB
-- PHP Version: 7.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sarpras3`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add mobil', 1, 'add_mobil'),
(2, 'Can change mobil', 1, 'change_mobil'),
(3, 'Can delete mobil', 1, 'delete_mobil'),
(4, 'Can add telepon peminjam', 2, 'add_teleponpeminjam'),
(5, 'Can change telepon peminjam', 2, 'change_teleponpeminjam'),
(6, 'Can delete telepon peminjam', 2, 'delete_teleponpeminjam'),
(7, 'Can add peminjam', 3, 'add_peminjam'),
(8, 'Can change peminjam', 3, 'change_peminjam'),
(9, 'Can delete peminjam', 3, 'delete_peminjam'),
(10, 'Can add telepon supir', 4, 'add_teleponsupir'),
(11, 'Can change telepon supir', 4, 'change_teleponsupir'),
(12, 'Can delete telepon supir', 4, 'delete_teleponsupir'),
(13, 'Can add supir', 5, 'add_supir'),
(14, 'Can change supir', 5, 'change_supir'),
(15, 'Can delete supir', 5, 'delete_supir'),
(16, 'Can add peminjaman kendaraan', 6, 'add_peminjamankendaraan'),
(17, 'Can change peminjaman kendaraan', 6, 'change_peminjamankendaraan'),
(18, 'Can delete peminjaman kendaraan', 6, 'delete_peminjamankendaraan'),
(19, 'Can add log entry', 7, 'add_logentry'),
(20, 'Can change log entry', 7, 'change_logentry'),
(21, 'Can delete log entry', 7, 'delete_logentry'),
(22, 'Can add permission', 8, 'add_permission'),
(23, 'Can change permission', 8, 'change_permission'),
(24, 'Can delete permission', 8, 'delete_permission'),
(25, 'Can add user', 9, 'add_user'),
(26, 'Can change user', 9, 'change_user'),
(27, 'Can delete user', 9, 'delete_user'),
(28, 'Can add group', 10, 'add_group'),
(29, 'Can change group', 10, 'change_group'),
(30, 'Can delete group', 10, 'delete_group'),
(31, 'Can add content type', 11, 'add_contenttype'),
(32, 'Can change content type', 11, 'change_contenttype'),
(33, 'Can delete content type', 11, 'delete_contenttype'),
(34, 'Can add session', 12, 'add_session'),
(35, 'Can change session', 12, 'change_session'),
(36, 'Can delete session', 12, 'delete_session'),
(37, 'Can add foto mobil', 13, 'add_fotomobil'),
(38, 'Can change foto mobil', 13, 'change_fotomobil'),
(39, 'Can delete foto mobil', 13, 'delete_fotomobil');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$30000$DIKLVeDC7ViJ$B3+EfM3GxbOoKT5Nu4oGKxOAg99SvYVXWXmtAgU+ooY=', '2017-04-25 10:31:30.556000', 1, 'admin', '', '', 'admin@sarpras.com', 1, 1, '2017-04-25 02:23:08.586000');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(7, 'admin', 'logentry'),
(10, 'auth', 'group'),
(8, 'auth', 'permission'),
(9, 'auth', 'user'),
(11, 'contenttypes', 'contenttype'),
(13, 'peminjaman', 'fotomobil'),
(1, 'peminjaman', 'mobil'),
(3, 'peminjaman', 'peminjam'),
(6, 'peminjaman', 'peminjamankendaraan'),
(5, 'peminjaman', 'supir'),
(2, 'peminjaman', 'teleponpeminjam'),
(4, 'peminjaman', 'teleponsupir'),
(12, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2017-04-06 05:10:48.612000'),
(2, 'auth', '0001_initial', '2017-04-06 05:10:58.476000'),
(3, 'admin', '0001_initial', '2017-04-06 05:11:00.926000'),
(4, 'admin', '0002_logentry_remove_auto_add', '2017-04-06 05:11:00.973000'),
(5, 'contenttypes', '0002_remove_content_type_name', '2017-04-06 05:11:02.395000'),
(6, 'auth', '0002_alter_permission_name_max_length', '2017-04-06 05:11:03.551000'),
(7, 'auth', '0003_alter_user_email_max_length', '2017-04-06 05:11:04.348000'),
(8, 'auth', '0004_alter_user_username_opts', '2017-04-06 05:11:04.395000'),
(9, 'auth', '0005_alter_user_last_login_null', '2017-04-06 05:11:04.910000'),
(10, 'auth', '0006_require_contenttypes_0002', '2017-04-06 05:11:04.926000'),
(11, 'auth', '0007_alter_validators_add_error_messages', '2017-04-06 05:11:04.973000'),
(12, 'auth', '0008_alter_user_username_max_length', '2017-04-06 05:11:05.805000'),
(13, 'peminjaman', '0001_initial', '2017-04-06 05:11:14.696000'),
(14, 'peminjaman', '0002_auto_20170327_2234', '2017-04-06 05:11:17.182000'),
(15, 'sessions', '0001_initial', '2017-04-06 05:11:17.822000'),
(16, 'peminjaman', '0003_mobil_supir', '2017-04-25 03:43:58.532000'),
(17, 'peminjaman', '0004_fotomobil', '2017-04-25 03:43:59.548000'),
(18, 'peminjaman', '0005_auto_20170415_0544', '2017-04-25 03:43:59.595000'),
(19, 'peminjaman', '0006_peminjamankendaraan_foto_bukti_transfer', '2017-04-25 03:44:00.282000');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('elsznopwdg42mfxawmkjh6edqj7c0cbg', 'NjAwNGIzMzlhZmFiOTBlMTdhMGM2NTlhYmJhZmVlYjU5MTNmZmUyOTp7Il9hdXRoX3VzZXJfaGFzaCI6IjZmN2Y1ZDdmZmFmZTY2MzYwYTZlYWJkMmI0NWNlYjZlNWI4OGMyMTAiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2017-05-09 10:31:30.602000');

-- --------------------------------------------------------

--
-- Table structure for table `peminjaman_fotomobil`
--

CREATE TABLE `peminjaman_fotomobil` (
  `id` int(11) NOT NULL,
  `foto` varchar(100) NOT NULL,
  `mobil_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `peminjaman_mobil`
--

CREATE TABLE `peminjaman_mobil` (
  `id` int(11) NOT NULL,
  `no_polisi` varchar(100) NOT NULL,
  `jenis` varchar(100) NOT NULL,
  `kapasitas` int(11) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `supir_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `peminjaman_mobil`
--

INSERT INTO `peminjaman_mobil` (`id`, `no_polisi`, `jenis`, `kapasitas`, `nama`, `supir_id`) VALUES
(1, 'D 7001 DS', 'Kendaraan Titipan', 1, 'Bus AC Besar (LAPI)', 1),
(2, 'D 7188 AP', 'Kendaraan Titipan', 1, 'Bus KOIKA (STEI)', 2),
(3, 'D 7159 AP', 'Kendaraan Titipan', 1, 'Elf KOIKA (STEI)', 3),
(4, 'D 1787 LR', 'Kendaraan Operasional', 1, 'Kijang Toyota Innova 2009', 4),
(5, 'D 1828 GT', 'Kendaraan Operasional', 1, 'Kijang Toyota 2003', 5),
(6, 'D 1785 GT', 'Kendaraan Operasional', 1, 'Kijang Toyota 2003', 6),
(7, 'D 1039 HY', 'Kendaraan Operasional', 1, 'Toyota Avanza 2006', 7),
(8, 'D 7391 AK', 'Kendaraan Operasional', 1, 'Travelo KIA 2008', 26),
(9, 'D 8526 CR', 'Kendaraan Operasional', 1, 'Truk Engkel Mitsubishi 2004', 8),
(10, 'D 7045 AM', 'Kendaraan Operasional', 1, 'Bus AC Kecil HINO 2009', 10),
(11, 'D 7136 A', 'Kendaraan Operasional', 1, 'Bus Non AC Kecil Mitsubishi 2004', 11),
(12, 'D 7161 C', 'Kendaraan Operasional', 1, 'Bus AC Kecil HINO 2003', 12),
(13, 'D 7165 C', 'Kendaraan Operasional', 1, 'Bus AC Kecil HINO 2013', 13),
(14, 'D 99 PY', 'Kendaraan Operasional', 1, 'Toyota Camry', 14),
(15, 'D 1699 MX', 'Kendaraan Operasional', 1, 'Toyota Fortuner', 16),
(16, 'D 1472 AEE', 'Kendaraan Operasional', 1, 'Toyota Altis', 17),
(17, 'D 1754 AEA', 'Kendaraan Operasional', 1, 'Toyota Altis', 18),
(18, 'D 1760 AEA', 'Kendaraan Operasional', 1, 'Toyota Altis', 19),
(19, 'D 1752 AEA', 'Kendaraan Operasional', 1, 'Toyota Altis', 20),
(20, 'D 15 BB', 'Kendaraan Operasional', 1, 'Toyota Altis', 21),
(21, 'B 2166 SFX', 'Kendaraan Operasional', 1, 'Kijang Innova ', 22),
(22, 'D 1502 ACO', 'Kendaraan Operasional', 1, 'Kijang Innova ', 27),
(23, 'D 1470 AEE', 'Kendaraan Operasional', 1, 'Toyota Altis', 23),
(24, 'B 2134 SFX', 'Kendaraan Operasional', 1, 'Kijang Innova ', 24),
(25, 'D 1226 GD', 'Kendaraan Operasional', 1, 'Toyota Kijang', 25);

-- --------------------------------------------------------

--
-- Table structure for table `peminjaman_peminjam`
--

CREATE TABLE `peminjaman_peminjam` (
  `id` int(11) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `bagian_jurusan` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `peminjaman_peminjamankendaraan`
--

CREATE TABLE `peminjaman_peminjamankendaraan` (
  `id` int(11) NOT NULL,
  `bukti_transfer` int(11) NOT NULL,
  `no_surat` varchar(100) NOT NULL,
  `tanggal_surat` datetime(6) NOT NULL,
  `tanggal_booking` datetime(6) NOT NULL,
  `odometer_sebelum` double DEFAULT NULL,
  `odometer_sesudah` double DEFAULT NULL,
  `acara` varchar(100) NOT NULL,
  `tujuan` varchar(100) NOT NULL,
  `tanggal_pemakaian` datetime(6) NOT NULL,
  `tanggal_pengembalian` datetime(6) NOT NULL,
  `tempat_berkumpul` varchar(100) NOT NULL,
  `keterangan` varchar(200) NOT NULL,
  `mobil_id` int(11) NOT NULL,
  `peminjam_id` int(11) NOT NULL,
  `supir_id` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `foto_bukti_transfer` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `peminjaman_supir`
--

CREATE TABLE `peminjaman_supir` (
  `id` int(11) NOT NULL,
  `nama` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `peminjaman_supir`
--

INSERT INTO `peminjaman_supir` (`id`, `nama`) VALUES
(1, 'Sudrajat'),
(2, 'Agus'),
(3, 'Imanudin'),
(4, 'Rahman'),
(5, 'Subarna'),
(6, 'Uci Sanusi'),
(7, 'Wagio'),
(8, 'Komar Rasmana'),
(9, 'Undang'),
(10, 'Didin Kosidin'),
(11, 'Taryono'),
(12, 'Tjahya Mansyur'),
(13, 'Sudrajat'),
(14, 'Wawan Gunawan'),
(15, 'Rahman'),
(16, 'Harry Setiana'),
(17, 'Kurnaedi'),
(18, 'Tisna Senjaya'),
(19, 'Adin Ahmadi'),
(20, 'Abdul Kohar'),
(21, 'Sulaeman'),
(22, 'Joni Hoby'),
(23, 'Yadi Suryadi'),
(24, 'Didi Sardi'),
(25, 'Yadi Suharyadi'),
(26, 'Tedi Kusnaedi'),
(27, 'Solihin');

-- --------------------------------------------------------

--
-- Table structure for table `peminjaman_teleponpeminjam`
--

CREATE TABLE `peminjaman_teleponpeminjam` (
  `id` int(11) NOT NULL,
  `no_telepon` varchar(100) NOT NULL,
  `peminjam_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `peminjaman_teleponsupir`
--

CREATE TABLE `peminjaman_teleponsupir` (
  `id` int(11) NOT NULL,
  `no_telepon` varchar(100) NOT NULL,
  `supir_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `peminjaman_teleponsupir`
--

INSERT INTO `peminjaman_teleponsupir` (`id`, `no_telepon`, `supir_id`) VALUES
(1, '0', 1),
(2, '0', 2),
(3, '0', 3),
(4, '0', 4),
(5, '0', 5),
(6, '0', 6),
(7, '0', 7),
(8, '0', 8),
(9, '0', 9),
(10, '0', 10),
(11, '0', 11),
(12, '0', 12),
(13, '0', 13),
(14, '0', 14),
(15, '0', 15),
(16, '0', 16),
(17, '0', 17),
(18, '0', 18),
(19, '0', 19),
(20, '0', 20),
(21, '0', 21),
(22, '0', 22),
(23, '0', 23),
(24, '0', 24),
(25, '0', 25),
(26, '0', 26),
(27, '0', 27);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_de54fa62` (`expire_date`);

--
-- Indexes for table `peminjaman_fotomobil`
--
ALTER TABLE `peminjaman_fotomobil`
  ADD PRIMARY KEY (`id`),
  ADD KEY `peminjaman_fotomobil_mobil_id_60ed6d22_fk_peminjaman_mobil_id` (`mobil_id`);

--
-- Indexes for table `peminjaman_mobil`
--
ALTER TABLE `peminjaman_mobil`
  ADD PRIMARY KEY (`id`),
  ADD KEY `peminjaman_mobil_supir_id_f84b26f8_fk_peminjaman_supir_id` (`supir_id`);

--
-- Indexes for table `peminjaman_peminjam`
--
ALTER TABLE `peminjaman_peminjam`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `peminjaman_peminjamankendaraan`
--
ALTER TABLE `peminjaman_peminjamankendaraan`
  ADD PRIMARY KEY (`id`),
  ADD KEY `peminjaman_peminjamanke_mobil_id_ca9c4d2b_fk_peminjaman_mobil_id` (`mobil_id`),
  ADD KEY `peminjaman_peminj_peminjam_id_c8826d13_fk_peminjaman_peminjam_id` (`peminjam_id`),
  ADD KEY `peminjaman_peminjamanke_supir_id_661a9c7c_fk_peminjaman_supir_id` (`supir_id`);

--
-- Indexes for table `peminjaman_supir`
--
ALTER TABLE `peminjaman_supir`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `peminjaman_teleponpeminjam`
--
ALTER TABLE `peminjaman_teleponpeminjam`
  ADD PRIMARY KEY (`id`),
  ADD KEY `peminjaman_telepo_peminjam_id_3e5220c7_fk_peminjaman_peminjam_id` (`peminjam_id`);

--
-- Indexes for table `peminjaman_teleponsupir`
--
ALTER TABLE `peminjaman_teleponsupir`
  ADD PRIMARY KEY (`id`),
  ADD KEY `peminjaman_teleponsupir_supir_id_d00872e2_fk_peminjaman_supir_id` (`supir_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;
--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
--
-- AUTO_INCREMENT for table `peminjaman_fotomobil`
--
ALTER TABLE `peminjaman_fotomobil`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `peminjaman_mobil`
--
ALTER TABLE `peminjaman_mobil`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
--
-- AUTO_INCREMENT for table `peminjaman_peminjam`
--
ALTER TABLE `peminjaman_peminjam`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `peminjaman_peminjamankendaraan`
--
ALTER TABLE `peminjaman_peminjamankendaraan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `peminjaman_supir`
--
ALTER TABLE `peminjaman_supir`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;
--
-- AUTO_INCREMENT for table `peminjaman_teleponpeminjam`
--
ALTER TABLE `peminjaman_teleponpeminjam`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `peminjaman_teleponsupir`
--
ALTER TABLE `peminjaman_teleponsupir`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `peminjaman_fotomobil`
--
ALTER TABLE `peminjaman_fotomobil`
  ADD CONSTRAINT `peminjaman_fotomobil_mobil_id_60ed6d22_fk_peminjaman_mobil_id` FOREIGN KEY (`mobil_id`) REFERENCES `peminjaman_mobil` (`id`);

--
-- Constraints for table `peminjaman_mobil`
--
ALTER TABLE `peminjaman_mobil`
  ADD CONSTRAINT `peminjaman_mobil_supir_id_f84b26f8_fk_peminjaman_supir_id` FOREIGN KEY (`supir_id`) REFERENCES `peminjaman_supir` (`id`);

--
-- Constraints for table `peminjaman_peminjamankendaraan`
--
ALTER TABLE `peminjaman_peminjamankendaraan`
  ADD CONSTRAINT `peminjaman_peminj_peminjam_id_c8826d13_fk_peminjaman_peminjam_id` FOREIGN KEY (`peminjam_id`) REFERENCES `peminjaman_peminjam` (`id`),
  ADD CONSTRAINT `peminjaman_peminjamanke_mobil_id_ca9c4d2b_fk_peminjaman_mobil_id` FOREIGN KEY (`mobil_id`) REFERENCES `peminjaman_mobil` (`id`),
  ADD CONSTRAINT `peminjaman_peminjamanke_supir_id_661a9c7c_fk_peminjaman_supir_id` FOREIGN KEY (`supir_id`) REFERENCES `peminjaman_supir` (`id`);

--
-- Constraints for table `peminjaman_teleponpeminjam`
--
ALTER TABLE `peminjaman_teleponpeminjam`
  ADD CONSTRAINT `peminjaman_telepo_peminjam_id_3e5220c7_fk_peminjaman_peminjam_id` FOREIGN KEY (`peminjam_id`) REFERENCES `peminjaman_peminjam` (`id`);

--
-- Constraints for table `peminjaman_teleponsupir`
--
ALTER TABLE `peminjaman_teleponsupir`
  ADD CONSTRAINT `peminjaman_teleponsupir_supir_id_d00872e2_fk_peminjaman_supir_id` FOREIGN KEY (`supir_id`) REFERENCES `peminjaman_supir` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
