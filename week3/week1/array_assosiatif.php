<<?php
//cara menulis array
//array indexing
$buah = ['Alpukat','Jeruk','Mangga','Pisang'];
//cara memanggil array indexing
echo $buah[2];

//cetak jumlah
echo '<br/>Jumlah Buah ' .count($buah);
echo "<ol>";
foreach($buah as $fruit){
    echo "<li>$fruit</li>";
}
echo "</ol>";

//=======================

//tambahkan buah baru ke dalam array
$buah[] = "Durian";

//ubah buah index ke 1
$buah[1] = "Apel";

//cetak seluruh buah
echo '<br/>Jumlah Buah ' .count($buah);
echo "<ol>";
foreach($buah as $buas){
    echo "<li>$buas</li>";
}
echo "</ol>";


?>