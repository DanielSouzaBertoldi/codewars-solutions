<?php
function decode_morse(string $code): string {
  $result = '';
  $words = explode("  ", trim($code));

  for($i = 0; $i < count($words); $i++) {
    $word = explode(' ', $words[$i]);
    for($j = 0; $j < count($word); $j++)
      $result .= MORSE_CODE[$word[$j]];
    if($i != count($words)-1)
      $result .= ' ';
  }

  return $result;
}
?>