# HabitTracker
This application will focus on developing a backend of a habit tracking application using the Python 3.7+ with the following functionality; habit creation, task completion, streak tracking, and analytics.

## 📌 Features

* **Habit Creation**: Define new habits with customizable attributes.
* **Task Completion**: Mark habits as completed on specific dates.
* **Streak Tracking**: Monitor consecutive completions to build and maintain streaks.
* **Analytics**: Generate insights such as longest streaks and completion rates.
* **SQLite Integration**: Persist data using a lightweight SQLite database.
* **Unit Testing**: Ensure reliability through comprehensive test coverage.

## 🗂️ Project Structure

```

HabitTracker/
├── Habit.py             # Defines the Habit class and related methods
├── HabitTracker.py      # Core logic for managing habits
├── analytics.py         # Functions for analyzing habit data
├── db.py                # Handles database connections and operations
├── main.py              # Entry point for the application
├── tests.py             # Unit tests for the application
├── requirement.txt      # List of required Python packages
├── habit_tracker.db     # SQLite database file
└── README.md            # Project documentation
```



## ⚙️ Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/sheepo9/HabitTracker.git
   cd HabitTracker
   ```



2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```



3. **Install Dependencies**

   ```bash
   pip install -r requirement.txt
   ```



## 🚀 Usage

Run the main application:

```bash
python main.py
```



Follow the on-screen prompts to create habits, mark completions, and view analytics.([GitHub][1])

## 🧪 Running Tests

To execute the unit tests and ensure everything is working correctly:

```bash
python tests.py
```
## 📊 Analytics

The `analytics.py` module provides functions to analyze your habit data, including:

* **Longest Streak**: Identify the habit with the longest consecutive completion streak.
* **Completion Rates**: Calculate the percentage of completions over time.
* **Habit Trends**: Detect patterns and trends in habit performance.

## 📌 Requirements

* Python 3.7 or higher
* Packages listed in `requirement.txt`
## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.



