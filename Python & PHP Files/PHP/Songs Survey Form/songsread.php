<html>
<head><title>Song Survey Read</title></head>
<body>
<h1>Survey Data Results</h1>

<?php
	$songsfile = fopen("songs.txt", "r") or
		die("<strong>Invalid file</strong>");
	
	$textdoc = fgets($songsfile, 100);
	while (!feof($songsfile)) {
		printf("<h3>%s</h3>", $textdoc);
		$textdoc = fgets($songsfile, 100);
	} // end of while loop
	
	fclose($songsfile); // Close file
?>

</body>
</html>