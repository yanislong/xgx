<!DOCTYPE html>
<meta charset="gbk"><!--仅用于基础的显示，换成utf8也行就是不好看-->
<?php 
error_reporting(0);
$conn = mysql_connect('127.0.0.1','root',''); 
mysql_select_db('test',$conn);
mysql_query("set names 'gbk'");  //不安全的编码设置方式
$res = mysql_query("show variables like 'character%';"); //显示当前数据库设置的各项字符集
while($row = mysql_fetch_array($res)){
var_dump($row);
}
$user = addslashes($_GET['sql']); //mysql_real_escape_string() magic_quote_gpc=On addslashes() mysql_escape_string()功能类似
$sql = "SELECT name,pass FROM admin WHERE name='".$user."'"; 
echo $sql.'</br>';
echo $user."</br >";
if($res = mysql_query($sql)){ 
while($row = mysql_fetch_array($res)){
var_dump($row);
}
} 
else{ 
echo "Error".mysql_error()."<br/>"; 
} 
?>
