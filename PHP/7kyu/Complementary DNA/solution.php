<?php
function DNA_strand($dna) {
  return strtr($dna, ['A' => 'T', 'T' => 'A', 'C' => 'G', 'G' => 'C']);
}
?>