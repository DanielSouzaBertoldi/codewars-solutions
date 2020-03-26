<?php
function format_duration($seconds) {
  $times = array("year" => 365 * 24 * 60 * 60, 
                 "day" => 24 * 60 * 60,
                 "hour"=> 60 * 60,
                 "minute"=> 60,
                 "second" => 1);

    if(empty($seconds))
        return "now";

  $years = intdiv($seconds, $times["year"]);
  $days = intdiv(($seconds - $times["year"]*$years), $times["day"]);
  $hours = intdiv(($seconds - $times["year"]*$years - $times["day"]*$days), $times["hour"]);
  $minutes = intdiv(($seconds - $times["year"]*$years - $times["day"]*$days - $times["hour"]*$hours), $times["minute"]);
  $seconds = $seconds - $times["year"]*$years - $times["day"]*$days - $times["hour"]*$hours - $times["minute"]*$minutes;
  
  $chunks = array("year" => $years, "day" => $days, "hour" => $hours, "minute" => $minutes, "second" => $seconds);
  
  $firstiteration = 0;
  $string = "";
  foreach($chunks as $key => $time) {
    $date = $key;
    if($time) {
      if($firstiteration)
        $string .= ", ";

      if($time > 1)
        $date = $key . "s";

      $string .= strval($time) . " " . $date;
      $firstiteration = 1;
    }
  }

  $array = explode(", ", $string);
  return join(' and ', array_filter(array_merge(array(join(', ', array_slice($array, 0, -1))), array_slice($array, -1)), 'strlen'));
}
?>