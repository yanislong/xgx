<?php
    @ini_set('display_errors',1);
    $str = $_GET['joke'];
    $filePath = "/root/var/www/html/xss.txt";

    if(is_writable($filePath)==false){
         echo "can't write";
    }else{
          $handler = fopen(filePath, "a");
          fwrite($handler, $str);
          fclose($handler);
    }
?>
