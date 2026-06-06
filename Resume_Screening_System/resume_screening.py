# Resume Screening System
import csv
def extract_skills(text):
    skills_database = [
        "python",
        "machine learning",
        "sql",
        "data analysis",
        "pandas",
        "excel",
        "java",
        "html",
        "css"
    ]

    found_skills = []

    text = text.lower()

    for skill in skills_database:
        if skill in text:
            found_skills.append(skill)

    return found_skills


# Read Job Description
with open("job_description.txt", "r") as file:
    jd_text = file.read()

# Read Resume
with open("resume1.txt", "r") as file:
    resume_text = file.read()

# Extract Skills
jd_skills = extract_skills(jd_text)
resume_skills = extract_skills(resume_text)

# Find Matches
matched_skills = list(set(jd_skills) & set(resume_skills))
missing_skills = list(set(jd_skills) - set(resume_skills))

# Calculate Score
if len(jd_skills) > 0:
    score = (len(matched_skills) / len(jd_skills)) * 100
else:
    score = 0

# Display Results
print("=" * 40)
print("RESUME SCREENING REPORT")
print("=" * 40)

print(f"\nMatch Score: {score:.2f}%")

print("\nMatched Skills:")
for skill in matched_skills:
    print("-", skill.title())

print("\nMissing Skills:")
for skill in missing_skills:
    print("-", skill.title())

print("\nResume Status:")
if score >= 80:
    print("Highly Recommended")
elif score >= 60:
    print("Recommended")
else:
    print("Needs Improvement")
   

with open("results.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Candidate", "Score", "Status"])

    status = (
        "Highly Recommended"
        if score >= 80
        else "Recommended"
        if score >= 60
        else "Needs Improvement"
    )

    writer.writerow(["Pramiti R", round(score, 2), status])

print("\nResults saved to results.csv")