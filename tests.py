# --------------------- seed_data.py --------------------- #
from HabitTracker import HabitTracker
from Habit import Habit
from datetime import datetime, timedelta

tracker = HabitTracker()

# Create dummy habits
habits = [
    Habit(name="Exercise", periodicity="daily"),
    Habit(name="Read Book", periodicity="daily"),
    Habit(name="Meditate", periodicity="weekly")
]

for habit in habits:
    tracker.add_habit(habit)

# Add dummy completions
def add_completions(habit_id, days=5, interval='daily'):
    for i in range(days):
        date = datetime.now() - timedelta(days=i if interval == 'daily' else i * 7)
        tracker.complete_task(habit_id)

habit_list = tracker.get_all_habits()
for h in habit_list:
    add_completions(h[0], days=5, interval=h[2])
