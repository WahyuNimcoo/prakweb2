<?php
include_once('navbar.php');
include_once('sidebar.php');
?>
<!--Ini untuk buka konten-->
<div class="content-wrapper">
    <!-- Content Header (Page header) -->
    <div class="content-header">
        <div class="container-fluid">
            <div class="row mb-2">
                <div class="col-sm-6">
                    <h1 class="m-0">Week 2</h1>
                </div><!-- /.col -->
                <div class="col-sm-6">
                    <ol class="breadcrumb float-sm-right">
                        <li class="breadcrumb-item"><a href="#">Home</a></li>
                        <li class="breadcrumb-item active">week 2</li>
                    </ol>
                </div><!-- /.col -->
            </div><!-- /.row -->
        </div><!-- /.container-fluid -->
    </div>
    <!-- /.content-header -->
    <section class="content">
        <div class="container">
            <form method="POST" action="">
                <div class="form-group row">
                    <label for="name" class="col-4 col-form-label">Nama Mahasiswa</label>
                    <div class="col-8">
                        <input id="name" name="name" placeholder="Masukkan Nama anda" type="text" class="form-control">
                    </div>
                </div>
                <div class="form-group row">
                    <label for="matkul" class="col-4 col-form-label">Mata Kuliah</label>
                    <div class="col-8">
                        <select id="matkul" name="matkul" class="custom-select">
                            <option value="DDP">Dasar-Dasar Pemrograman</option>
                            <option value="WEB">Pemrograman Web</option>
                            <option value="BASDAT">Basis Data</option>
                        </select>
                    </div>
                </div>
                <div class="form-group row">
                    <label for="nilai_uts" class="col-4 col-form-label">Nilai UTS</label>
                    <div class="col-8">
                        <input id="nilai_uts" name="nilai_uts" placeholder="Masukkan Nilai UTS" type="text" class="form-control">
                    </div>
                </div>
                <div class="form-group row">
                    <label for="nilai_uas" class="col-4 col-form-label">Nilai UAS</label>
                    <div class="col-8">
                        <input id="nilai_uas" name="nilai_uas" placeholder="Masukkan Nilai UAS" type="text" class="form-control">
                    </div>
                </div>
                <div class="form-group row">
                    <label for="nilai_tugas" class="col-4 col-form-label">Nilai Tugas</label>
                    <div class="col-8">
                        <input id="nilai_tugas" name="nilai_tugas" placeholder="Masukkan Nilai Tugas" type="text" class="form-control">
                    </div>
                </div>
                <div class="form-group row">
                    <div class="offset-4 col-8">
                        <input type="submit" value="Simpan" name="proses" class="btn btn-primary" />
                    </div>
                </div>
            </form>
            <?php 
            if (isset($_POST['proses'])) {
                include_once('../../week2/nilai_siswa.php');
            }
             ?>
        </div>
    </section>
</div>
<!--Ini untuk tutup konten-->

<?php
include_once('footer.php');
?>