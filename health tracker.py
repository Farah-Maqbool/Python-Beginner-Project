#Question 4: Health Tracker App
#Create a function check_activity_goal(steps_taken, goal) for a Health Tracker App. If the user has 
#achieved their daily step goal (given as input), return "Goal achieved," otherwise, provide a message 
#indicating how many more steps are needed to reach the goal.
# Input that user use this app for disease or diet
def check_activity_goal(task,goal):
    Morning,Exercise,Breakfast,Lunch,Evening,Dinner=task
    Morning_done=input(f"you drink {Morning} in Morning (yes or no): ")
    Exercise_done=input(f"you do {Exercise} today (yes or no): ")
    Breakfast_done=input(f"you Eat {Breakfast} in Breakfast (yes or no): ")
    lunch_done=input(f"you Eat {Lunch} in Lunch (yes or no): ")
    Evening_done=input(f"you Eat {Evening} in Evening (yes or no): ")
    Dinner_done=input(f"you Eat {Dinner} in Dinner (yes or no): ")
    if Morning_done=="yes" and Exercise_done=="yes" and Breakfast_done=="yes" and lunch_done=="yes" and Evening_done=="yes" and Dinner_done=="yes":
        return f"Congratulations You achieved your goal {goal} :)"
    list_task=[Morning_done,Exercise_done,Breakfast_done,lunch_done,Evening_done,Dinner_done]
    result=list_task.count("no")
    return f"Your {result} steps are needed to complete your goal"
goal=input("Goal: ")
parts_of_day = ["Morning", "Exercise", "Breakfast", "Lunch", "Evening", "Dinner"]
tasks=[]
for part in parts_of_day:
    task_input = input(f"{part}: ")
    tasks.append(task_input)
result=check_activity_goal(tasks,goal)
print(result)



