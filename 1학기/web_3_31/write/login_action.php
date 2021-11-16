<?php
// 세션 시작
session_start();

// 입력된 패스워드를 가져와서
$password = $_POST['password'];

// 비교!
if ($password == '1234') {
	// 세션에 logged 값을 true 로 설정
	$_SESSION['logged'] = true;
	// 원래 있던 페이지로 이동
	header('Location: ./write.php');
}else{
	// 비밀번호가 맞지 않다면 오류 표시 후 뒤로가기
?>
	<script>
		alert("비밀번호가 올바르지 않습니다.");
		// 뒤로가기
		history.back();
	</script>
<?php
}
?>