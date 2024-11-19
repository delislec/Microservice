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

