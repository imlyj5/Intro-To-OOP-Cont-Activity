class Student:
    def __init__(self, name, grade, classes):
        self.name = name
        self.grade = grade
        self.classes = classes

    def add_class(self, class_name):
        if class_name not in self.classes:  #changes
            self.classes.append(class_name)
        return self.classes

    def get_num_classes(self):
        return len(self.classes)

    def display_classes(self):
        #change
        if not self.classes:
            return "Not enroll in any class yet"
        return ", ".join(self.classes)

    def summary(self):
        return (f"{self.name} is a {self.grade} "
            f"enrolled in {self.get_num_classes()} classes: "
            f"{self.display_classes()}")
        
        
    