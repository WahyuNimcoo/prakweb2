<?php
session_start(); // Mulai Session
// cek terlebih dahulu apakah user sudah submit form atau belum
// dengan menggunakan fungsi if isset
if (isset($_POST['login'])){
    // ambil data dari form login
    // 1. ambil data username
    // 2. ambil data password
    $username = $_POST['username'];
    $password = $_POST['password'];
	// validasi username dan password
	// misal username == admin && password == 12345
	if ($username == "admin" && $password == "12345") {
		$_SESSION['username'] = $username; // set session username
		header('Location: home.php');
		exit();
	} else {
		$error = 'Username dan passwors salah';
	}

}



// jika username dan password sama arahkan/redirect ke halaman dashboard

// jika username dan password salah kasih alert username dan pass sama
// tetap di halaman login 

?>

<!doctype html>
<html lang="en">
  <head>
  	<title>Login PMB</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

	<link href="https://fonts.googleapis.com/css?family=Lato:300,400,700&display=swap" rel="stylesheet">

	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
	
	<link rel="stylesheet" href="dist_login/css/style.css">

	</head>
	<body class="img js-fullheight" style="background-image: url(dist_login/images/bg.jpg);">
	<section class="ftco-section">
		<div class="container">
			<div class="row justify-content-center">
				<div class="col-md-6 text-center mb-5">
					<h2 class="heading-section">Login </h2>
                    <?php if (isset($error)){
                        echo '<h5>' . $error . '</h5>';
                    } ?>
				</div>
			</div>
			<div class="row justify-content-center">
				<div class="col-md-6 col-lg-4">
					<div class="login-wrap p-0">
		      	<form method="POST" action="index.php" class="signin-form">
		      		<div class="form-group">
		      			<input type="text" name="username" class="form-control" placeholder="Username" required>
		      		</div>
	            <div class="form-group">
	              <input id="password" name="password" type="password" class="form-control" placeholder="Password" required>
	              <span toggle="#password" class="fa fa-fw fa-eye field-icon toggle-password"></span>
	            </div>
	            <div class="form-group">
	            	<input name="login" type="submit" class="form-control btn btn-primary submit px-3"></button>
	            </div>
	            <div class="form-group d-md-flex">
	            	<div class="w-50">
		            	<label class="checkbox-wrap checkbox-primary">Remember Me
									  <input type="checkbox" checked>
									  <span class="checkmark"></span>
									</label>
								</div>
								<div class="w-50 text-md-right">
									<a href="#" style="color: #fff">Forgot Password</a>
								</div>
	            </div>
	          </form>
	          <!-- <p class="w-100 text-center">&mdash; Or Sign In With &mdash;</p>
	          <div class="social d-flex text-center">
	          	<a href="#" class="px-2 py-2 mr-md-1 rounded"><span class="ion-logo-facebook mr-2"></span> Facebook</a>
	          	<a href="#" class="px-2 py-2 ml-md-1 rounded"><span class="ion-logo-twitter mr-2"></span> Twitter</a>
	          </div> -->
		      </div>
				</div>
			</div>
		</div>
	</section>

	<script src="dist_login/js/jquery.min.js"></script>
  <script src="dist_login/js/popper.js"></script>
  <script src="dist_login/js/bootstrap.min.js"></script>
  <script src="dist_login/js/main.js"></script>

	</body>
</html>

