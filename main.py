def main():
    print('Welcome to the Dance School Scheduler')
    while True:

        break


class Student:
    def __init__(self, name, role):
        self.name = name
        self.role = role


class Class:
    def __init__(self, name, room, capacity):
        self.name = name
        self.room = room
        self.capacity = capacity
        self.students = []
        self.leaders = 0
        self.followers = 0

    def sign_up(self, student):
        if len(self.students) >= self.capacity:
            return False
        if student.role == 'leader':
            if self.leaders - self.followers >= 2:
                return False
            self.followers += 1
        self.students.append(student)
        self.capacity -= 1
        return True


if __name__ == '__main__':
    main()
