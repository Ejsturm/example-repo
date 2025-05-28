'''Modify the inheritance_template.py, create a subclass with
constructor and methods. 2025-05-027 EJS'''


class Course:
    # Class attribute for the course name
    name = "Fundamentals of Computer Science"

    # Class attribute for the contact website
    contact_website = "www.hyperiondev.com"

    # Method to display contact details
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    def office_location(self):
        print("The head office is located in Cape Town.")


class OOPCourse(Course):
    def __init__(self, description="OOP Fundamentals",
                 trainer="Mr Anon A. Mouse"):
        self.description = description
        self.trainer = trainer

    def trainer_details(self):
        print("Here are the course details:\n"
              f"\tThe class is about {self.description}.\n"
              f"\tThe trainer is named {self.trainer}.\n")

    def show_course_id(self):
        print("The course ID number is #12345.")


# Example usage:
# Create an instance of the Course class
course = Course()

# Call the contact_details method to display contact information
course.contact_details()

# EJS: instantiate an OOPCourse object and use its methods.
course_1 = OOPCourse()

course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()
