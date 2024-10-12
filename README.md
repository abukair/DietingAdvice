# DietingAdvice
 Determine your dieting info/goals.

## Overview
This Diet Advising Program is an interactive command-line tool designed to help users calculate their Basal Metabolic Rate (BMR), Body Mass Index (BMI), Total Daily Energy Expenditure (TDEE), and suggested daily protein intake. BMR, a value that is essential to the functionality of the program, is calculated using the Mifflen St-Jeor equation. Based on user input like age, sex, weight, height, activity level, and fitness goals, the program provides personalized dietary advice that helps with fat loss, muscle maintenance, bulking, or general weight management.

## Key Features:
BMI Calculation: Calculates body mass index based on weight, height, and unit preference (imperial or metric).
BMR Calculation: Calculates the basal metabolic rate.
TDEE Calculation: Calculates total daily energy expenditure based on user activity levels.
Dietary Goal Recommendations: Suggests caloric intake adjustments based on diet goals like weight loss, muscle gain, or maintenance.
Protein Intake: Provides a suggested daily protein intake to align with the user's fitness goals.

## How It Works
The program prompts the user for several inputs:

Age: (18-65) Age in years for calculating BMR.
Units: Choice between Imperial (lbs, inches) and Metric (kg, cm).
Weight and Height: Collected in either lbs/inches or kg/cm.
Sex: Male or Female, used to adjust BMR calculations based on biological differences.
Activity Level: Users select from a scale of 1 (sedentary) to 5 (vigorous daily exercise).
Fitness Goals: Users choose their fitness focus (fat loss, bulking, maintenance).
Dieting Goals: Ranges from -2 (significant weight loss) to +2 (significant muscle gain).

## Requirements
Python 3.x
