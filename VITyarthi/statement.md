# Project Statement

## Problem Statement

Keeping track of what you eat each day is hard work. Most calorie trackers make you search through long food databases just to log a simple meal, and this takes time and puts people off using them. Many people also do not know how much protein, fat or sugar is in their food, even though this matters for staying healthy. This project solves that problem by letting a user simply describe what they ate in simple English, such as "1 cup of milk and 2 eggs," and using AI to work out the nutrition for them straight away.

## Scope of the Project

This project is a command-line application built in Python. It covers:

- Creating a user account and logging in with a password
- Typing a food description and sending it to the Gemini AI model to get nutrition values
- Saving daily food logs for each user in a local file
- Showing a daily summary of calories, protein, fat and sugar, compared to standard RDA

The project does not cover a graphical interface, mobile app, or long term diet planning. It is meant to be a straightforward tool run from the terminal, not a full health platform.

## Target Users

This app is aimed at:

- Students or individuals who want a quick and easy way to track their daily food intake
- People who find typical calorie counting apps too slow or complex to use
- Anyone curious about the nutrition in everyday meals without needing to search a food database themselves

## High Level Features

- User registration and login, with passwords stored securely using **hashing**
- AI powered food analysis that turns a raw text food description into calorie, protein, fat and sugar values
- Automatic daily totals that add every item logged during the day
- A daily summary screen comparing the user's intake against standard recommended daily allowances
- Persistent storage, so a user's login details and food history is saved
