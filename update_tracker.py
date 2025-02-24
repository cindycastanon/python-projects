def update_study_tracker():
    # Collect user input
    week = input("Enter the week number: ")
    project = input("Enter the project completed: ")
    problems = input("Enter the number of LeetCode problems solved: ")

    # Prepare the new row for the Markdown table
    new_entry = f"| {week}    | {project}   | {problems}                        |\n"

    # Update the study-tracker.md file
    with open("study-tracker.md", "a") as file:
        file.write(new_entry)

    print(f"\n✅ Study tracker updated for Week {week}!\n")

if __name__ == "__main__":
    update_study_tracker()