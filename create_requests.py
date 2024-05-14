import random

def create_request_file(filename, num_requests, max_cylinder):
    with open(filename, 'w') as file:
        for _ in range(num_requests):
            request = random.randint(0, max_cylinder - 1)
            file.write(f"{request}\n")

# Settings
filename = 'disk_requests.txt'
num_requests = 1000
max_cylinder = 5000

# Generate the file
create_request_file(filename, num_requests, max_cylinder)

print(f"File '{filename}' with {num_requests} requests has been created.")
