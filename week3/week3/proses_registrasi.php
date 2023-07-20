<?php
//ambil data yang di inputkan oleh user 
require_once 'fungsi.php';
$submit = $_POST["submit"];
$nama = $_POST['nama'];
$nim = $_POST['nim'];
$jk = $_POST['jk'];
$studi = $_POST['studi'];
$skill = $_POST['skill'];
$email = $_POST['email'];

$nilai = 0;
foreach ($skill as $value){
        switch ($value){
            case 'html' :
                $nilai += 10;
                break;
            case 'css' :
                $nilai += 10;
                break;
            case 'javascript' :
                $nilai += 20;
                break;
            case 'javascript' :
                $nilai += 20;
                break;
            case 'Bootstrap' :
                $nilai += 20;
                break;
            case 'php' :
                $nilai += 30;
                break;
            case 'python' :
                $nilai += 30;
                break;
            case 'java' :
                $nilai += 50;
                break;
            default :
                $nilai += 0;
                break;

        }
    }
$grade = grade($nilai);

//cetak data yang telah diambil kedalam browser 

echo "<h4>Hasil Register: </h4>";
echo "<br/>Nama : $nama ";
echo "<br/>NIM : $nim ";
echo "<br/>Jenis Kelamin : $jk ";
echo "<br/>Program : $studi ";
echo "<br/>Skill :  ";
foreach ($skill as $value) {
    echo $value . ",";
}
echo "<br/>Skor Nilai : $nilai";
echo "<br/> Kategori Skill : $grade";
echo "<br/>email : $email";
echo "<br/>Data Telah di simpan $submit";


?>
