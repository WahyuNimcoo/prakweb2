<?php
require_once 'dbkoneksi.php';
?>
<?php
$_kode = $_POST['kode'];
$_nama = $_POST['nama'];
$_jk = $_POST['jk'];
$_tmp_lahir = $_POST['tmp_lahir'];
$_tgl_lahir = $_POST['tgl_lahir'];
$_email = $_POST['email'];
$_kartu = $_POST['kartu_id'];

$_proses = $_POST['proses'];

// array data
$ar_data[] = $_POST['kode'];
$ar_data[] = $_POST['nama'];
$ar_data[] = $_POST['jk'];
$ar_data[] = $_POST['tmp_lahir'];
$ar_data[] = $_POST['tgl_lahir'];
$ar_data[] = $_POST['email'];
$ar_data[] = $_POST['kartu_id'];

if ($_proses == "Simpan") {
   // data baru
   $sql = "INSERT INTO pelanggan (kode,nama,jk,tmp_lahir,tgl_lahir,
    email,kartu_id) VALUES (?,?,?,?,?,?,?)";
} else if ($_proses == "Update") {
   $ar_data[] = $_POST['idedit']; // ? 8
   $sql = "UPDATE pelanggan SET kode=?,nama=?,jk=?,tmp_lahir=?,
    tgl_lahir=?,email=?,kartu_id=? WHERE id=?";
}
if (isset($sql)) {
   $st = $dbh->prepare($sql);
   $st->execute($ar_data);
}

header('location:list_pelanggan.php');
?>