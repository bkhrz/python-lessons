import csv

# Dictionary to store total grades and count of grades for each subject
subject_grades = {}

# Read data from grades.csv
with open('grades.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        subject = row['Subject']
        grade = int(row['Grade'])

        if subject not in subject_grades:
            subject_grades[subject] = {'total': 0, 'count': 0}

        subject_grades[subject]['total'] += grade
        subject_grades[subject]['count'] += 1

# Calculate the average grades
grade_average = [{'Subject': subject, 'Average grade': total['total'] / total['count']}
                 for subject, total in subject_grades.items()]

# Write to average_grades.csv
with open('average_grades.csv', 'w', newline='') as f:
    fieldnames = ['Subject', 'Average grade']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(grade_average)
