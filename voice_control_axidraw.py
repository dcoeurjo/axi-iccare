import speech_recognition as sr
from pyaxidraw import axidraw

# Initialize the recognizer and AxiDraw
recognizer = sr.Recognizer()
ad = axidraw.AxiDraw()

def setup_axidraw():
    """Setup and connect to AxiDraw."""
    ad.interactive()
    ad.connect()

def draw_circle():
    """Example function to draw a circle using AxiDraw."""
    setup_axidraw()
    ad.moveto(5, 5)  # Move to starting position
    ad.circle(2)     # Draw a circle with radius 2
    ad.disconnect()

def draw_square():
    """Example function to draw a square using AxiDraw."""
    setup_axidraw()
    ad.moveto(3, 3)  # Move to starting position
    ad.lineto(3, 6)  # Draw square sides
    ad.lineto(6, 6)
    ad.lineto(6, 3)
    ad.lineto(3, 3)
    ad.disconnect()

def recognize_speech_and_draw():
    """Listen through the microphone and control the AxiDraw based on speech."""
    print("Listening for commands. Say something like 'draw a circle' or 'draw a square'...")
    with sr.Microphone() as source:
        try:
            # Listen to the audio
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            
            # Convert Speech to Text
            command = recognizer.recognize_google(audio).lower()
            print(f"Heard: {command}")
            
            # Map commands to AxiDraw actions
            if "circle" in command:
                draw_circle()
                print("Done drawing a circle!")
            elif "square" in command:
                draw_square()
                print("Done drawing a square!")
            else:
                print("Command not recognized. Please try again!")

        except sr.UnknownValueError:
            print("Could not understand the audio. Please try again.")
        except sr.RequestError as e:
            print(f"Error connecting to the recognition service: {e}")

if __name__ == "__main__":
    while True:
        recognize_speech_and_draw()