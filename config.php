<?php
extract($_REQUEST);
$file = fopen("form-save.txt", "a");

fwrite($file, $class1 . "\n");
fwrite($file, ",");
fwrite($file, $class2 . "\n");
fwrite($file, ",");
fwrite($file, $class3 . "\n");
fwrite($file, ",");
fwrite($file, $class4 . "\n");

fclose($file);
header("location: index.php");
