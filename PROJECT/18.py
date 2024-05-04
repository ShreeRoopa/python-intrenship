import streamlit as st

class Student:
    def __init__(self, name, age, gender, gpa, state, student_id, university, amount, discount):
        self.name = name
        self.age = age
        self.gender = gender
        self.gpa = gpa
        self.state = state
        self.student_id = student_id
        self.university = university
        self.amount = amount
        self.discount = discount

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        st.success("Student added successfully.")

    def display_students(self):
        if self.students:
            for idx, student in enumerate(self.students, 1):
                st.write(f"Student {idx}:")
                st.write(f"Name: {student.name}")
                st.write(f"Age: {student.age}")
                st.write(f"Gender: {student.gender}")
                st.write(f"GPA: {student.gpa}")
                st.write(f"State: {student.state}")
                st.write(f"ID: {student.student_id}")
                st.write(f"University: {student.university}")
                st.write(f"Amount: {student.amount}")
                st.write(f"Discount: {student.discount}%")
                st.write( )
        else:
            st.warning("No students to display.")

    def remove_student(self, student_name):
        removed = False
        for student in self.students:
            if student.name == student_name:
                self.students.remove(student)
                st.success(f"{student_name} removed successfully.")
                removed = True
                break
        if not removed:
            st.error(f"Student {student_name} not found.")

def check_eligibility(age, gpa, sport):
    age_limits = {
        "basketball": 25,
        "soccer": 23,
        "swimming": 22,
        "football": 21
    }

    gpa_limits = {
        "basketball": 12,
        "soccer": 10,
        "swimming": 8,
        "football": 9
    }
    
    amount_limits = {
        "basketball": 10000,
        "soccer": 8000,
        "swimming": 6000,
        "football": 7000
    }

    if sport.lower() in age_limits and sport.lower() in gpa_limits:
        max_age = age_limits[sport.lower()]
        min_gpa = gpa_limits[sport.lower()]
        max_amount = amount_limits[sport.lower()]
        if age <= max_age and gpa >= min_gpa:
            discount = (gpa - min_gpa) * 5  
            st.success(f"You are eligible for {sport} scholarship with a {discount}% discount!")
            return max_amount - (max_amount * discount / 100), discount
        else:
            st.error(f"Sorry, you are not eligible for {sport} scholarship.")
            return 0, 0
    else:
        st.error("Sport is not found or age/grade limit not defined for this sport.")
        return 0, 0

def sport_information(sport):
    age_limits = {
        "basketball": 25,
        "soccer": 23,
        "swimming": 22,
        "football": 21
    }

    gpa_limits = {
        "basketball": 12,
        "soccer": 10,
        "swimming": 8,
        "football": 9
    }
    
    amount_limits = {
        "basketball": 10000,
        "soccer": 8000,
        "swimming": 6000,
        "football": 7000
    }

    if sport.lower() in age_limits and sport.lower() in gpa_limits:
        st.write(f"Sport: {sport}")
        st.write(f"Minimum GPA: {gpa_limits[sport.lower()]}")
        st.write(f"Maximum Age: {age_limits[sport.lower()]}")
        st.write(f"Maximum Scholarship Amount: {amount_limits[sport.lower()]}")
    else:
        st.error("Sport information not found.")

def main():
    st.title("Student Management System")

    student_manager = StudentManager()

    menu_choice = st.sidebar.selectbox("Menu", ["Add a student", "Display all students", "Remove a student", "Sport Information", "Exit"])

    if menu_choice == "Add a student":
        st.subheader("Add a student")
        name = st.text_input("Enter your name:")
        age = st.number_input("Enter your age:")
        gender = st.text_input("Enter your gender:")
        gpa = st.number_input("Enter your GPA:")
        state = st.text_input("Enter your state:")
        student_id = st.number_input("Enter your ID:")
        university = st.text_input("Enter your university:")
        sport = st.selectbox("Select the sport you're interested in:", ["basketball", "soccer", "swimming", "football"])
        if st.button("Add Student"):
            amount, discount = check_eligibility(age, gpa, sport)
            if amount > 0:
                student = Student(name, age, gender, gpa, state, student_id, university, amount, discount)
                student_manager.add_student(student)
    elif menu_choice == "Display all students":
        st.subheader("Display all students")
        student_manager.display_students()
    elif menu_choice == "Remove a student":
        st.subheader("Remove a student")
        name = st.text_input("Enter student's name to remove:")
        if st.button("Remove Student"):
            student_manager.remove_student(name)
    elif menu_choice == "Sport Information":
        st.subheader("Sport Information")
        sport = st.selectbox("Select the sport:", ["basketball", "soccer", "swimming", "football"])
        sport_information(sport)
    else:
        st.write("Exiting program...")

if __name__ == "__main__":
  main()