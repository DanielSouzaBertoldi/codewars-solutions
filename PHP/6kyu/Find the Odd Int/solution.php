<?php
function findIt(array $seq) : int
{
    $item = array();
    
    for($i = 0; $i < count($seq); $i++) {
      if(array_key_exists(strval($seq[$i]), $item))
        $item[strval($seq[$i])] += 1;
      else
        $item[strval($seq[$i])] = 1;
    }

    foreach($item as $key => $value){
      if($value % 2 == 1)
        return $key;
    }
    
    return 0;
}
?>