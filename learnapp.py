print("hello world")

# tuple practise
coordinates = (1, 3, 4, 5, 7, 896)
print(coordinates[5])


# list and list functions practise
friend_list = ["Tunde", "Seun", "Tade", "Bolu", "Bode", "Tunde"]
friend_list.sort()
friend_list[2] = ("omoboriola")
friend_list_2 = friend_list.copy()

print(friend_list)
print(friend_list[4])
print(friend_list[-4])
print(friend_list[3:5])
print(friend_list_2)
print(friend_list_2.index("omoboriola"))

# function practise
def sayhi(name, id):
    print("Hello " + name + " you are welcome to python class 101")
    print("Your id is " + id)

sayhi("Bolu", "1asw11Z")

# if statement practise
is_male = False
is_tall = True

if is_male:
    print("okunrin ni e jo")
else:
    print("obinrin ni e")
if is_tall:
    print("agoro ni bobo")
else:
    print("kuru bente")
if is_male or is_tall:
    print("okunrin lanti lanti")
else:
    print("alaye park well!")
if is_male and is_tall:
    print("kare laye okunrin mewa")
elif is_tall and not (is_male):
    print("omoge, you try but na man get this job")
elif is_male and not(is_tall):
    print("ogbeni, go join usher")
else:
    print("go chop beans")


#if comparison statement This is used to filter group of data according to the conditions after comparing.

def max_num(num1, num2, num3, num4, num5, num6, num7, num8):
    if num1>=num2 and num1>=num3 and num1>=num4 and num1>=num5 and num1>=num6 and num1>=num7 and num1>=num8:
        return num1
    elif num2>=num1 and num2>=num3 and num2>=num4 and num2>=num5 and num2>=num6 and num2>=num7 and num2>=num8:
        return num2
    elif num3>=num1 and num3>=num2 and num3>=num4 and num3>=num5 and num3>=num6 and num3>=num7 and num3>=num8:
        return num3
    elif num4>=num1 and num4>=num2 and num4>=num3 and num4>=num5 and num4>=num6 and num4>=num7 and num4>=num8:
        return num4
    elif num5>=num1 and num5>=num2 and num5>=num3 and num5>=num4 and num5>=num6 and num4>=num7 and num5>=num8:
        return num5
    elif num6>=num1 and num6>=num2 and num6>=num3 and num6>=num4 and num6>=num5 and num6>=num7 and num6>=num8:
        return num6
    elif num7>=num1 and num7>=num2 and num7>=num3 and num7>=num4 and num7>=num5 and num7>=num6 and num7>=num8:
        return num7
    elif num8>=num1 and num8>=num2 and num8>=num3 and num8>=num4 and num8>=num5 and num8>=num6 and num8>=num7:
        return num8
    else:
        return 0
print(max_num(47, 959, 9, 33, 43, 2, 200000,993 ))


# Dictionary Practise




