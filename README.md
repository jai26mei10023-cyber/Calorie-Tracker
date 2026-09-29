# Calorie Tracker

## Overview

This is a simple command-line program that helps you keep track of what you eat. Instead of looking up food in a big database or all over the internet, you just type what you had; like "1 cup of milk and 2 eggs" and the gives the calories, protein, fat and sugar in it, using the GEMINI_API_KEY.

Each person can make their own account, log their meals, and see a daily summary showing how their food compares to the recommended amounts a person should eat in a day.

## Features

**User accounts** — you can register a username and password, and log in later. Passwords are stored safely using hashing, not as plain text.
**AI food logging** — type a description of what you ate in normal English, and the app asks Gemini to estimate the nutrition for you.
**Daily totals** — every food item you log gets added up into a running total for the day.
**Daily summary** — see your calories, protein, fat and sugar for the day, next to the standard recommended daily amount (RDA), with a percentage showing how close you are.
**Saved history** — your logs are saved in a file, so they're still there next time you run the code

## Technologies used

**Python** — the whole program is written in Python
**Google Gemini API** (`google-genai` package) — used to work out nutrition from a food description
**JSON files** — used to store user accounts (`users.json`) and food logs (`logs.json`)
**hashlib** — used to keep passwords secure

## Steps to install and run

1. Make sure you have Python installed on your computer.
2. Install the Gemini API package by running this in your terminal:
   
   'pip install google-genai'
   
3. Get a Gemini API key from Google(https://aistudio.google.com/api-keys?project=gen-lang-client-0089455607), then set it as an environment variable called `GEMINI_API_KEY`:
   - On Windows: `$env:GEMINI_API_KEY="your_key_here"`
   - On Mac/Linux: `export GEMINI_API_KEY="your_key_here"`
4. Run the program:
   
   'python VIT.py'
   
5. Follow the on-screen menu to register, log in, and start logging food.

## Instructions for testing

1. Start the program and choose **Register**. Pick a username and password.
2. Log in with the same details.
3. Choose **Log Food** and type something , like "a banana and a glass of orange juice".
4. Check that the AI returns items with calorie and nutrient values.
5. Choose **View Today's Summary** and check the numbers match what you logged.
6. Log out and log back in again to make sure your data was saved.
7. Try typing something odd/different or leaving it blank to see how the program handles errors.

<img width="865" height="403" alt="Screenshot 2026-09-27 203242" src="https://github.com/user-attachments/assets/45bd61cf-9995-47cd-a8d7-dad6fac47a9f" />
<img width="871" height="572" alt="Screenshot 2026-09-27 203214" src="https://github.com/user-attachments/assets/035c2f35-761a-411e-b7ae-1c62b052bd5f" />
<img width="812" height="106" alt="Screenshot 2026-09-27 203142" src="https://github.com/user-attachments/assets/c22fb96e-1456-4a34-8b21-f1f06922a65d" />
