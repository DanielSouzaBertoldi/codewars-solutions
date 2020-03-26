<?php
function orderWeight($str) {
  $nums = explode(" ", $str);
  $sumArr = array();
  $sum = 0;
  foreach($nums as $num) {
    for($i = 0; $i < strlen($num); $i++)
      $sum += strval($num[$i]);

    array_push($sumArr, $sum);
    $sum = 0;
  }

  array_multisort($sumArr, $nums, SORT_STRING);
  return implode(' ', $nums);
}
?>