import datetime

now = datetime.datetime.now().strftime("Date = (%Y-%m-%d) :: :: Time = (%H:%M:%S)")
log = []

try:
    user_input = input("Enter your age (or type 'clear,log' to clear the log): ")
    if user_input.lower() == "clear,log":
        with open("log3.txt", "w") as f:
            f.write("")
        print("Log file cleared.")
    num1, num2 = map(float, user_input.split(","))
    result, resul = int(num1) and int(num2)
    print("The result of division is:", result)
    log.append(f"{now} :: Division Successful\n")
except S: