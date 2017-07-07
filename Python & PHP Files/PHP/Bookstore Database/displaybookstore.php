<html>
	<body>
		<?php
			$connect = mysqli_connect("localhost","root","abc123",
			"bookstore");
			printf("Connected");
			 if (!$connect){
				die("<h1>Could not connect to MySQL</h1>".mysqli_connect_error());
			}
			else {
				printf("<h1>Connected to MySQL</h1>");
				$sqlcmd = "SELECT * FROM books";
				$resultset = mysqli_query($connect,$sqlcmd);
				
				if ($resultset) {
					printf("<h1>Successful query </h1>");
					printf("<table>");
			//		printf("<th align='left'>Title</th>");
				//	<th align='left'>Author</th>
					//<th align='left'>Price Each</th>");
					while ($row = mysqli_fetch_row($resultset)){
						printf("<tr align='left'>");
						for ($i = 0; $i < count($row); $i++) 
							printf("<td>%s</td>",$row[$i]);
						printf("</tr>");
					}
					printf("</table>");
				}
				else {
					printf("<h1>Query did not run</h1>");
				}
				mysqli_close($connect);
			}
		?>
	</body>
</html>