# Microservice
Microservice A implementation for CS361: Calorie and Macronutrient Calculator

# Installation
The microservice only relies on ZeroMQ to send and recieve data

# Requesting Data
To send a request to the microservice:
1. Connect to the server at port 5555 using TCP protocol to a ZeroMQ socket
2. Send a JSON payload with the following structure:
   {
    "age": 30,
    "gender": "male",
    "weight": 70,
    "height": 175,
    "goal": "lose weight",
    "active_calories": 300
}

# Example of Requesting
import zmq

// Set up ZeroMQ client

context = zmq.Context()

socket = context.socket(zmq.REQ)

socket.connect("tcp://localhost:5555")

// Define request payload

request_payload = {
    "age": 30,
    "gender": "male",
    "weight": 70,
    "height": 175,
    "goal": "lose weight",
    "active_calories": 300
}

// Send request to the microservice

socket.send_json(request_payload)

print("Request sent!")

# Receiving Data
After sending a request, wait for a response:

1. Use the recv_json() method to receive the response.

2. Parse the JSON response for the calculated calories and macros.

# Receive response from the microservice
response = socket.recv_json()

print("Response received:")

print(response)

# Example Output of Payload
{
    "total_calories": 2000,
    "macros": {
        "carbs": 200.0,
        "protein": 150.0,
        "fats": 66.7
    }
}


