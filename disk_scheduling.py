import sys

def read_requests(file_path):
    with open(file_path, 'r') as file:
        requests = [int(line.strip()) for line in file]
    return requests

def fcfs(requests, start):
    head_movements = 0
    current_position = start
    for request in requests:
        head_movements += abs(request - current_position)
        current_position = request
    return head_movements

def optimized_fcfs(requests, start):
    return fcfs(requests, start)

def scan(requests, start, total_cylinders):
    requests.sort()
    head_movements = 0
    current_position = start
    if (max(requests) - start) < (start - min(requests)):
        left_part = [r for r in requests if r <= start]
        right_part = [r for r in requests if r > start]
        for request in reversed(left_part):
            head_movements += abs(request - current_position)
            current_position = request
        if right_part:
            head_movements += current_position
            head_movements += right_part[0]
            current_position = right_part[0]
        for request in right_part:
            head_movements += abs(request - current_position)
            current_position = request
    else:
        left_part = [r for r in requests if r <= start]
        right_part = [r for r in requests if r > start]
        for request in right_part:
            head_movements += abs(request - current_position)
            current_position = request
        if left_part:
            head_movements += (total_cylinders - 1 - current_position)
            head_movements += (total_cylinders - 1 - left_part[-1])
            current_position = left_part[-1]
        for request in reversed(left_part):
            head_movements += abs(request - current_position)
            current_position = request
    return head_movements

def optimized_scan(requests, start, total_cylinders):
    requests.sort()
    head_movements = 0
    current_position = start
    left_part = [r for r in requests if r <= start]
    right_part = [r for r in requests if r > start]
    for request in reversed(left_part):
        head_movements += abs(request - current_position)
        current_position = request
    for request in right_part:
        head_movements += abs(request - current_position)
        current_position = request
    return head_movements

def cscan(requests, start, total_cylinders):
    head_movements = 0
    current_position = start

    requests_above = [req for req in requests if req >= start]
    requests_below = [req for req in requests if req < start]

    for request in requests_above:
        head_movements += abs(request - current_position)
        current_position = request

    if requests_below:
        head_movements += total_cylinders - 1 - current_position  
        head_movements += total_cylinders - 1  
        current_position = 0

        for request in requests_below:
            head_movements += abs(request - current_position)
            current_position = request

    return head_movements


def optimized_cscan(requests, start, total_cylinders):
    requests.sort()
    head_movements = 0
    current_position = start
    
    index = 0 
    while index < len(requests) and requests[index] < start:
        index += 1
    
    for i in range(index, len(requests)):
        head_movements += abs(requests[i] - current_position)
        current_position = requests[i]

    if index > 0: 
        head_movements += total_cylinders - 1 - current_position 
        head_movements += total_cylinders - 1  
        current_position = 0
        for i in range(index):
            head_movements += abs(requests[i] - current_position)
            current_position = requests[i]

    return head_movements
def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <initial_position> <file_path> <total_cylinders>")
        return

    start = int(sys.argv[1])
    file_path = sys.argv[2]
    total_cylinders = int(sys.argv[3])

    requests_initial = read_requests(file_path)
    
    # Using a copy of the original list for each call
    print("Total head movements for FCFS:", fcfs(requests_initial[:], start))
    print("Total head movements for SCAN:", scan(requests_initial[:], start, total_cylinders))
    print("Total head movements for C-SCAN:", cscan(requests_initial[:], start, total_cylinders))
    print("Total optimal head movements for FCFS:", fcfs(sorted(requests_initial[:]), start))
    print("Total optimal head movements for SCAN:", optimized_scan(requests_initial, start, total_cylinders))
    print("Total optimal head movements for C-SCAN:", optimized_cscan(requests_initial, start, total_cylinders))

if __name__ == "__main__":
    main()


