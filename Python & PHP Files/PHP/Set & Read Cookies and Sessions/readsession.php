<html>
<body>
<h1>Hardware Store</h1>
<?php
session_start();
if (isset($_SESSION['custname'])) {
	printf("<p>Welcome %s</p>", 
	$_SESSION['custname']);
}
else {
printf("<p>Welcome to the Hardware Store</p>");
}
if (isset($_SESSION['prefers'])) {
	printf("<p>You prefer %s</p>", 
	$_SESSION['prefers']);
}
if (isset($_POST['numberorder'])) {
	printf("<p>You ordered %s</p>",
	$_POST['numberorder']);
}
?>
</body>
</html>