# **kwargs allows us to have more keyword arguments
def student_data(student_id, **kwargs):
    print("Student ID is", student_id, end='')
    if "student_name" in kwargs:
        print(", Student's Name is", kwargs["student_name"], end='')
    if "student_class" in kwargs:
        print(", Student's Class is", kwargs["student_class"])

student_data(student_id="211020xx")
print()
student_data(student_id="211020xx",student_name="ABC")
print()
student_data(student_id="211020xx", student_name="ABC", student_class="Civil")
