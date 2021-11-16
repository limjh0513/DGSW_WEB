<?php
// 서버 연결 / 서버주소, 아이디, 비밀번호, DB이름
$id = $_POST['id'];
$pw = $_POST['pw'];

$mysqli = new mysqli('localhost', 's2115', '21152115', 's2115');
if (mysqli_connect_error()) {
    exit('Connect Error');
}

// 쿼리 실행
$cursor = $mysqli->query("SELECT * FROM `users` WHERE 1=1");

// SELECT 구문일 경우 가져온 행 갯수
echo $cursor->num_rows;
echo "<br>";

// 결과 1개 가져오기
//$row = $cursor->fetch_assoc();

// 결과 전부 가져오기
while ($row = $cursor->fetch_assoc()) {
    print_r($row);
    echo "<br>";
}

// 서버 연결 / 서버주소, 아이디, 비밀번호, DB이름
$mysqli = new mysqli('localhost', 's2115', '21152115', 's2115');
if (mysqli_connect_error()) {
    exit('Connect Error');
}

$id = $mysqli->real_escape_string($id);
$pw = $mysqli->real_escape_string($pw);

// 쿼리 실행
$cursor = $mysqli->query("SELECT * FROM `users` WHERE user_id = '" . $id . "' AND user_pw = '" . $pw . "'");
// SELECT * FROM `users` WHERE user_id = 'admin' AND user_pw = '1234';"
//SELECT * FROM `users` WHERE user_id = '" . $id . "' AND user_pw = '" . $pw . "';

if ($cursor->num_rows > 0) {
    // DB에서 한개 이상 결과가 나온다면 로그인 성공
    
    // 결과 행을 가져옴
    $row = $cursor->fetch_assoc();
    
    // 세션 이름에 pk값 저장
    $_SESSION['name'] = $row['pk'];
    
    // 원래 페이지로 이동
    header("Location: ./index.php");
}else{
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
    <div>hello</div>    
</body>
</html>
<?php
}
?>