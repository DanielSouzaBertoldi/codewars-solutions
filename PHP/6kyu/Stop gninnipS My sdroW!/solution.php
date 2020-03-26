<?php
function spinWords(string $str): string {
  $words = explode(" ", $str);
  
  foreach($words as $index => $word) {
    if(strlen($word) > 4)
      $words[$index] = strrev($word);
  }
  
  return implode(" ", $words);
}
?>