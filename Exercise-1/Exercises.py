# Exercise 1
students = 20
course = 'CMP'
print(f"This course {course} has {students} students.")

# Exercise 2
colors = ["red","blue","green", "yellow", "pink"]
colors.append("Purple")
print(colors) # colors[2] prints green
dictionary = {
    "name" : "Joe",
    "gpa" : 80
}
print(dictionary)  # print(dictionary["name"]) prints Joe

# Exercise 3
numbers = [1,2,3,4,5,6,7,8,9,10]
evens = []
for x in numbers:
    if x % 2 == 0:
        evens.append(x)
print(evens)

