# Calorie Tracker

## Overview 

This is a simple command line program to help you track what you eat. Using the GEMINI_API_KEY. Instead of looking up food in a big database overall over the internet, you just type what you had; like "1 cup of milk and 2 eggs" and it gives the calories, protein, fat and sugar in it.

Everyone can make their own account, track their meals and get a daily summary showing how their food stacks up against the recommended amounts a person should eat in a day.

## Features

**User accounts** - you can set up a username and password and log in at a later date. Passwords are saved securely. 
**AI Food Logging** - Describe what you ate in English and the API prompts Gemini to estimate nutrition for you.
**Daily totals** - Each food you log is added to a running total for the day.
**Daily summary** - see your calories, protein, fat and sugar for the day, next to the standard recommended daily amount (RDA), with a percentage of how close you are.
**Saved history** - your logs are saved in a file, so they are saved to the next time you run the code

## Technologies used

**Python** — the entire program is written in Python
**Google Gemini API** (`google-genai` package) - used to find nutrition of a food description
**JSON files** – used for storing user accounts (`users.json`) and food logs (`logs.json`)
**hashlib** — used for password security

## Steps to install and run

1. Ensure that you have Python installed on your computer.
2. Run this command on your terminal to install the Gemini API package:
   
   Install google-genai with pip: pip set up google-genai
   
3. Obtain a Gemini API key from Google ( https://aistudio.google.com/api-keys?project=gen-lang-client-0089455607 ) and set it as an environment variable called `GEMINI_API_KEY`:

   - On Windows: `$env:GEMINI_API_KEY="your_key_here"`
   - On Mac/Linux: `export GEMINI_API_KEY=your_key_here`
4. Execute the program:
python VIT.py
   
5. Use the on-screen menu to sign up, sign in and begin logging food.

## Instructions for testing

1. At the start of the program, click **Register**. Choose a username and password.
2. Sign in with the same login credentials.
3. Choose **Log Food** and enter something, e.g. "a banana and a glass of orange juice".
4. Ensure AI returns items with calorie and nutrient values.
5. Select **View Today’s Summary** and make sure the numbers match.
6. Log out and log back in. Check whether the data was saved.
7. Use unusual input or leave it blank and see if it can handle errors.

## Screenshots

Test Successful:

<img width="517" height="85" alt="Screenshot 2026-09-30 195709" src="https://github.com/user-attachments/assets/f03411bb-e09e-4ca3-bf07-8cd4ed16f452" />

Invalid User:
<img width="1094" height="156" alt="Screenshot 2026-09-30 212922" src="https://github.com/user-attachments/assets/8731cffe-c391-4610-89e9-20b022a73af3" />

User Registered:
<img width="1124" height="110" alt="Screenshot 2026-09-30 213108" src="https://github.com/user-attachments/assets/6c9c0de9-13ff-4f21-bfbf-4f4bd11f0b0d" />

Calories Tracked:
<img width="1131" height="242" alt="Screenshot 2026-09-30 213142" src="https://github.com/user-attachments/assets/99396b33-fd46-48f0-b6db-fea9e5e7c2d8" />

Invalid Input:
<img width="1142" height="86" alt="Screenshot 2026-09-30 213230" src="https://github.com/user-attachments/assets/ba5edcf7-e5fe-45da-9b18-7ca62ebd921c" />

Food Summary:
<img width="1122" height="136" alt="Screenshot 2026-09-30 213254" src="https://github.com/user-attachments/assets/a38c19cb-8b36-4d91-af16-30136f31bf24" />

Logout & Exit:
<img width="1115" height="128" alt="Screenshot 2026-09-30 213420" src="https://github.com/user-attachments/assets/7ee137b3-f0bf-4c9e-9279-bafa7913d78e" />
