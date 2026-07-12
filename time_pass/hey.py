# Importing the required libraries
import time
import win32com.client

# Reading the text file
with open("document.txt", "r") as file:
    content = file.read()

# Splitting the text into words
words = content.split()

# Creating an instance of the keyboard
keyboard = win32com.client.Dispatch("WScript.Shell")

# Typing each word one by one
for word in words:
    print(word, end=" ")
    time.sleep(0.5)
    # Typing the word using the keyboard
    keyboard.SendKeys(word + " ")
