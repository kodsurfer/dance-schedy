def main():
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


if __name__ == '__main__':
    main()
