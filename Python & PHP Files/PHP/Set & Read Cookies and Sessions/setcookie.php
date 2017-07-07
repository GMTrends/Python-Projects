<html>
<body>
<?php
$prefers = $_POST['prefers'];
$name = $_POST['custname'];
printf("<h1>Thank you %s, you prefer %s</h1>",
$name,$prefers);
setcookie("prefers",$prefers,time() + 60);
setcookie("name",$name,time() + 60);
?>
</body>
</html>