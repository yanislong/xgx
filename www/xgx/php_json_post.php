<?php
//sleep(10);
    header("Content-Type: application/json;charset=utf-8");
//    echo file_get_contents('php//input')
//    $student = $_POST["user"];
//    var_dump($GLOBALS[$student]);
    echo "123>>\n";
    echo $GLOBALS["HTTP_RAW_POST_DATA"];
    echo ">>\n";
    echo $_GET[a];
    echo ">>\n";
    var_dump($_GET);
#    var_dump($GLOBALS["HTTP_RAW_POST_DATA"]);
#    var_dump($GLOBALS);
//    echo $student['name'];
//    echo $student['age'];
//    echo $student['sex'];
//echo $student;
//$res = json_decode($GLOBAL["HTTP_RAW_POST_DATA"]);
//var_dump($res);
//echo $res->name;
//echo $student->name;

//$db=new MySQLi("localhost","root","","test");
$pp = $_GET[a];
$sql = "insert into admin(name) value('$pp')";
$result = $db->query($sql);
?>
