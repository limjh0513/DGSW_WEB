<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

<?php
    if(isset($_SESSION['logged'])){
?>
<br><br>
<a href="./logout.php">로그아웃</a>
<?php
else{
    ?>
    <form method="POST" action="./login_action.php">
    <label>아이디:<input type="text" name="id"></label><br>
    <label>아이디:<input type="password" name="password"></label><br>
    <input type="submit" value="로그인">
</form>
<?php } ?>
}
</body>
</html>