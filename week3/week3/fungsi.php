<?php
function grade($nilai){
    if ($nilai >= 150){
        return "Sangat Baik";
    }elseif ($nilai >= 60){
        return "Baik";
    }elseif ($nilai >= 40){
        return "Cukup";
    }elseif ($nilai >= 0){
        return "Kurang";
    }else{
        return "0(Tidak Memadai)";
    }
}
?> 