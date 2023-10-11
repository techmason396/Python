
class Course:
    def __init__(self, name, duration, *books) -> None:
        self.course_name = name
        self.course_duration = duration
        self.books = [self.Book(b) for b in books]
    
    def show_detail(self):
        print('Name: ', self.course_name)
        print('Duration: ', self.course_duration)
        print('Suggested book')
        for b in self.books:
            print(b.__str__())
    class Book:
        def __init__(self, title) -> None:
            self.book_title = title

        def __str__(self) -> str:
            return self.book_title




c = Course('Python',80,'Basic Python','Advantage Python')
c.show_detail()