sum = 0

x = int(input("Enter a number of numbers: "))
for i in range(0, x):
    num = int(input("Enter a number: "))
    sum += num

mean = sum / x
print("The mean is:", mean)
print("The sum is:", sum)

w_n = int(input("Enter the wrong number: "))
c_n = int(input("Enter the correct replacement number: "))

new_sum = sum - w_n + c_n
new_mean = new_sum / x

print("The new mean is:", new_mean)
print("The new sum is:", new_sum)