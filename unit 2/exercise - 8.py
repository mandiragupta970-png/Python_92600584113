
x = 10   # Global variable

def outer():
    y = 20   # Nonlocal variable

    def inner():
        nonlocal y
        global x

        z = 30   # Local variable

        y = 25
        x = 15

        print("Local variable:", z)
        print("Nonlocal variable:", y)
        print("Global variable:", x)

    inner()

outer()
