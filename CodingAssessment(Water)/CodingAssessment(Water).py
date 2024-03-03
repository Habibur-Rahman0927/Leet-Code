def calculate_fill_time(queue, num_taps):
    total_time = 0
    while queue:
        for _ in range(min(num_taps, len(queue))):
            bottle_size = queue.pop(0)
            fill_time = bottle_size / 100  # 100ml per second
            total_time += fill_time
    return total_time

queue = [400, 750, 1000]
num_taps = 2
print("Total time required:", calculate_fill_time(queue, num_taps), "seconds")


def calculate_fill_time_with_input_validation(queue, num_taps):
    if not isinstance(queue, list) or not all(isinstance(x, int) for x in queue):
        raise TypeError("Queue must be a list of integers.")
    if not isinstance(num_taps, int) or num_taps <= 0:
        raise ValueError("Number of taps must be a positive integer.")
        
    total_time = 0
    while queue:
        for _ in range(min(num_taps, len(queue))):
            bottle_size = queue.pop(0)
            fill_time = bottle_size / 100  # 100ml per second
            total_time += fill_time
    return total_time

queue = [400, 750, 1000]
num_taps = 1
print("Total time required:", calculate_fill_time_with_input_validation(queue, num_taps), "seconds")

def calculate_fill_time_with_walking_time(queue, num_taps, walking_time_per_person):
    if not isinstance(queue, list) or not all(isinstance(x, int) for x in queue):
        raise TypeError("Queue must be a list of integers.")
    if not isinstance(num_taps, int) or num_taps <= 0:
        raise ValueError("Number of taps must be a positive integer.")
    if not isinstance(walking_time_per_person, (int, float)) or walking_time_per_person < 0:
        raise ValueError("Walking time per person must be a non-negative number.")
        
    total_time = 0
    while queue:
        # Add walking time for each person
        total_time += walking_time_per_person * min(num_taps, len(queue))
        for _ in range(min(num_taps, len(queue))):
            bottle_size = queue.pop(0)
            fill_time = bottle_size / 100  # 100ml per second
            total_time += fill_time
    return total_time

queue = [400, 750, 1000]
num_taps = 3
walking_time_per_person = 2  # 2 seconds walking time per person
print("Total time required:", calculate_fill_time_with_walking_time(queue, num_taps, walking_time_per_person), "seconds")

def calculate_fill_time_with_flow_rates(queue, tap_flow_rates, walking_time_per_person):
    if not isinstance(queue, list) or not all(isinstance(x, int) for x in queue):
        raise TypeError("Queue must be a list of integers.")
    if not isinstance(tap_flow_rates, list) or not all(isinstance(rate, (int, float)) for rate in tap_flow_rates):
        raise TypeError("Tap flow rates must be a list of numbers.")
    if not all(rate > 0 for rate in tap_flow_rates):
        raise ValueError("Tap flow rates must be positive.")
    if not isinstance(walking_time_per_person, (int, float)) or walking_time_per_person < 0:
        raise ValueError("Walking time per person must be a non-negative number.")
        
    total_time = 0
    while queue:
        total_time += walking_time_per_person * len(queue)
        fastest_tap_index = tap_flow_rates.index(max(tap_flow_rates))
        fill_time = queue.pop(0) / tap_flow_rates[fastest_tap_index]
        total_time += fill_time
    return total_time

queue = [400, 750, 1000]
tap_flow_rates = [50, 200]  
walking_time_per_person = 2 
print("Total time required:", calculate_fill_time_with_flow_rates(queue, tap_flow_rates, walking_time_per_person), "seconds")

def calculate_fill_time_and_flow_rate_with_flow_rates(queue, tap_flow_rates, walking_time_per_person):
    if not isinstance(queue, list) or not all(isinstance(x, int) for x in queue):
        raise TypeError("Queue must be a list of integers.")
    if not isinstance(tap_flow_rates, list) or not all(isinstance(rate, (int, float)) for rate in tap_flow_rates):
        raise TypeError("Tap flow rates must be a list of numbers.")
    if not all(rate > 0 for rate in tap_flow_rates):
        raise ValueError("Tap flow rates must be positive.")
    if not isinstance(walking_time_per_person, (int, float)) or walking_time_per_person < 0:
        raise ValueError("Walking time per person must be a non-negative number.")
        
    total_time = 0
    while queue:
        total_time += walking_time_per_person * len(queue)
        fastest_tap_index = tap_flow_rates.index(max(tap_flow_rates))
        fill_time = queue.pop(0) / tap_flow_rates[fastest_tap_index]
        total_time += fill_time
    return total_time, tap_flow_rates[fastest_tap_index]

queue = [400, 750, 1000]
tap_flow_rates = [50, 200]
walking_time_per_person = 2
total_time, used_flow_rate = calculate_fill_time_and_flow_rate_with_flow_rates(queue, tap_flow_rates, walking_time_per_person)
print("Total time required:", total_time, "seconds")
print("Flow rate of the tap used:", used_flow_rate, "ml/s")


