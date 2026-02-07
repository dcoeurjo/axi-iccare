# voice_control_axidraw.py

import speech_recognition as sr
import os
import subprocess

# Function to execute AxiDraw commands

def execute_axidraw(command):
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

# Initialize recognizer
recognizer = sr.Recognizer()

# Define AxiDraw command
axidraw_command = ["axidraw_command_here"]  # Replace with actual AxiDraw command

# Main loop
while True:
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            # Recognize speech
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")

            # Check for exit command
            if "stop" in command:
                print("Exiting.")
                break

            # Execute AxiDraw command
            execute_axidraw(axidraw_command)

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
