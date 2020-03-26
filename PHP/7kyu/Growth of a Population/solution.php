<?php
function nbYear($p0, $percent, $aug, $p) {
    $years = 0;
    $percent /= 100;
    
    while($p0 < $p) {
      ++$years;
      $p0 += $p0 * $percent + $aug;
    }
    
    return $years;
}
?>