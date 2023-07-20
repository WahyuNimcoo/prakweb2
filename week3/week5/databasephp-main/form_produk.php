<?php
require_once 'dbkoneksi.php';
if (isset($_GET['idedit'])) {
  $sql = "SELECT * FROM produk WHERE id=?";
  $st = $dbh->prepare($sql);
  $st->execute([$_GET['idedit']]);
  $row = $st->fetch();
}
?>
<form method="POST" action="proses_produk.php">
  <div class="form-group row">
    <label for="kode" class="col-4 col-form-label">Kode</label>
    <div class="col-8">
      <div class="input-group">
        <div class="input-group-prepend">
          <div class="input-group-text">
            <i class="fa fa-anchor"></i>
          </div>
        </div>
        <input id="kode" name="kode" type="text" class="form-control" value="<?php if (isset($_GET['idedit'])) {
                                                                                echo $row['kode'];
                                                                              } ?>">
        <?php
        if (isset($_GET['idedit'])) {
          echo "<input name='idedit' type='hidden' value='" . $_GET['idedit'] . "'>";
        }
        ?>
      </div>
    </div>
  </div>
  <div class="form-group row">
    <label for="nama" class="col-4 col-form-label">Nama Produk</label>
    <div class="col-8">
      <div class="input-group">
        <div class="input-group-prepend">
          <div class="input-group-text">
            <i class="fa fa-adjust"></i>
          </div>
        </div>
        <input id="nama" name="nama" type="text" class="form-control" value="<?php if (isset($_GET['idedit'])) {
                                                                                echo $row['nama'];
                                                                              } ?>">
      </div>
    </div>
  </div>
  <div class="form-group row">
    <label for="harga_beli" class="col-4 col-form-label">Harga Beli</label>
    <div class="col-8">
      <div class="input-group">
        <div class="input-group-prepend">
          <div class="input-group-text">
            <i class="fa fa-arrow-circle-o-left"></i>
          </div>
        </div>
        <input id="harga_beli" name="harga_beli" value="<?php if (isset($_GET['idedit'])) {
                                                          echo $row['harga_beli'];
                                                        } ?>" type="text" class="form-control">
      </div>
    </div>
  </div>
  <div class="form-group row">
    <label for="stok" class="col-4 col-form-label">Stok</label>
    <div class="col-8">
      <div class="input-group">
        <div class="input-group-prepend">
          <div class="input-group-text">
            <i class="fa fa-arrow-circle-up"></i>
          </div>
        </div>
        <input id="stok" name="stok" value="<?php if (isset($_GET['idedit'])) {
                                              echo $row['stok'];
                                            } ?>" type="text" class="form-control">
      </div>
    </div>
  </div>
  <div class="form-group row">
    <label for="min_stok" class="col-4 col-form-label">Minimum Stok</label>
    <div class="col-8">
      <div class="input-group">
        <div class="input-group-prepend">
          <div class="input-group-text">
            <i class="fa fa-arrow-circle-right"></i>
          </div>
        </div>
        <input id="min_stok" name="min_stok" value="<?php if (isset($_GET['idedit'])) {
                                                      echo $row['min_stok'];
                                                    } ?>" type="text" class="form-control">
      </div>
    </div>
  </div>
  <div class="form-group row">
    <label for="jenis" class="col-4 col-form-label">Jenis Produk</label>
    <div class="col-8">
      <?php
      $sqljenis = "SELECT * FROM jenis_produk";
      $rsjenis = $dbh->query($sqljenis);
      ?>
      <select id="jenis" name="jenis" class="custom-select">
        <?php
        if (isset($_GET['idedit'])) {
          $sqljenis = "SELECT * FROM jenis_produk WHERE id=?";
          $stjenis = $dbh->prepare($sqljenis);
          $stjenis->execute([$row['jenis_produk_id']]);
          $rowjenis = $stjenis->fetch();
        ?>
          <option value="<?= $rowjenis['id'] ?>"><?= $rowjenis['nama'] ?></option>
        <?php
        }
        foreach ($rsjenis as $rowjenis) {
        ?>
          <option value="<?= $rowjenis['id'] ?>"><?= $rowjenis['nama'] ?></option>
        <?php
        }
        ?>
        <!--
        <option value="1">Elektronik</option>
        <option value="2">Furniture</option>
        <option value="3">Makanan</option>-->

      </select>
    </div>
  </div>
  <div class="form-group row">
    <div class="offset-4 col-8">
      <input type="submit" name="proses" type="submit" class="btn btn-primary" value="<?php if (isset($_GET['idedit'])) {
                                                                                        echo "Update";
                                                                                      } else {
                                                                                        echo "Simpan";
                                                                                      } ?>" />
    </div>
  </div>
</form>