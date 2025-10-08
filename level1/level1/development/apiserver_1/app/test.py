def even_number(num):
    for i in range(num):
        if i % 2 == 0:
            print(i)
def getJsonObject(name, age):
    return {
        "name": name,
        "age": age
    }

simobj = getJsonObject("Simran", 20)
harishobj = getJsonObject("Harish", 21)

print(simobj)
print(harishobj)
my_number=even_number(10)
print(my_number)
