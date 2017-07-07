<html>
<head><title>Song Survey PHP</title></head>
<body>
<h1>Song Survey</h1>

<?php
	$songsfile = fopen("songs.txt", "a") or
		die("<strong>Invalid data entry</strong>");
	
	$song = $_POST["song"]; // Song Title variable
	for ($i = 0; $i < count($song); $i += 1) {
		printf("<p>%s</p>", $song);
		if($i != (count($song)-1))
			fputs($songsfile, "$song\r\n");
		else
			fputs($songsfile, "$song\r\n");
	} // end of for loop
	
	$composer = $_POST["composer"]; // Song Composer variable
	for ($i = 0; $i < count($composer); $i += 1) {
		printf("<p>%s</p>", $composer);
		if($i != (count($composer)-1))
			fputs($songsfile, "$composer\r\n");
		else
			fputs($songsfile, "$composer\r\n");
	} // end of for loop
	
	$artist = $_POST["artist"]; // Song Artist variable
	for ($i = 0; $i < count($artist); $i += 1) {
		printf("<p>%s</p>", $artist);
		if($i != (count($artist)-1))
			fputs($songsfile, "$artist\r\n\r\n");
		else
			fputs($songsfile, "$artist\r\n\r\n");
	} // end of for loop
	
	fclose($songsfile);  // Close "songs.txt" file
	
	printf("<h3>Thank you!</h3>");
?>

</body>
</html>