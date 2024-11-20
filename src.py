import zmq
import json
import time 

def calculate_calories_and_macros(data):
    # Extract user data
    age = data['age']
    gender = data['gender']
    weight = data['weight']  # in kg
    height = data['height']  # in cm
    goal = data['goal']
    active_calories = data['active_calories']

    # Basal Metabolic Rate (BMR) calculation using Mifflin-St Jeor Equation
    if gender.lower() == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender.lower() == "female":
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    else:
        return {"error": "Invalid gender"}

    # Adjust based on goal
    if goal.lower() == "lose weight":
        calories = bmr - 500
        macro_dist = {"carbs": 0.3, "protein": 0.4, "fats": 0.3}
    elif goal.lower() == "gain weight":
        calories = bmr + 500
        macro_dist = {"carbs": 0.4, "protein": 0.3, "fats": 0.3}
    elif goal.lower() == "gain muscle":
        calories = bmr + 300
        macro_dist = {"carbs": 0.4, "protein": 0.35, "fats": 0.25}
    else:
        calories = bmr
        macro_dist = {"carbs": 0.4, "protein": 0.3, "fats": 0.3}

    # Add active calories burned
    total_calories = calories + active_calories

    # Macronutrient distribution
    macros = {
        "carbs": total_calories * macro_dist["carbs"] / 4,  # 4 kcal per gram of carbs
        "protein": total_calories * macro_dist["protein"] / 4,  # 4 kcal per gram of protein
        "fats": total_calories * macro_dist["fats"] / 9,  # 9 kcal per gram of fat
    }

    rounded_calories = round(total_calories)
    rounded_macros = {key: round(value) for key, value in macros.items()}

    return {
        "total_calories": rounded_calories,
        "macros": rounded_macros
    }

# Set up ZeroMQ server
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print("Microservice A is running...")
while True:
     # Receive a JSON message sent to this service via the ZeroMQ socket
    message = socket.recv_json()
    
    # Simulate a slight delay in processing the request
    time.sleep(0.5)
    
    # Log the received request for debugging or informational purposes
    print(f"Received request: {message}")
    
    # Process the request using a function that calculates calorie and macronutrient values
    response = calculate_calories_and_macros(message)
    
    # Send the calculated response back to the requester via the ZeroMQ socket
    socket.send_json(response)
