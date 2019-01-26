<html>
	<head>
		<link rel="stylesheet" href="CSS/main.css">
		<link rel="stylesheet" href="CSS/table.css">
		<title>GET MY BOOK</title></head>
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
		<link href="https://fonts.googleapis.com/css?family=Nunito" rel="stylesheet">
	<body>
		<form action = "get.php" method = "get" >
			<table style="margin-top:30px;">
			<tr>
				<td><h1 style="color:white;vertical-align:center;">GET MY BOOK</h1></td><td style="padding-left:10vh;"><input type="text"  name="book"/><button type="submit"><i class="fa fa-search"></i></button></td>
			</tr>
			</table>
			</form>
		<div class="div2">
			<center>
				<?php
					ini_set('max_execution_time', 300); 
					$name = $_GET["book"];
					exec('scrapy runspider Amazon.py -a term="'.$name.'"');
					exec('scrapy runspider Flipkart.py -a term="'.$name.'"');
					exec('scrapy runspider Crossword.py -a term="'.$name.'"');
					$name = strtoupper($name);
					$ama = fopen("AMAZON.txt", "r");
					$flip = fopen("FLIPKART.txt", "r");
					$cross = fopen("CROSSWORD.txt", "r");
					$a_link = fgets($ama);
					$a_img = fgets($ama);
					$a_price = fgets($ama);
					$c_price = fgets($cross);
					$c_link = fgets($cross);
					$f_price = fgets($flip);
					$f_link = fgets($flip);
					echo "<table class='main_table' ><th>".$name."</th><th>WEBSITE</th><th>PRICE</th><th>LINK</th><tr><td rowspan='3'><img src=".$a_img."></td><td>AMAZON</td><td>".$a_price."</td><td><a href='".$a_link."'><img src='CSS/AMAZON.jpg' height='55px' width = '50%'/></a></td></tr><tr><td>CROSSWORD</td><td>".$c_price."</td><td><a href='".$c_link."'><img src='CSS/CROSSWORD.jpg' height='55px' width = '50%'/></a></td></tr><tr><td>FLIPKART
					</td><td>".$f_price."</td><td><a href='".$f_link."'><img src='CSS/FLIPKART.jpg' height='55px' width = '50%'/></a></td></tr></table>";
				?>
			</center>
		</div>
	</body>
</html>