<?php 
include("config/db.php");
 ?>
<table class="table">
			<thead>
				<th>Name</th>
				<th>Status</th>
			</thead>
<?php 
	$query = mysqli_query($conn, "SELECT * FROM attendance");
	while($row = mysqli_fetch_array($query)){

		$name = $row['name'];
		$status = $row['status'];
 ?>
			<tbody>
				<tr>
					<td><?php echo $name; ?></td>
					<td><?php echo $status; ?></td>
				</tr>
			</tbody>
<?php 	} ?>
		</table>