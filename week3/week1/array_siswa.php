<?php
//buatlah data nilai siswa dengan array assosiatif
$ns1 = ['id' => 1, 'nim' => '01101', 'uts' => 80, 'uas' => 84, 'tugas' => 78];
$ns2 = ['id' => 2, 'nim' => '01102', 'uts' => 81, 'uas' => 85, 'tugas' => 79];
$ns3 = ['id' => 3, 'nim' => '01103', 'uts' => 82, 'uas' => 86, 'tugas' => 80];

//simpan seluruh data variable array assosiatif ke dalam array indexing
$ar_nilai = [$ns1,$ns2,$ns3];


?>
<h3 style="text-align: center ;">Daftar Nama Siswa</h3>
<table border="1" width="100%">
    <tr>
        <th>NO</th>
        <th>NIM</th>
        <th>UTS</th>
        <th>UAS</th>
        <th>TUGAS</th>
        <th>NILAI AKHIR</th>
    </tr>
</thead>
<tbody>
    <?php
    $nomor = 1;
    foreach ($ar_nilai as $nilai){
        echo '<tr><td>' .$nomor. '</td>';
        echo '<td>'.$nilai['nim'].'</td>';
        echo '<td>'.$nilai['uts'].'</td>';
        echo '<td>'.$nilai['uas'].'</td>';
        echo '<td>'.$nilai['tugas'].'</td>';
        $nilai_akhir = ($nilai['uts'] + $nilai['uas'] + $nilai['tugas'])/3;
            echo '<td>'.number_format($nilai_akhir) .'</td>';
            echo '</tr>';
            $nomor++;
        }
        ?>
    </tbody>
</table>