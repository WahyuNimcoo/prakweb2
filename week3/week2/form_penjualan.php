<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Belanja Online</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"> 
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
    <div class="container">
        <br>
        <h3>Belanja Online</h3>
        <hr>
        <div class="row">
            <div class="col-md-12">
                <div class="row">
                    <div class="col-md-8">
                        <form method="POST" action="form_penjualan.php">
                            <div class="form-group row">
                                <label for="customer" class="col-4 col-form-label">Customer</label> 
                                <div class="col-8">
                                <input id="customer" name="customer" type="text" class="form-control">
                                </div>
                            </div>
                            <div class="form-group row">
                                <label class="col-4">Pilih Produk</label> 
                                <div class="col-8">
                                <div class="custom-control custom-radio custom-control-inline">
                                    <input name="produk" id="produk_0" type="radio" class="custom-control-input" value="TV"> 
                                    <label for="produk_0" class="custom-control-label">TV</label>
                                </div>
                                <div class="custom-control custom-radio custom-control-inline">
                                    <input name="produk" id="produk_1" type="radio" class="custom-control-input" value="Kulkas"> 
                                    <label for="produk_1" class="custom-control-label">Kulkas</label>
                                </div>
                                <div class="custom-control custom-radio custom-control-inline">
                                    <input name="produk" id="produk_2" type="radio" class="custom-control-input" value="Mesin Cuci"> 
                                    <label for="produk_2" class="custom-control-label">Mesin Cuci</label>
                                </div>
                                </div>
                            </div>
                            <div class="form-group row">
                                <label for="jumlah" class="col-4 col-form-label">Jumlah</label> 
                                <div class="col-8">
                                <input id="jumlah" name="jumlah" placeholder="Jumlah" type="text" class="form-control">
                                </div>
                            </div> 
                            <div class="form-group row">
                                <div class="offset-4 col-8">
                                <input type="submit" value="Simpan" name="proses" class="btn btn-success">
                                </div>
                            </div>
                        </form>
                    </div>
                    <div class="col-md-4">
                        <ul class="list-group">
                            <li class="list-group-item active" aria-current="true">Daftar Harga</li>
                            <li class="list-group-item">TV : Rp. 4.200.000</li>
                            <li class="list-group-item">Kulkas : Rp. 3.100.000</li>
                            <li class="list-group-item">Mesin Cuci : Rp. 3.800.000</li>
                            <li class="list-group-item active">Harga Dapat Berubah Setiap Saat</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
        <hr>
        <?php
        // Mengambil data yang telah diinput oleh customer
        // error_reporting(0);
        require_once 'fungsi2.php';
        // $proses = $_POST ['proses'];
        $nama_customer = $_POST ['customer'];
        $pilih_produk = $_POST ['produk'];
        $jumlah_beli = $_POST  ['jumlah'];
        $hasil = harga($pilih_produk, $jumlah_beli);

        //Memilih produk yang diinginkan dan membuat perhitungannya
        
    
        //Mencetak data yang diambil ke dalam browser
            echo " Nama Customer : $nama_customer";
            echo "<br/>Produk Pilihan : $pilih_produk";
            echo "<br/>Jumlah Beli : $jumlah_beli";
            echo "<br/>Total Belanja : "  ."Rp. " .number_format($hasil, 2, ",", "."). ",-" ;

        ?>

</body>
</html>