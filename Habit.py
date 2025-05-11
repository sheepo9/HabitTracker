from datetime import datetime
from typing import Optional

class Habit:
    def __init__(self, name: str, periodicity: str, creation_date: Optional[str] = None):
        self.name = name
        self.periodicity = periodicity
        self.creation_date = creation_date or datetime.now().isoformat()