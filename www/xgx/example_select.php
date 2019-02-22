<?php 
$post=$_POST[name];
echo $name['name'];
echo "<hr />";
$db=new MySQLi("localhost","root","","test");
$req="select * from admin where name='$post'";
$res=$db->query($req);
echo "<table class='itable' border='1' cellspacing='0' width='300px' height='150'>";
echo "<tr>";
echo "<td>id</td>";
echo "<td>username</td>";
echo "</tr>";
while ($row=mysqli_fetch_assoc($res))
{
echo "<br />";
echo "<td>num</td>";
echo "<td>".$row['name']."</td>";
echo "</tr>";
}
echo "</table>";
$db->close();
?>
