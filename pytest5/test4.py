
def hi():
    return "hi yasoob!"


def daosomethingbeforehi(func):
    print("i am doing some boring work before executing hi(")
    print(func())


daosomethingbeforehi(hi)
