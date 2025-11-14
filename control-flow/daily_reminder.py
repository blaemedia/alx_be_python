# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Enter the priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        reminder = f"High priority task: {task}"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += " - address this soon."
    
    case "medium":
        reminder = f"Medium priority task: {task}"
        if time_bound == "yes":
            reminder += " - try to complete this today."
        else:
            reminder += " - schedule this for the week."
    
    case "low":
        reminder = f"Low priority task: {task}"
        if time_bound == "yes":
            reminder += " - complete when you have free time."
        else:
            reminder += " - no rush on this task."
    
    case _:
        reminder = "Invalid priority level entered."

# Provide a Customized Reminder
print(reminder)