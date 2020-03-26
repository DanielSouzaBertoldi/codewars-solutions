<?php
function likes( $names ) {
  switch(count($names)) {
    case 0: return "no one likes this"; break;
    case 1: return sprintf("%s likes this", $names[0]); break;
    case 2: return sprintf("%s and %s like this", $names[0], $names[1]); break;
    case 3: return sprintf("%s, %s and %s like this", $names[0], $names[1], $names[2]); break;
    default: return sprintf("%s, %s and %d others like this", $names[0], $names[1], count($names)-2); break;
  }
}
?>