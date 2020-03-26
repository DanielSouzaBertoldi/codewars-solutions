<?php
function upper($matches) {
  return strtoupper($matches[0]);
}

function toCamelCase($str){
  return preg_replace("(\-|\_)", "", preg_replace_callback('/([-_])([a-z])/', 'upper', $str));
}
?>