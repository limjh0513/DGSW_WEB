<?php
session_start();

$id = $_POST['id'];
$pw = $_POST['password'];

if($id == 'test' && $pw == '1234'){

    $_SESSION['logged'] = true;

    header("Location: ./index.php");
} else{
    ?>
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <script>
            alert("아이디 어쩌구")
            history.back();
        </script>

    </head>
    </html>
    <?php
}
?>