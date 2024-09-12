
def decorator(fun):
    def wraper():
        print("start")
        fun()
        print("end")
    return wraper


def hi():
    print("helloo...")
s=decorator(hi)
hi()