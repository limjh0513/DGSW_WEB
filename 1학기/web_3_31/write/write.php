
<!doctype html>
<html lang="ko">
	<head>
	<meta charset="utf-8" />
		<link rel="stylesheet" href="app.css">
		<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css">
		<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
		<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.bundle.min.js"></script>
		<style>
body {
	padding-top: 50px;
	padding-bottom: 100px;
}
		</style>
	</head>
	<body>
		<main class="container">
			<form method="POST" action="write_php.php">
				<div class="form-group">
				  <label for="guest-content" class="form-label">내용</label>
				  <textarea class="form-control" id="guest-content" name="content" rows="3" required></textarea>
				</div>
				<button type="submit" class="btn btn-primary">작성</button>
			</form>
			<hr>
            <?php

            $file = fopen('./content.txt', 'r');

        while(!feof($file)){
			echo htmlspecialchars(fgets($file), ENT_QUOTES,'utf-8', true);
        }
            fclose($file);
            ?>

	<br><br>
	<a href="./logout.php">로그아웃</a>
	<?php
//}else{
	//로그인이 되어있지 않다면 로그인폼을 표시
	?>
			<form class="form-inline" method="POST" action="login_action.php">
				<input type="password" name="password">
				<input type="submit" value="로그인">
			</form>
	<?php
//}
?>
        </main>
    </body>
    
</html>