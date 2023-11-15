# Kevin Nguyen 1928145

import csv


# Class to create student attributes
class Student:
    # Constructor with parameters for each student, disciplinary_action is None because student might not have
    def __init__(self, student_id, last_name, first_name, major, disciplinary_action=None):
        # Initialize attributes of each student and assign them
        self.student_id = student_id
        self.last_name = last_name
        self.first_name = first_name
        self.major = major
        self.disciplinary_action = disciplinary_action


# Class to represent entire student data system
class SystemClass:
    # Constructor initializes dicts
    def __init__(self):
        self.students = {}
        self.gpa_data = {}
        self.grad_dates = {}

    # Method to load student data from csv
    def load_student_data(self, students_file):
        # Open and read student_file.csv
        with open(students_file, 'r') as file:
            # Csv reader to read line by line
            reader = csv.reader(file)
            # For loop to read each row
            for row in reader:
                # Assign row 0,1,2 with respective attribute of each student
                student_id = row[0]
                last_name = row[1]
                first_name = row[2]
                major = row[3]
                # Check if student has disciplinary action == Y
                if len(row) > 4:
                    disciplinary_action = row[4]
                else:
                    disciplinary_action = None
                # Create student object and add it to student dict w/ student_id as key
                self.students[student_id] = Student(student_id, last_name, first_name, major, disciplinary_action)

    # Method to load GPA data from csv
    def load_gpa_data(self, gpa_file):
        # Open and read gpa_file.csv
        with open(gpa_file, 'r') as file:
            # Csv reader to read line by line
            reader = csv.reader(file)
            # For loop to read each row
            for row in reader:
                # Assign row 0,1 with student_id and gpa
                student_id = row[0]
                gpa = row[1]
                # Store gpa with the student_id as key
                self.gpa_data[student_id] = gpa

    # Method to load grad dates from csv
    def load_grad_dates(self, grad_dates_file):
        # Open and read grad_dates_file
        with open(grad_dates_file, 'r') as file:
            # Csv reader to read line by line
            reader = csv.reader(file)
            # For loop to read each row
            for row in reader:
                # Assign row 0,1 with student_id and graduation_rate
                student_id = row[0]
                grad_dates = row[1]
                # Store grad_dates with student_id as key
                self.grad_dates[student_id] = grad_dates

    # Method to create FullRoster.csv
    def generate_full_roster_report(self, output_file):
        # Prepare output file to write
        with open(output_file, 'w', newline='') as file:
            # csv writer
            writer = csv.writer(file)
            # Sort the student IDs by the last name of the students.
            # Sort student IDs by their last name
            sorted_student_ids = sorted(self.students, key=self.sort_lastname)
            # Iterate over each student_id
            for student_id in sorted_student_ids:
                # Retrieve student_id
                student = self.students[student_id]
                # Retrieve student's GPA, graduation date, and disciplinary action
                gpa = self.gpa_data.get(student_id, 'N/A')
                grad_dates = self.grad_dates.get(student_id, 'N/A')
                # Check if empty
                if student.disciplinary_action:
                    disciplinary_action = student.disciplinary_action
                else:
                    disciplinary_action = ''
                # Write student info into output file
                writer.writerow([student.student_id, student.major, student.first_name, student.last_name,
                                 gpa, grad_dates, disciplinary_action])

    # Method to create major csvs
    def generate_major_reports(self):
        # Create unique majors
        majors = set(student.major for student in self.students.values())
        # Loop over each unique major
        for major in majors:
            # Remove spaces
            major_file_name = f"{major.replace(' ', '')}Students.csv"
            # Prepare to write in major_file_name
            with open(major_file_name, 'w', newline='') as file:
                # Create csv writer
                writer = csv.writer(file)
                # Filter students by their major
                major_students = []
                # Check if major matches the specified 'major'
                for student in self.students.values():
                    if student.major == major:
                        major_students.append(student)
                # sort students by their student_id
                major_students.sort(key=self.sort_student_id)
                # Loop over each student in each major
                for student in major_students:
                    # Retrieve grad date and disciplinary action if not set
                    grad_dates = self.grad_dates.get(student.student_id, 'N/A')
                    if student.disciplinary_action:
                        disciplinary_action = student.disciplinary_action
                    else:
                        disciplinary_action = ''
                    # Write student info in csv
                    writer.writerow([student.student_id, student.last_name, student.first_name,
                                     grad_dates, disciplinary_action])

    # Method to create ScholarshipCandidates.csv
    def generate_scholarship_candidates_report(self, output_file):
        # Open output_file to write
        with open(output_file, 'w', newline='') as file:
            # Create csv writer
            writer = csv.writer(file)
            # Filter students if they have >3.8 GPA and having no disciplinary action
            # Create empty list for eligible students
            eligible_students = []
            # Iterate through the students and check eligibility criteria
            for student_id, student in self.students.items():
                gpa = float(self.gpa_data.get(student_id, 0))
                if gpa > 3.8 and not student.disciplinary_action:
                    eligible_students.append(student)

            # Sort eligible students by GPA in descending order
            eligible_students.sort(key=self.sort_gpa, reverse=True)
            # Loop over eligible_students
            for student in eligible_students:
                # write student info into csv
                writer.writerow([student.student_id, student.last_name, student.first_name, student.major,
                                 self.gpa_data.get(student.student_id, 'N/A')])

    # Method to create DisciplinedStudents.csv
    def generate_disciplined_students_report(self, output_file):
        # Open output file to write
        with open(output_file, 'w', newline='') as file:
            # csv writer
            writer = csv.writer(file)
            # Filter students to see if they have Y in disciplinary action column
            disciplined_students = []
            for student in self.students.values():
                if student.disciplinary_action:
                    disciplined_students.append(student)
            # Sort students by grad date
            disciplined_students.sort(key=self.sort_grad_dates)
            # Loop over each student
            for student in disciplined_students:
                # Get their grad date
                grad_dates = self.grad_dates.get(student.student_id, 'N/A')
                # Write info into csv
                writer.writerow([student.student_id, student.last_name, student.first_name, grad_dates])

    # Sort Methods
    def sort_lastname(self, student_id):
        return self.students[student_id].last_name

    def sort_student_id(self, student):
        return student.student_id

    def sort_gpa(self, student):
        return float(self.gpa_data.get(student.student_id, 0))

    def sort_grad_dates(self, student):
        return self.grad_dates.get(student.student_id, '9999-12-31')


if __name__ == "__main__":
    # Instantiate
    system = SystemClass()

    # Name output files
    students_file = "StudentsMajorsList.csv"
    gpa_file = "GPAList.csv"
    grad_dates_file = "GraduationDatesList.csv"

    full_roster_output_file = "FullRoster.csv"
    scholarship_candidates_output_file = "ScholarshipCandidates.csv"
    disciplined_students_output_file = "DisciplinedStudents.csv"

    # Load the data from input CSV files.
    system.load_student_data(students_file)
    system.load_gpa_data(gpa_file)
    system.load_grad_dates(grad_dates_file)

    # Create reports
    system.generate_full_roster_report(full_roster_output_file)
    system.generate_major_reports()
    system.generate_scholarship_candidates_report(scholarship_candidates_output_file)
    system.generate_disciplined_students_report(disciplined_students_output_file)
