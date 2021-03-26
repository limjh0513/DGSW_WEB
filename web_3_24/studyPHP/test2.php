<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    현재시간 : <?php echo date("H:i:s"); ?><br>
    접속한 ip : <?php echo $_SERVER['REMOTE_ADDR'] ?><br>
    접속한 user-agent: <?php echo $SERVER['HTTP_USER_AGENT']?><br>
</body>
</html>
