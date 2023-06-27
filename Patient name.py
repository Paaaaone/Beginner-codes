import random

patient_name = input("What is your name? ")
patient_age = input("what is your age? ")
patient_type = input("First time visitor? (0/1) ")
file_number = random.randint(24000, 100000)
if patient_type == "0":
    file_number = input("Enter file number: ")
print("Patient name: " + patient_name)
print("Patient age: " + patient_age)
print("File number: " + str(file_number))
