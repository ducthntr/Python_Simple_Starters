fruit_list1 = ["apple","banana","pear","grape"]
fruit_list2 = ["peach","strawberry","banana","orange"]

for fruit1 in fruit_list1:
    for fruit2 in fruit_list2:
        if fruit1 == fruit2:
            print(f"We have a match {fruit1} from list1 is the same as {fruit2} from list2!")
        else: 
            print(f"{fruit1} is not the same as {fruit2}.")

