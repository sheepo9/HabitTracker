from HabitTracker import HabitTracker
from Habit import Habit
import questionary

def main():
    tracker = HabitTracker()
    while True:
        choice = questionary.select(
            "Habit Tracker - Choose an option:",
            choices=[
                "Add Habit",
                "Complete Habit",
                "View All Habits",
                "View Habits by Periodicity",
                "View Longest Streak for Habit",
                "Exit"
            ]).ask()

        if choice == "Add Habit":
            name = questionary.text("Enter habit name:").ask()
            periodicity = questionary.select("Enter periodicity:", choices=["daily", "weekly"]).ask()
            tracker.add_habit(Habit(name, periodicity))

        elif choice == "Complete Habit":
            habits = tracker.get_all_habits()
            habit_choices = [f"{h[0]}: {h[1]}" for h in habits]
            selected = questionary.select("Select habit to complete:", choices=habit_choices).ask()
            habit_id = int(selected.split(":")[0])
            tracker.complete_task(habit_id)

        elif choice == "View All Habits":
            for habit in tracker.get_all_habits():
                print(habit)

        elif choice == "View Habits by Periodicity":
            period = questionary.select("Select periodicity:", choices=["daily", "weekly"]).ask()
            for habit in tracker.get_habits_by_periodicity(period):
                print(habit)

        elif choice == "View Longest Streak for Habit":
            habits = tracker.get_all_habits()
            habit_choices = [f"{h[0]}: {h[1]}" for h in habits]
            selected = questionary.select("Select habit:", choices=habit_choices).ask()
            habit_id = int(selected.split(":")[0])
            streak = tracker.get_longest_streak(habit_id)
            print(f"Longest streak for habit {habit_id}: {streak}")

        elif choice == "Exit":
            break

if __name__ == "__main__":
    main()
