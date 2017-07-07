<html>
<body>
<h1>insertbookstoresql.php</h1>
<?php
$title = $_POST['title'];
$author = $_POST['author'];
$priceeach = $_POST['priceeach'];
$numbersold = $_POST['numbersold'];
$pubnumb = $_POST['pubnumb'];
$connect = mysqli_connect("localhost","root",
"abc123","bookstore");
printf("Connected");
if (!$connect){
die("<h1>MySQL</h1>".mysqli_connect_error());
}
else {
	printf("<h1>Connected to MySQL</h1>");
	$sqlcmd = "INSERT INTO books ".
	"VALUES('$title','$author','$pubnumb'".
",$numbersold,$priceeach)";
printf("<h1>%s</h1>",$sqlcmd);
$numberupdated=mysqli_query($connect,$sqlcmd);
if ($numberupdated == 1) {
printf("<h1>Record added </h1>");
}
mysqli_close($connect);
}
?>
</body>
</html>