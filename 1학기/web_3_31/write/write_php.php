<?php

$content = $_POST['content'];


//파일 열어서 fopen("경로", 모드)
//모드 : read/ wirte/ append
$file = fopen('./content.txt','w');

//파일 내용 기록
// fwrite(파일 핸들러, 입력할 내용)
fwrite($file, $content);

//닫기
fclose($file);

// 돌아가기
header('Location: ./write.php');


?>