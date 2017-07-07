<html>
<head>
<title>Process Employee Pay</title>
</head>
<body>
<?php
$employeename = $_POST["employeename"];
if ($employeename != "") {
	printf("<h3>The employee name is %s</h3>",
	$employeename);
}
else {
printf("<h2>No employee name was input</h2>");
}
$email = $_POST["email"];
if ($email != "") {
	printf("<h3>The employee email is %s</h3>",
	$email);
}
else {
printf("<h2>No employee email was input</h2>");
}
 if (isset($_POST["emptype"])) {
	$emptype = $_POST["emptype"];
	if ($emptype == "parttime") {
		printf("<h3>Part time employee</h3>");
	}
	else {
		printf("<h3>Full time employee</h3>");
	}
  }  // end of isset test
$hoursworked = $_POST["hoursworked"];
if ($hoursworked != "") {
	$hoursworked = (int) $hoursworked;
}
else {
	$hoursworked = 40;
}
$payrate = $_POST["payrate"];
if ($payrate != "") {
	$payrate = (float) $payrate;
   if ($hoursworked <= 40) {
	 $totalpay = $hoursworked * $payrate;
     }
   else {
	 $totalpay = 40 * $payrate + 
	 ($hoursworked - 40) * 1.5 * $payrate;
    }
printf("<p>Hours %d Payrate $%7.2f</p>",
$hoursworked,$payrate);
printf("<p>Total pays is $%7.2f</p>",
$totalpay);
}  // end of pay block
?>
</body>
</html>