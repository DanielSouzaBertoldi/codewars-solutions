<?php
function series_sum($n) {
  $base = 1;
  $sum = 0;
  
  while($n) {
    $sum = $sum + 1.0/$base;
    $base += 3;
    --$n;
  }
  return number_format($sum, 2);
}
?>