<?php
function find_next_empty($puzzle) {
    for ($i = 0; $i < 9; $i++) {
        for ($j = 0; $j < 9; $j++) {
          if ($puzzle[$i][$j] == -1) {
            return [$i, $j];
          }
        }
    }
    return [null, null];
}

function is_valid($puzzle, $guess, $row, $col) {
  $row_vals = $puzzle[$row];
  if (in_array($guess, $row_vals)) {
    return False;
  }
  $col_vals = [];
  for ($k = 0; $k < 9; $k++) {
    array_push($col_vals, $puzzle[$k][$col]);
  }
  if (in_array($guess, $col_vals)) {
    return False;
  }
  $row_start = (floor($row / 3) * 3);
  $col_start = (floor($col /3) * 3);
  for ($r = $row_start; $r < ($row_start + 3); $r++) {
    for ($c = $col_start; $c < ($col_start + 3); $c++) {
      if ($puzzle[$r][$c] == $guess) {
        return False;
      }
    }
  }
  return True;
}

function solve_sudoku($puzzle) {
  [$row, $col] = find_next_empty($puzzle);
  if ($row == null) {
    return True;
  }
  for ($i = 0; $i < 9; $i++) {
    if (is_valid($puzzle, $i, $row, $col)) {
      $puzzle[$row][$col] = $i;
      if (solve_sudoku($puzzle)) {
        return True;
      }
      $puzzle[$row][$col] = -1;
    }
  return False;
  }
}

$example_board = [
  [3,9,-1, -1,5,-1, -1,-1,-1],
  [-1,-1,-1, 2,-1,-1, -1,-1,-1],
  [-1,-1,-1, 7,1,9, -1,8,-1],

  [-1,5,-1, -1,6,8, -1,-1,-1],
  [2,-1,6, -1,-1,3, -1,-1,-1],
  [-1,-1,-1, -1,-1,-1, -1,-1,4],

  [5,-1,-1, -1,-1,-1, -1,-1,-1],
  [6,7,-1, 1,-1,5, -1,4,-1],
  [1,-1,9, -1,-1,-1, 2,-1,-1]
];
print_r(solve_sudoku($example_board));
print_r($example_board);