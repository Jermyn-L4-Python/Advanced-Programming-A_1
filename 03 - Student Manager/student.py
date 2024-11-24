import tkinter as tk
from tkinter import ttk

class StudentManager:
    def __init__(self, root, filename):
        self.root = root
        self.root.title("Student Manager")
        self.filename = filename
        self.students = []
        self.load_data()

        tk.Label(root, text="Student Manager", font=("Arial", 20, "bold"), fg = "indigo").pack(pady=10)

        self.buttons = tk.Frame(root)
        self.buttons.pack()

        tk.Button(self.buttons, 
                  text="View All Student Records", 
                  command=self.view_all_records, 
                  font=("Arial", 11), 
                  padx=10, pady=5, bg = "indigo", fg = "white").grid(row=0, column=0, padx=15, pady=20, sticky="ew")

        tk.Button(self.buttons, 
                  text="Show Highest Score", 
                  command=self.show_highest_score, 
                  font=("Arial", 11), 
                  padx=10, pady=5, bg = "green", ).grid(row=0, column=1, padx=15, pady=20, sticky="ew")

        tk.Button(self.buttons, 
                  text="Show Lowest Score", 
                  command=self.show_lowest_score, 
                  font=("Arial", 11), 
                  padx=10, pady=5, bg = "red").grid(row=0, column=2, padx=15, pady=20, sticky="ew")

        # Label for View Individual Student Record
        tk.Label(self.buttons, 
                 text="View Individual Student Record:", 
                 font=("Arial", 11)).grid(row=1, column=0, pady=10, padx=10)

        # Combobox for selecting student
        self.selectStudent = ttk.Combobox(self.buttons, 
                                              values=[student['name'] for student in self.students])
        self.selectStudent.grid(row=1, column=1, pady=5, padx=10, sticky="ew")

        tk.Button(self.buttons, 
                  text="View Record", 
                  command=self.view_individual_record, 
                  font=("Arial", 11), 
                  padx=10, pady=5, bg = "indigo", fg = "white").grid(row=1, column=2, pady=5, padx=10)

        self.text = tk.Text(root, width=70, height=20, state="disabled", wrap="word")
        self.text.pack(pady=10)

    def load_data(self):
        with open(self.filename, "r") as file:
            lines = file.readlines()
            num_students = int(lines[0].strip())  
                
            for line in lines[1:]:
                line = line.replace(", ", ",").strip()  
                parts = line.split(",")  
                    
                if len(parts) != 6:
                    print(f"Skipping malformed line: {line}")
                    continue
  
                student_id = parts[0].strip()
                name = parts[1].strip()
                
                marks = list(map(int, parts[2:]))
                    
                coursework_total = sum(marks[:3])  
                exam_mark = marks[3]  
                total_score = coursework_total + exam_mark
                percentage = (total_score / 160) * 100
                grade = self.calculate(percentage)

                self.students.append({
                    "id": student_id,
                    "name": name,
                    "coursework_total": coursework_total,
                    "exam_mark": exam_mark,
                    "percentage": percentage,
                    "grade": grade
                })

    @staticmethod
    def calculate(percentage):
        if percentage >= 70:
            return 'A'
        elif percentage >= 60:
            return 'B'
        elif percentage >= 50:
            return 'C'
        elif percentage >= 40:
            return 'D'
        else:
            return 'F'

    def view_all_records(self):
        output = ""
        for student in self.students:
            output += self.format_student_record(student) + "\n"
        self.display_output(output)

    def view_individual_record(self):
        selected_name = self.selectStudent.get()
        for student in self.students:
            if student['name'] == selected_name:
                self.display_output(self.format_student_record(student))
                return

    def show_highest_score(self):
        highest_student = max(self.students, key=lambda s: s['percentage'])
        self.display_output(self.format_student_record(highest_student))

    def show_lowest_score(self):
        lowest_student = min(self.students, key=lambda s: s['percentage'])
        self.display_output(self.format_student_record(lowest_student))

    @staticmethod
    def format_student_record(student):
        return (f"Name: {student['name']}\n"
                f"Number: {student['id']}\n"
                f"Coursework Total: {student['coursework_total']}\n"
                f"Exam Mark: {student['exam_mark']}\n"
                f"Overall Percentage: {student['percentage']:.2f}%\n"
                f"Grade: {student['grade']}\n")

    def display_output(self, text):
        self.text.config(state="normal")
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, text)
        self.text.config(state="disabled")


root = tk.Tk()
app = StudentManager(root, "03 - Student Manager/studentMarks.txt")  # Replace with the correct file path
root.mainloop()

