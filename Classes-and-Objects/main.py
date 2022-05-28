class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, track, score):
        print(f"name-{name}, age-{age}, track-{track}, score-{score}")

    def change_name(self, newname):
        self.change_name = newname
        print(f"The new student's name is {newname}")
    def change_age(self, age):
        print(f"The new student's age is  {age}")
    def add_track(self, track):
        print(f"The new student's track is  {track}")
    def get_score(self, score):
        print(f"The new student's score is  {score}")



Bob = Student(name="Bob", age=26, track=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(20.90)
