<?php require ('config/db.php');

//Create Query
$query = 'SELECT * FROM attendance ORDER BY id DESC';

//Get Results
$result = mysqli_query($conn, $query);

// Fetch Data
$students = mysqli_fetch_all($result, MYSQLI_ASSOC);
// var_dump($blogs);

mysqli_free_result($result);

mysqli_close($conn);


?>







<!DOCTYPE html>
<html>
<head>
	<title>Attendance Table</title>
	<style>
		table {
			border-collapse: collapse;
			width: 100%;
			font-family: Arial, sans-serif;
			font-size: 14px;
			text-align: left;
		}
		table th, table td {
			border: 1px solid #ddd;
			padding: 8px;
		}
		table th {
			background-color: #f2f2f2;
			color: #333;
		}
		table tr:nth-child(even) {
			background-color: #f9f9f9;
		}
	</style>
</head>
<body>
	<h1>Attendance Table</h1>
	<div class="container">
		<div id="link_wrapper">

		</div>
	</div>
</body>


<script>
function loadXMLDoc() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("link_wrapper").innerHTML =
      this.responseText;
    }
  };
  xhttp.open("GET", "server.php", true);
  xhttp.send();
}
setInterval(function(){
	loadXMLDoc();
	// 1sec
},1000);

window.onload = loadXMLDoc;
</script>
</html>
