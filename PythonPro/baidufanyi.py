def a(func):
    print("It's A")


def b(func):
    print("It's B")
    func()
@a
@b
def c():
    print("It's C")
    

