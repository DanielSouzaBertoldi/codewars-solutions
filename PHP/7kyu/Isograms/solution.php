<?php
function isIsogram($string) {
  if(strlen($string) == 0)
    return true;
  
  $string = strtolower($string);
  foreach(count_chars($string, 1) as $key => $ocurrences) {
    if($ocurrences != 1)
      return false;
  }
  
  return true;
}
?>