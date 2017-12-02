def foo():
    return "This demo"


def bar():
    return foo() + ", probably won't run"


def foobar():
    # my point exactly..
    return foo() + bar()
