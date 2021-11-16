<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <form method="POST">
      <input type="number" id="calc-a" name="a" value="<?=$_REQUEST['a']?>" />
      <select id="calc-op" name="op">
          <option value="add" <?php if($op=="add")  echo "selected"; ?>>+</option>
        <option value="sub" <?php if($op=="sub")  echo "selected"; ?>>-</option>
        <option value="mul" <?php if($op=="mul")  echo "selected"; ?>>x</option>
        <option value="div" <?php if($op=="div")  echo "selected"; ?>>/</option> 
      </select>
      <input type="number" id="calc-b" name="b" value="<?=$_REQUEST['b']?>"/>
      <input type="submit" value="계산하기" />
      <input type="reset" value="초기화" />
    </form>
    <div>결과: <?php 
    
    if(isset($_REQUEST['a']) && isset($_REQUEST['b']))
    {
      $op = $_REQUEST['op'];
      $a = (int)$_REQUEST['a'];
      $b = (int)$_REQUEST['b'];
      if($op == "add"){
        $result = $a + $b;
      } else if($op == "sub"){
        $result = $a - $b;
      }else if($op == "mul"){
        $result = $a * $b;
      }else if($op == "div"){
        $result = $a / $b;
      }
      echo($result);
    }
    else{
      echo("계산할 숫자 입력 후 계산하기 버튼 클릭!");
    }
  ?></div>
  

  <!--

/*
print_r: 배열 등 객체의 정보를 출력해줌

// GET 요청으로 들어온 변수
print_r($_GET);

// POST 요청으로 들어온 변수
print_r($_POST);

// GET, POST 요청 및 COOKIE 가 합쳐있음
print_r($_REQUEST);
*/

// 변수가 정의되어 있는지 확인
if (isset($_REQUEST['a'])) {
	// 문자열을 숫자형으로 변환
	$a = (int)$_REQUEST['a'];
	
	//TODO: 나머지 코드 작성
}
-->
  </body>
</html>
