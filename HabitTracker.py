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

    def get_all_habits(self) -> List[tuple]:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM habits')
            return cursor.fetchall()

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

    def calculate_streak(self, dates: List[str], periodicity: str) -> int:
        if not dates:
            return 0
        streak = 1
        for i in range(len(dates) - 1, 0, -1):
            current = datetime.fromisoformat(dates[i])
            previous = datetime.fromisoformat(dates[i - 1])
            delta = timedelta(days=1 if periodicity == 'daily' else 7)
            if (current - previous).days <= delta.days:
                streak += 1
            else:
                break
        return streak

    def get_longest_streak(self, habit_id: int) -> int:
        completions = self.get_completions(habit_id)
        habit = self.get_habit_by_id(habit_id)
        return self.calculate_streak(completions, habit[2])

    def get_habit_by_id(self, habit_id: int):
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM habits WHERE id=?', (habit_id,))
            return cursor.fetchone()