#!/usr/bin/env python3
"""
Personal Daily Reminder
Provides customized reminders for a single task based on priority and time sensitivity
"""

def main():
    print("🌟 Personal Daily Reminder 🌟")
    print("-" * 30)
    
    # Prompt for task information
    task = input("Enter your task: ").strip()
    
    # Get priority with validation loop
    while True:
        priority = input("Priority (high/medium/low): ").strip().lower()
        if priority in ['high', 'medium', 'low']:
            break
        print("Please enter 'high', 'medium', or 'low'")
    
    # Get time-bound status with validation loop
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
        if time_bound in ['yes', 'no']:
            break
        print("Please enter 'yes' or 'no'")
    
    print("\n" + "=" * 50)
    print("REMINDER:")
    print("=" * 50)
    
    # Process task using match case for priority
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"🚨 '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"⚠️  '{task}' is a high priority task. Please address it soon.")
        
        case "medium":
            if time_bound == "yes":
                print(f"📅 '{task}' is a medium priority task with a time constraint. Plan to complete it today.")
            else:
                print(f"📋 '{task}' is a medium priority task. Schedule it for this week.")
        
        case "low":
            if time_bound == "yes":
                print(f"⏰ '{task}' is a low priority task but has a time limit. Complete it when possible.")
            else:
                print(f"📚 Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    
    print("=" * 50)
    print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
    print("\n🚀 Click here to tweet! 🚀")

if __name__ == "__main__":
    main()
