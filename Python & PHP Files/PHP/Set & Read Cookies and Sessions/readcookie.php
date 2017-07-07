<html>
<body>
<?php
if (isset($_COOKIE["name"])) {
	$name = $_COOKIE["name"];
	printf("<h1>Welcome back %s</h1>",
	$name);
}
else {
	printf("<h1>The Hardware store ");
	printf(" welcomes you</h1>");
}
 if (isset($_COOKIE["prefers"])) {
	$prefers = $_COOKIE["prefers"];
	if ($prefers == "power tools") {
		printf("<p>Power tools are 15% off</p>");
	}
	else if ($prefers == "hand tools") {
		printf("<p>Hammers are on sale</p>");
	}
	else {
		printf("<p>Pine scented air ");
		printf(" fresheners are $1.99");
	}
}
?>
</body>
</html>