<html>
<body>
<?php
session_start();
if (isset($_POST['custname'])) {
	$_SESSION['custname'] = $_POST['custname'];
}
else {
	printf("<p>No name entered</p>");
}
if (isset($_POST['prefers'])) {
	$_SESSION['prefers'] = $_POST['prefers'];
	printf("<p>You prefer %s</p>",
	$_POST['prefers']);
}
?>
<form action=
"http://localhost:8088/readsession.php" 
method = "POST" >
<p>Number to order:<input type="text" 
name="numberorder" size="5"></p>
<input type="submit" value="submit order" />
</form>
</body>
</html>