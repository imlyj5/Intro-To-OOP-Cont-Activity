from school_schedule.student import Student

# Write your tests here!
def test_creating_student():
    #arrange
    name = "Amy"
    grade = "Junior"
    classes = ["Math","PE"]
    #act
    new_student = Student(name,grade,classes)
    #assert
    assert new_student.name == name
    assert new_student.grade == grade
    assert new_student.classes == classes

#Edge case
def test_creating_student_with_no_class():
    #arrange
    name = "Amy"
    grade = "Junior"
    classes = []
    #act
    new_student = Student(name,grade,classes)
    #assert
    assert new_student.name == name
    assert new_student.grade == grade
    assert new_student.classes == classes
    assert new_student.classes == []
    assert len(new_student.classes) == 0

def test_add_class():
    #arrange
    student = Student("Amy","Junior",["Math","PE"])
    new_class = "Art"
    #act
    classes_list = student.add_class(new_class)
    #assert
    assert classes_list == ["Math","PE","Art"]
    assert len(classes_list) == 3
    assert new_class in student.classes

#change add_class a little bit to handle duplicate classes case
#Edge case
def test_add_duplicate_class():
    #arrange
    student = Student("Amy","Junior",["Math","PE"])
    new_class = "PE"
    #act
    classes_list = student.add_class(new_class)
    #assert
    assert classes_list == ["Math","PE"]
    assert len(classes_list) == 2
    assert new_class in student.classes



def test_get_num_classes():
    #arrange
    student = Student("Amy","Junior",["Math","PE"])
    #act
    num_of_classes = student.get_num_classes()
    #assert
    assert num_of_classes == 2

#Edge case
def test_count_empty_classes_list():
    #arrange
    student = Student("Amy","Junior",[])
    #act
    num_of_classes = student.get_num_classes()
    #assert
    assert num_of_classes == 0

def test_display_classes():
    #arrange
    student = Student("Amy","Junior",["Math","PE"])
    #act
    display = student.display_classes()
    #assert
    assert display == "Math, PE"

#change display_classes a little bit to handle empty classes situation
#Edge case
def test_display_empty_classes():
    #arrange
    student = Student("Amy","Junior",[])
    #act
    display = student.display_classes()
    #assert
    assert display == "Not enroll in any class yet"

def test_summary():
    #arrange
    student = Student("Amy","Junior",["Math","PE"])
    #act
    summary = student.summary()
    #assert
    assert summary == f"{student.name} is a {student.grade} enrolled in {student.get_num_classes()} classes: {student.display_classes()}"

def test_summary_with_no_class():
    #arrange
    student = Student("Amy","Junior",[])
    #act
    summary = student.summary()
    #assert
    assert summary == f"{student.name} is a {student.grade} enrolled in {student.get_num_classes()} classes: Not enroll in any class yet"
