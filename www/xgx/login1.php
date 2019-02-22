<?php
if(is_null($_REQUEST['username']) || is_null($_REQUEST['password']))
{
        die();
}
$link=mysql_connect("localhost","root","");
mysql_query("SET NAMES 'gbk'");
mysql_select_db("test",$link);
$username=addslashes($_REQUEST['username']);
#$password=md5($_REQUEST['password']);
$password=$_REQUEST['password'];
$sql="select count(*) as num from admin where name='".$username."' and pass='".$password."'";
echo addslashes($username);
echo "<br />";
#echo "$sql";
$query=mysql_query($sql);
$res=mysql_fetch_array($query);
$count=$res['num'];
if($count==1)
{
        echo "login success";
}
else
{
        echo "login failed";
}
?>
