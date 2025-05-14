import sqlite3
from datetime import datetime, timedelta
from typing import List
from Habit import Habit
from db import init_db, DB_NAME

class HabitTracker:
    def __init__(self):
        init_db()

    def add_habit(self, habit: Habit):
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO habits (name, periodicity, creation_date) VALUES (?, ?, ?)',
                           (habit.name, habit.periodicity, habit.creation_date))
            conn.commit()

    def complete_task(self, habit_id: int):
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO completions (habit_id, completion_date) VALUES (?, ?)',
                           (habit_id, datetime.now().isoformat()))
            conn.commit()

# Fetches all habits stored in the database.
    def get_all_habits(self) -> List[tuple]:
        # Connect to the SQLite database using a context manager
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()

            # Execute a SQL query to select all rows from the 'habits' table
            cursor.execute('SELECT * FROM habits')
            return cursor.fetchall() # Return all fetched rows as a list of tuples

#Retrieves all habits that match a specific frequency (e.g., daily or weekly).
    def get_habits_by_periodicity(self, periodicity: str) -> List[tuple]:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM habits WHERE periodicity=?', (periodicity,))
            return cursor.fetchall()
   
    def get_completions(self, habit_id: int) -> List[str]:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT completion_date FROM completions WHERE habit_id=? ORDER BY completion_date', (habit_id,))
            return [row[0] for row in cursor.fetchall()]

   #calculate_streak aims to calculate how many times in a row (consecutively) a habit was completed based on its daily or weekly tracking frequency.
    def calculate_streak(self, dates: List[str], periodicity: str) -> int:
        if not dates:
            return 0 # Return 0 if there are no completion dates

        streak = 1 # Start the streak count at 1 (minimum streak)
        # Iterate through the list of dates in reverse order (latest to earliest)
        for i in range(len(dates) - 1, 0, -1):

            # Convert the current and previous dates from ISO format (e.g. '2025-05-10') to datetime objects
            current = datetime.fromisoformat(dates[i])
            previous = datetime.fromisoformat(dates[i - 1])

            # Set the expected time gap between completions based on periodicity
            delta = timedelta(days=1 if periodicity == 'daily' else 7)
            # If the difference between the current and previous date is within the allowed range (1 day or 7 days)
            if (current - previous).days <= delta.days:
                streak += 1
            else:
                break # The streak is broken; stop counting
        return streak   # Return the total streak count

#get_longest_streak is designed to retrieve the longest streak of completions for a specific habit, using the habit's ID
    def get_longest_streak(self, habit_id: int) -> int:
        completions = self.get_completions(habit_id)# Gets all completion dates
        habit = self.get_habit_by_id(habit_id)# Retrieves habit details (e.g., frequency)
        return self.calculate_streak(completions, habit[2]) # return the longest streak based on completions and periodicity(habit[2] represent the period)

# This function receives an id and return the habit based on the id
    def get_habit_by_id(self, habit_id: int):
        with sqlite3.connect(DB_NAME) as conn: # Connect to the SQLite database using a context manager
            cursor = conn.cursor() # Create a cursor object to execute SQL commands

            # Execute a SELECT query to fetch the habit with the given ID
            cursor.execute('SELECT * FROM habits WHERE id=?', (habit_id,))

            # Return the first matching record (or None if not found)
            return cursor.fetchone()

# Deletes a habit and all associated completions from the database
    def delete_habit(self, habit_id: int):
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()

            # First, delete all completions associated with the habit
            cursor.execute('DELETE FROM completions WHERE habit_id=?', (habit_id,))

            # Then, delete the habit itself
            cursor.execute('DELETE FROM habits WHERE id=?', (habit_id,))

            conn.commit()  # Commit the transaction to apply changes
    # Returns a list of broken habits (not completed within expected timeframe)


    def get_broken_habits(self) -> List[tuple]:
        broken_habits = []
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM habits")
            habits = cursor.fetchall()

            for habit in habits:
                habit_id, name, periodicity, creation_date = habit
                cursor.execute("SELECT MAX(completion_date) FROM completions WHERE habit_id=?", (habit_id,))
                last_completion = cursor.fetchone()[0]

                # If there's no completion at all
                if not last_completion:
                    broken_habits.append(habit)
                    continue

                last_date = datetime.fromisoformat(last_completion)
                now = datetime.now()
                delta = timedelta(days=1 if periodicity == 'daily' else 7)

                # If current time exceeds last completion + delta => broken
                if now > last_date + delta:
                    broken_habits.append(habit)

        return broken_habits

# Returns the current ongoing streak for a habit
    def get_current_streak(self, habit_id: int) -> int:
            completions = self.get_completions(habit_id)
            if not completions:
                return 0

            habit = self.get_habit_by_id(habit_id)
            periodicity = habit[2]
            delta = timedelta(days=1 if periodicity == 'daily' else 7)

            # Convert the last completion date
            last_date = datetime.fromisoformat(completions[-1])
            now = datetime.now()

            # Check if current date is within the allowed range to keep the streak alive
            if now - last_date <= delta:
                return self.calculate_streak(completions, periodicity)
            else:
                return 0  # Streak is broken
