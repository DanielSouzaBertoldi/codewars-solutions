<?php
function is_prime(int $n): bool {
  if($n > 1) {
    for($i = 2; $i <= sqrt($n); $i++){
      if($n % $i == 0)
        return false;
    }
    return true;
  }
  return false;
}
?>