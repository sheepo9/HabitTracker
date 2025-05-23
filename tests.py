# --------------------- seed_data.py --------------------- #
from HabitTracker import HabitTracker
from Habit import Habit
from datetime import datetime, timedelta

# Initialize the HabitTracker
tracker = HabitTracker()

# Create dummy habits
habits = [
    Habit(name="Exercise", periodicity="daily"),
    Habit(name="Read Book", periodicity="daily"),
    Habit(name="Meditate", periodicity="weekly"),
    Habit(name="Journal", periodicity="monthly")  # New monthly habit
]

# Add habits to the tracker
for habit in habits:
    tracker.add_habit(habit)

# Function to add dummy completions
def add_completions(habit_id, days=5, interval='daily'):
    for i in range(days):
        date = datetime.now() - timedelta(days=i if interval == 'daily' else i * 7)
        tracker.complete_task(habit_id)

# Get all habits from the tracker
habit_list = tracker.get_all_habits()

# Add completions for each habit based on its periodicity
for h in habit_list:
    if h[1] == "daily":
        add_completions(h[0], days=28, interval='daily')  # 4 weeks of daily completions
    elif h[1] == "weekly":
        add_completions(h[0], days=4, interval='weekly')  # 4 weeks of weekly completions
    elif h[1] == "monthly":
        add_completions(h[0], days=4, interval='monthly')  # 4 months of monthly completions
