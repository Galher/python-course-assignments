import re
from datetime import datetime, timedelta
from collections import defaultdict

# Step 1: Read the log file
with open("Day08/timelog.log", "r") as file:
    lines = file.readlines()

activity_log = []
activity_totals = defaultdict(timedelta)

time_format = "%H:%M"

# Step 2: Parse each line
for line in lines:
    line = line.strip()
    if not line:
        print()  # Print a blank line between days
        continue

    match = re.match(r"(\d{2}:\d{2})-(\d{2}:\d{2}) (.+)", line)
    if match:
        start_str, end_str, activity = match.groups()
        start = datetime.strptime(start_str, time_format)
        end = datetime.strptime(end_str, time_format)
        duration = end - start
        activity_totals[activity] += duration

        # Step 3: Print the schedule line
        print(f"{start_str}-{end_str} {activity}")

# Step 4: Calculate grand total
total_minutes = sum((td.total_seconds() for td in activity_totals.values()), 0) / 60

print("\n")  # Separate schedule and summary

# Step 5: Print summary
for activity, duration in sorted(activity_totals.items()):
    minutes = int(duration.total_seconds() // 60)
    percentage = round((minutes / total_minutes) * 100)
    print(f"{activity:<25} {minutes:>3} minutes   {percentage}%")
