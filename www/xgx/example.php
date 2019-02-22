<?php 
$post=$_POST['name'];
$pp=$name['name']
echo "<hr />";
$db=new MySQLi("localhost","root","","test");
$sql = "insert into admin(name) value('$pp')";
$result = $db->query($sql);
$req="select * from admin";
$res=$db->query($req);
while ($row=mysqli_fetch_assoc($res))
{
echo $row['name'].'<br />';
}
echo "<br />";
?>
