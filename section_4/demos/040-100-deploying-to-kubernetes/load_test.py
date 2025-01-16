import requests
import threading
import time
import base64
import os

# Configuration
ENDPOINT_URL = "http://127.0.0.0:8000/predict"  
REQUESTS_PER_SECOND = 3  # Number of requests per second
DURATION = 60  # Duration of the load test in seconds

work_dir = os.path.dirname(os.path.abspath(__file__))

# Open image and encode it
with open(os.path.join(work_dir, 'dog-1.jpg'), 'rb') as img_file:
    base64_string = base64.b64encode(img_file.read()).decode('utf-8')

# JSON payload with the Base64 encoded image
payload = {
    "image": base64_string
}

# Set the headers
headers = {
    "Content-Type": "application/json"
}


# Function to send a single request
def send_request():
    try:
        response = requests.post(ENDPOINT_URL, json=payload, headers=headers)
        print(f"Response Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Function to simulate traffic
def load_test():
    start_time = time.time()
    threads = []

    while time.time() - start_time < DURATION:
        for _ in range(REQUESTS_PER_SECOND):
            thread = threading.Thread(target=send_request)
            thread.start()
            threads.append(thread)

        # Wait for 1 second before sending the next batch of requests
        time.sleep(1)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

# Run the load test
if __name__ == "__main__":
    print(f"Starting load test on {ENDPOINT_URL} for {DURATION} seconds...")
    load_test()
    print("Load test completed.")
