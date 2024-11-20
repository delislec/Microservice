import zmq
import json
import time 

# Set up ZeroMQ client
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Example user data
user_data = {
    "age": 30,
    "gender": "male",
    "weight": 70,  # in kg
    "height": 175,  # in cm
    "goal": "lose weight",
    "active_calories": 300
}

user_data_2 = {
    "age": 25,
    "gender": "male",
    "weight": 80,  # in kg
    "height": 175,  # in cm
    "goal": "gain muscle",
    "active_calories": 450
}

# Send data to microservice
print("Sending request to Microservice A...")
socket.send_json(user_data)

# Receive response
response = socket.recv_json()
time.sleep(.5)
print("Response received:")
print(json.dumps(response, indent=2))
