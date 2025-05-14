# ---------------------------- cli.py ---------------------------- #
from HabitTracker import HabitTracker
from Habit import Habit
import questionary

def main():
    tracker = HabitTracker()
    # Printing a welcome message
    print("=========================================================================")
    print("|                                                                       |")
    print("|                                TrackWise                              |")
    print("|                                We Track It                            |")
    print("|                                                                       |")
    print("=========================================================================")


    while True:
        choice = questionary.select(
            "Habit Tracker - Choose an option:",
            choices=[
                "Add Habit",
                "Complete Habit",
                "View All Habits",
                "Analyze Habits",
                "Delete Habit",
                "Exit"
            ]).ask()

        if choice == "Add Habit":
            name = questionary.text("Enter habit name:").ask()
            periodicity = questionary.select("Enter periodicity:", choices=["daily", "weekly"]).ask()
            tracker.add_habit(Habit(name, periodicity))

        elif choice == "Complete Habit":
            habits = tracker.get_all_habits()
            if not habits:
                print("No habits found.")
                continue
            habit_choices = [f"{h[0]}: {h[1]}" for h in habits]
            selected = questionary.select("Select habit to complete:", choices=habit_choices).ask()
            habit_id = int(selected.split(":")[0])
            tracker.complete_task(habit_id)

        elif choice == "View All Habits":
            habits = tracker.get_all_habits()
            if not habits:
                print("No habits available.")
            else:
                for habit in habits:
                    print(habit)

        elif choice == "Analyze Habits":
            analysis_choice = questionary.select(
                "Choose analysis type:",
                choices=[
                    "View Habits by Periodicity",
                    "View Longest Streak for Habit",
                    "View Current Streak for Habit",
                    "View Broken Habits",
                    "Back"
                ]).ask()

            if analysis_choice == "View Habits by Periodicity":
                period = questionary.select("Select periodicity:", choices=["daily", "weekly"]).ask()
                habits = tracker.get_habits_by_periodicity(period)
                if not habits:
                    print(f"No {period} habits found.")
                else:
                    for habit in habits:
                        print(habit)

            elif analysis_choice == "View Longest Streak for Habit":
                habits = tracker.get_all_habits()
                if not habits:
                    print("No habits to analyze.")
                    continue
                habit_choices = [f"{h[0]}: {h[1]}" for h in habits]
                selected = questionary.select("Select habit:", choices=habit_choices).ask()
                habit_id = int(selected.split(":")[0])
                streak = tracker.get_longest_streak(habit_id)
                print(f"Longest streak for habit {habit_id}: {streak}")
            elif analysis_choice == "View Current Streak for Habit":
                habits = tracker.get_all_habits()
                if not habits:
                    print("No habits to analyze.")
                    continue
                habit_choices = [f"{h[0]}: {h[1]}" for h in habits]
                selected = questionary.select("Select habit:", choices=habit_choices).ask()
                habit_id = int(selected.split(":")[0])
                streak = tracker.get_current_streak(habit_id)
                print(f"Current streak for habit {habit_id}: {streak}")
            elif analysis_choice == "View Broken Habits":
                broken = tracker.get_broken_habits()
                if not broken:
                    print("No broken habits found.")
                else:
                    print("Broken Habits:")
                    for habit in broken:
                        print(habit)
            elif analysis_choice == "Back":
                continue
        elif choice == "Delete Habit":
            habits = tracker.get_all_habits()
            if not habits:
                print("No habits to delete.")
                continue
            habit_choices = [f"{h[0]}: {h[1]}" for h in habits]
            selected = questionary.select("Select habit to delete:", choices=habit_choices).ask()
            habit_id = int(selected.split(":")[0])

            confirm = questionary.confirm(f"Are you sure you want to delete habit ID {habit_id}?").ask()
            if confirm:
                tracker.delete_habit(habit_id)
                print("Habit deleted successfully.")
            else:
                print("Deletion cancelled.")

        elif choice == "Exit":
            break

if __name__ == "__main__":
    main()
