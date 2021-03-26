<?php
session_start();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $type = $_POST['type'];
	
	if($type == "login"){
        $uid = $_POST['id'];
	    $upw = $_POST['password'];
        if ($uid == 'test' && $upw == '1234') {
            $_SESSION['name'] = "임재현";
            $logged = true;
        }else{
            $logged = false;
        }
    } else if ($type == 'logout') {
		unset($_SESSION['name']);
	}
}
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<form method="POST">
<?php if (isset($_SESSION['name'])) { ?>
		안녕하세요! <?=$_SESSION['name']?>님!<br>
		<input type="hidden" name="type" value="logout"><br>
		<input type="submit" value="로그아웃">
<?php } else { ?>
		<input type="hidden" name="type" value="login"><br>
        아이디: <input type="text" name="id"><br>
        비밀번호: <input type="password" name="password"><br>
<input type="submit" value="로그인">
<?php } ?>
</body>
</html>