while sum <= 100:
    try:
        sum = sum + input()
    except ValueError:
        print("try again!")