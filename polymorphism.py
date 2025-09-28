class Student:
    def __init__(self, name, major, gpa_for_semesters):
        self.name = name
        self.major = major
        self.__gpa_for_semesters = gpa_for_semesters  # Private attribute

    def __str__(self):
        return f"{self.name} is studying {self.major}."

    # Encapsulation: controlled access to GPA data
    def get_gpa(self):
        return self.__gpa_for_semesters

    def set_gpa(self, new_value):
        self.__gpa_for_semesters = new_value

    def calculate_average_gpa(self):
        if not self.__gpa_for_semesters:
            return 0.0
        return sum(self.__gpa_for_semesters) / len(self.__gpa_for_semesters)

    def is_in_good_standing(self):
        print(f"{self.name} is a student.")


class UndergraduateStudent(Student):
    def __str__(self):
        return f"{self.name} is an undergraduate student studying {self.major}."

    def is_in_good_standing(self):
        avg_gpa = self.calculate_average_gpa()
        if avg_gpa >= 2.5:
            print(f"{self.name} is in good academic standing.")
        else:
            print(f"{self.name} is not in good academic standing.")


class GraduateStudent(Student):
    def __str__(self):
        return f"{self.name} is a graduate student studying {self.major}."

    def is_in_good_standing(self):
        avg_gpa = self.calculate_average_gpa()
        if avg_gpa >= 3.0:
            print(f"{self.name} is in good academic standing.")
        else:
            print(f"{self.name} is not in good academic standing.")
