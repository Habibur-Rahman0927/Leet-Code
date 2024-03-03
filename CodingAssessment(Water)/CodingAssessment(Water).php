<?php

function calculate_fill_time($queue, $num_taps) {
    $total_time = 0;
    while ($queue) {
        for ($i = 0; $i < min($num_taps, count($queue)); $i++) {
            $bottle_size = array_shift($queue);
            $fill_time = $bottle_size / 100; 
            $total_time += $fill_time;
        }
    }
    return $total_time;
}

$queue = [400, 750, 1000];
$num_taps = 2;
echo "Total time required: " . calculate_fill_time($queue, $num_taps) . " seconds\n";


function calculate_fill_time_with_input_validation($queue, $num_taps) {
    if (!is_array($queue) || !array_filter($queue, 'is_int')) {
        throw new TypeError("Queue must be an array of integers.");
    }
    if (!is_int($num_taps) || $num_taps <= 0) {
        throw new ValueError("Number of taps must be a positive integer.");
    }
    
    $total_time = 0;
    while ($queue) {
        for ($i = 0; $i < min($num_taps, count($queue)); $i++) {
            $bottle_size = array_shift($queue);
            $fill_time = $bottle_size / 100; 
            $total_time += $fill_time;
        }
    }
    return $total_time;
}

$queue = [400, 750, 1000];
$num_taps = 1;
echo "Total time required: " . calculate_fill_time_with_input_validation($queue, $num_taps) . " seconds\n";


function calculate_fill_time_with_walking_time($queue, $num_taps, $walking_time_per_person) {
    if (!is_array($queue) || !array_filter($queue, 'is_int')) {
        throw new TypeError("Queue must be an array of integers.");
    }
    if (!is_int($num_taps) || $num_taps <= 0) {
        throw new ValueError("Number of taps must be a positive integer.");
    }
    if (!is_int($walking_time_per_person) || $walking_time_per_person < 0) {
        throw new ValueError("Walking time per person must be a non-negative number.");
    }
    
    $total_time = 0;
    while ($queue) {
        $total_time += $walking_time_per_person * min($num_taps, count($queue));
        for ($i = 0; $i < min($num_taps, count($queue)); $i++) {
            $bottle_size = array_shift($queue);
            $fill_time = $bottle_size / 100;
            $total_time += $fill_time;
        }
    }
    return $total_time;
}

$queue = [400, 750, 1000];
$num_taps = 3;
$walking_time_per_person = 2;
echo "Total time required: " . calculate_fill_time_with_walking_time($queue, $num_taps, $walking_time_per_person) . " seconds\n";


function calculate_fill_time_with_flow_rates($queue, $tap_flow_rates, $walking_time_per_person) {
    if (!is_array($queue) || !array_filter($queue, 'is_int')) {
        throw new TypeError("Queue must be an array of integers.");
    }
    if (!is_array($tap_flow_rates) || !array_filter($tap_flow_rates, 'is_numeric')) {
        throw new TypeError("Tap flow rates must be an array of numbers.");
    }
    if (array_filter($tap_flow_rates, function($rate) { return $rate <= 0; })) {
        throw new ValueError("Tap flow rates must be positive.");
    }
    if (!is_int($walking_time_per_person) || $walking_time_per_person < 0) {
        throw new ValueError("Walking time per person must be a non-negative number.");
    }
    
    $total_time = 0;
    while ($queue) {
        $total_time += $walking_time_per_person * count($queue);
        $fastest_tap_index = array_search(max($tap_flow_rates), $tap_flow_rates);
        $fill_time = array_shift($queue) / $tap_flow_rates[$fastest_tap_index];
        $total_time += $fill_time;
    }
    return $total_time;
}

$queue = [400, 750, 1000];
$tap_flow_rates = [50, 200];
$walking_time_per_person = 2;
echo "Total time required: " . calculate_fill_time_with_flow_rates($queue, $tap_flow_rates, $walking_time_per_person) . " seconds\n";


function calculate_fill_time_and_flow_rate_with_flow_rates($queue, $tap_flow_rates, $walking_time_per_person) {
    if (!is_array($queue) || !array_filter($queue, 'is_int')) {
        throw new TypeError("Queue must be an array of integers.");
    }
    if (!is_array($tap_flow_rates) || !array_filter($tap_flow_rates, 'is_numeric')) {
        throw new TypeError("Tap flow rates must be an array of numbers.");
    }
    if (array_filter($tap_flow_rates, function($rate) { return $rate <= 0; })) {
        throw new ValueError("Tap flow rates must be positive.");
    }
    if (!is_int($walking_time_per_person) || $walking_time_per_person < 0) {
        throw new ValueError("Walking time per person must be a non-negative number.");
    }
    
    $total_time = 0;
    while ($queue) {
        $total_time += $walking_time_per_person * count($queue);
        $fastest_tap_index = array_search(max($tap_flow_rates), $tap_flow_rates);
        $fill_time = array_shift($queue) / $tap_flow_rates[$fastest_tap_index];
        $total_time += $fill_time;
    }
    return [$total_time, $tap_flow_rates[$fastest_tap_index]];
}

$queue = [400, 750, 1000];
$tap_flow_rates = [50, 200];
$walking_time_per_person = 2;
[$total_time, $used_flow_rate] = calculate_fill_time_and_flow_rate_with_flow_rates($queue, $tap_flow_rates, $walking_time_per_person);
echo "Total time required: $total_time seconds\n";
echo "Flow rate of the tap used: $used_flow_rate ml/s\n";

?>
