<?php
function harga ($pilih_produk, $jumlah_beli){
    if ($pilih_produk == "TV" ){
        return  $jumlah_beli * 4200000;
    }elseif ($pilih_produk == "Kulkas"){
        return  $jumlah_beli * 3100000;
    }elseif ($pilih_produk == "Mesin Cuci"){
        return  $jumlah_beli * 3800000;
    }else {
        return "tidak ada";
    }

}




?>