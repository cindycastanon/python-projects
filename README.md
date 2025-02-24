# 📚 GitHub Project Structure for Python Projects

## 🗂️ **Main Directory Structure**
```
python-projects/
├── README.md          # Project overview and instructions
├── .gitignore         # Ignore unnecessary files
├── projects/          # Individual project folders
│   ├── 01_calculator/ 
│   │   ├── calculator.py      # Python code
│   │   ├── README.md          # Project-specific info
│   │   └── example_input.txt  # Example input file
│   ├── 02_todo_list/
│   │   ├── todo.py            # To-do list app
│   │   ├── README.md          # Project-specific info
│   │   └── tasks.txt          # Example task list
│   ├── 05_hello_world/        # New project folder
│   │   ├── hello.py           # Python code
│   │   └── README.md          # Project-specific info
│   └── ...
├── resources/         # Books, guides, and notes
│   ├── Python_Crash_Course.pdf
│   └── Grokking_Algorithms.pdf
└── study-tracker.md   # Weekly progress tracker
```

---

## 📖 **README.md (Main Repo)**
```markdown
# 🚀 Python Projects by Jennifer Eberhardt

This repository contains my Python projects as I advance from beginner to intermediate level.

## 📜 Project List
1. 📝 [Simple Calculator](projects/01_calculator/)
2. ✅ [To-Do List App](projects/02_todo_list/)
3. 📚 [Word Frequency Counter](projects/03_word_counter/)
4. 🌦️ [Weather App](projects/04_weather_app/)
5. 👋 [Hello World](projects/05_hello_world/)

## ⚙️ How to Run
1. Clone the repo:
```bash
git clone https://github.com/yourusername/python-projects.git
```
2. Go to any project folder and run the Python script:
```bash
cd projects/01_calculator
python calculator.py
```

## 🛠️ Steps to Add a New Project
1. **Create Project Folder:**
   - Inside `projects/`, create a new folder for each project, like `06_new_project/`.

2. **Add Files:**
   - Add your Python code, like `main.py`.
   - Create a `README.md` inside the project folder to describe what it does.

3. **Commit and Push:**
   ```bash
   git add .
   git commit -m "Add new project: 06_new_project"
   git push origin main
   ```

## 🙌 Contributions
Feel free to fork this repo and submit pull requests!
```

---

## 📅 **Study Tracker (study-tracker.md)**
```markdown
# 🕰️ Study Progress Tracker

| Week | Topics Covered            | LeetCode Problems Solved | Projects Completed        |
|-----|----------------------------|--------------------------|---------------------------|
| 1   | Python Basics, Functions  | Two Sum, Palindrome      | Simple Calculator         |
| 2   | OOP, File Handling        | Merge Two Lists, Climbing| To-Do List App            |
| 3   | Sorting, Recursion        | Valid Anagram, Group Ana | Word Frequency Counter    |
| 4   | Graphs, Trees             | Binary Tree Inorder      | Flask Blog                |
| 5   | APIs, Web Scraping        | Longest Substring        | Weather App               |
| 6   | Advanced Practice         | Merge Intervals, WordSea | News Scraper              |
```

---

💡 **Next Steps:**
1. Copy this structure to your GitHub repo.
2. Update `README.md` and `study-tracker.md` weekly.
3. Push new projects and solutions regularly.

