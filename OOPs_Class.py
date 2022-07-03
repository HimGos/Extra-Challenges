import pyinputplus as pyip
import logging as lg
lg.basicConfig(filename='classtask.log' , level=lg.DEBUG , format="%(levelname)s %(asctime)s %(message)s")


class List:
    def __init__(self,lst):
        self.lst = lst

    def slicing(self):
        lg.info("Performing slicing operation in list:")
        lg.info(self.lst)
        strt = pyip.inputInt("Enter starting index number: ")
        stop = pyip.inputInt("Enter last index number: ")
        step = pyip.inputInt("Enter steps you wish: ")
        lg.info("Slicing result of the list: ")
        lg.info(self.lst[strt:stop:step])

    def reverse(self):
        lg.info(f"Performing Reverse Operation on list: {self.lst}")
        lg.info(f"Reversed List: {self.lst[::-1]}")

    def specialops(self):
        lg.info("In special ops we will perform operation on List given in Task #2:")
        l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1":"sudh" ,234:[23,45,656]}]
        lg.info(f"Here is the list\n{l}")
        lg.info("What you wish to do with this list?")

        while True:
            try:
                op_inp = int(input(f"""
                Enter a number top perform the operation on list -
                {l}
                1. Reverse List.
                2. Fetch all LISTs from this list.
                3. Fetch all keys in dictionary.
                4. Fetch 'sudh' from dictionary.
                5. Fetch a value from list within list.
                --->"""))
                if op_inp > 5  or  op_inp < 1:
                    raise Exception ("You have input number out of range!")
                else:
                    if op_inp == 1:
                        lg.info(f"Reverse List: {l[::-1]}")
                        break
                    elif op_inp == 2:
                        lg.info("Here are your lists within list:")
                        for i in l:
                            if type(i) == list:
                                lg.info(i)
                        break
                    elif op_inp == 3:
                        lg.info("All keys within the dictionary:")
                        for i in l:
                            if type(i) == dict:
                                lg.info(i.keys())
                        break
                    elif op_inp == 4:
                        for i in l:
                            if type(i) == dict:
                                lg.info(f"Getting 'sudh' from key1: {i['key1']}")
                        break
                    else:
                        lg.info("Here are lists within list:")
                        for i in l:
                            if type(i) == list:
                                lg.info(i)
                        lg.info("Which list you wish to work on?... 1 or 2")
                        choice = pyip.inputInt(min=1,max=2)
                        if choice == 1:
                            val1 = pyip.inputInt("Pick your number to extract.")
                            for i in l[5]:
                                if i == val1:
                                    lg.info(f"Found your number {val1} at index: {l[5].index(val1)}")
                        break

            except Exception as e:
                lg.error(f"{e} Try Again!")
                continue


class Tuple:

    def __init__(self,tup):
        self.tup = tup

    def index(self):
        lg.info("We will check index of tuple value!")
        while True:
            try :
                lg.info("Enter value you wish to find index of in tuple:")
                val = int(input("Enter the value here to find it's index in tuple:"))
                if val in self.tup:
                    lg.info(f"Here is the index: {self.tup.index(val)}")
                    break
                elif str(val) in self.tup:
                    lg.info(f"Here is the index: {self.tup.index(str(val))}")
                    break
                else :
                    raise Exception ("Entered value which isn't part of tuple")
            except Exception as e:
                lg.error("Please input value which is part of tuple given")
                continue


class Dictionary:

    def __init__(self,dic):
        self.dic = dic

    def key(self):
        lg.info("Let's Fetch the keys from your dictionary:")
        for i in self.dic:
            lg.info(f"Key: {i}")

    def values(self):
        lg.info("Let's Fetch the values from your dictionary:")
        for i,j in self.dic.items():
            lg.info(f"Key: {j}")

    def specialops(self):
        lg.info("In special ops we will perform operation on Dictionary:")
        dc = {'key1':123, 'key2':'sudhanshu sir', 'key3':{1:'ineuron' , 2:'Data Science'}}
        lg.info(f"Here is the dictionary\n{dc}")
        lg.info("What you wish to do with this dictionary?")

        while True:
            try:
                op_inp = int(input(f"""
                                Enter a number to perform one of the operation on this dict-
                                {dc}
                                1. Extract all keys.
                                2. Extract all values.
                                3. Extract ineuron.
                                4. Change 'Data Science' to 'Scientist'
                                --->"""))
                if op_inp > 4 or op_inp < 1:
                    raise Exception("You have input number out of range!")
                else:
                    if op_inp == 1:
                        lg.info(f"All the keys are: {dc.keys()}")
                        break
                    elif op_inp == 2:
                        lg.info(f"All the values are: {dc.values()}")
                        break
                    elif op_inp == 3:
                        lg.info("To extract 'ineuron, we need to get into nested dictionary!")
                        lg.info(f"Here is it: {dc['key3'][1]}")
                        break
                    else:
                        lg.info("To change 'Data Science' to 'Scientist', we need to go to nested dictionary!")
                        dc['key3'][2] = 'Scientist'
                        lg.info(f"Here is the new Dictionary: {dc}")
                        break
            except Exception as e:
                lg.error("Please enter a valid number between 1 and 5")
                continue


class Set:

    def __init__(self,st):
        self.st = st

    def discarditem(self):
        lg.info(f"We will discard an item here in set: {self.st}")
        disc_item = input("Enter a value within the set you wish to discard.")
        if disc_item in self.st:
            self.st.discard(disc_item)
            lg.info(f"New Set after discard -> {self.st}")
        elif int(disc_item) in self.st:
            self.st.discard(int(disc_item))
            lg.info(f"New Set after discard -> {self.st}")
        else :
            lg.info("Maybe value isn't in the set.")

    def additem(self):
        lg.info(f"We will add an item here in set: {self.st}")
        add_item = input("Enter a value to add")
        lg.info(f"New Set -> {self.st.add(add_item)}")


class String:
    def __init__(self,string):
        self.string = string

    def slicing(self):
        lg.info("Performing slicing operation in string:")
        lg.info(self.string)
        strt = pyip.inputInt("Enter starting index number: ")
        stop = pyip.inputInt("Enter last index number: ")
        step = pyip.inputInt("Enter steps you wish: ")
        lg.info("Slicing result of the list: ")
        lg.info(self.string[strt:stop:step])

    def split(self):
        lg.info("Performing split operation in string:")
        lg.info(self.string.split())

    def specialops(self):
        lg.info("In special ops we will perform operation on String given in Task #1:")
        s = "this is My First Python programming class and i am learNING python string and its function"
        lg.info(f"Here is the string\n{s}")
        lg.info("What you wish to do with this string?")

        while True:
            try:
                op_inp = int(input("""
                        Enter a number where
                        1. Extract data from index one to index 300 with a jump of 3.
                        2. Reverse String.
                        3. Split string after conversion in uppercase.
                        4. Convert string in lowercase
                        5. Capitalize string."""))
                if op_inp > 5 or op_inp < 1:
                    raise Exception("You have input number out of range!")
                else:
                    if op_inp == 1:
                        lg.info("Let's Extract data from index 1-300 with jump of 3")
                        lg.info(s[1:300:3])
                        break
                    elif op_inp == 2:
                        lg.info("Let's Reverse String:")
                        lg.info(s[::-1])
                        break
                    elif op_inp == 3:
                        lg.info(f"First uppercase the string:\n{s.upper()}")
                        up = s.upper()
                        lg.info(f"Now we will split it:\n{up.split()}")
                        break
                    elif op_inp == 4:
                        lg.info(f"Converting string in smallcase:\n{s.lower()}")
                        break
                    else :
                        lg.info(f"Capitalize the string:\n {s.capitalize()}")
                        break
            except Exception as e:
                lg.error("Please enter a valid number between 1 and 5")
                continue


lg.info("Welcome to the program!")
while True:

    lg.info("Which Data Type, you wish to work on?")
    try:
        pick = pyip.inputInt("""
        Pick a number assigned to data type:
        1. List
        2. String
        3. Dictionary
        4. Set
        5. Tuple
        0. End Task :)
        ---> """)
        if pick<0 or pick>5:
            raise Exception ("Entered number out of range!")
        else :
            if pick == 0:
                lg.info("Exiting the whole task!")
                break
            elif pick == 1:
                lg.info("In this section we will work on LIST!")
                lg.info("Enter your list: ")
                elements = pyip.inputInt("How many elements you want in your list?")
                inp_list = []
                for i in range(elements):
                    val_type = pyip.inputInt("You wanna add ->\n1. String\n2. Integer",min=1,max=2)
                    if val_type == 1:
                        list_val = inp_list.append(pyip.inputStr("Enter next value: "))
                    else :
                        list_val = inp_list.append(pyip.inputInt("Enter next value: "))
                lg.info(f"Your new List: {inp_list}")

                list_obj = List(inp_list)

                list_pick = pyip.inputInt("""
                What you wanna do in list?
                1. Slicing Operation
                2. Reverse
                3. Some SPECIAL OPS
                0. Previous Menu
                ---> """,min=0,max=3)

                if list_pick == 0 :
                    lg.info("Moving back to previous menu")
                    continue
                elif list_pick == 1:
                    lg.info("We will perform slicing operation here!")
                    list_obj.slicing()
                    continue
                elif list_pick == 2:
                    lg.info("We will perform reverse operation here!")
                    list_obj.reverse()
                    continue
                else :
                    lg.info("We will perform special ops on a special list->")
                    list_obj.specialops()
                    continue

            elif pick == 2:
                lg.info("In this section we will work on Strings!")
                lg.info("Enter your string: ")
                inp_string = pyip.inputStr("Your String: ")
                lg.info(f"Your String on which we will perform operations->\n{inp_string}")

                string_obj = String(inp_string)
                string_pick = pyip.inputInt("""
                What you wanna do in string?
                1. Slicing Operation
                2. Split
                3. Some SPECIAL OPS
                0. Previous Menu
                ---> """, min=0, max=3)
                if string_pick == 0:
                    lg.info("Moving to previous menu!")
                    continue
                elif string_pick == 1:
                    lg.info("We will perform slicing operation here!")
                    string_obj.slicing()
                    continue
                elif string_pick == 2:
                    lg.info("We will perform split operation here!")
                    string_obj.slicing()
                    continue
                else :
                    lg.info("Let's perform special ops on other list we have!")
                    string_obj.specialops()
                    continue

            elif pick == 3:
                lg.info("In this section we will work on Dictionary!")
                lg.info("Enter your Dictionary: ")
                elem = pyip.inputInt("How many keys you want in dictionary?")
                dic_inp = dict(input("Enter key and value: ").split() for _ in range(elem))
                lg.info(f"Your Dictionary: {dic_inp}")
                dic_obj = Dictionary(dic_inp)
                dic_pick = pyip.inputInt("""
                What you wanna do in Dictionary?
                1. Fetch Keys
                2. Fetch Values
                3. Some SPECIAL OPS
                0. Previous Menu
                ---> """, min=0, max=3)
                if dic_pick == 0:
                    lg.info("Moving back to previous menu!")
                    continue
                elif dic_pick == 1:
                    lg.info("Let's fetch all the keys:")
                    dic_obj.key()
                    continue
                elif dic_pick == 2:
                    lg.info("Let's fetch all the values: ")
                    dic_obj.values()
                    continue
                else:
                    lg.info("Time to perform SPECIAL OPS!")
                    dic_obj.specialops()
                    continue

            elif pick == 4:
                lg.info("In this section we will work on Set!")
                lg.info("Enter your set: ")
                set_ele = pyip.inputInt("How many elements you want in your set?")
                inp_set = []
                for i in range(set_ele):
                    setval_type = pyip.inputInt("You wanna add ->\n1. String\n2. Integer", min=1, max=2)
                    if setval_type == 1:
                        set_val = inp_set.append(pyip.inputStr("Enter next value: "))
                    else:
                        set_val = inp_set.append(pyip.inputInt("Enter next value: "))
                inp_set = set(inp_set)
                lg.info(f"Your new Set: {inp_set}")

                set_obj = Set(inp_set)
                set_pick = pyip.inputInt("""
                    What you wanna do in Set?
                    1. Discard Item
                    2. Add Item
                    0. Previous Menu
                    ---> """, min=0, max=2)
                if set_pick == 0:
                    lg.info("Moving back to previous menu!")
                    continue
                elif set_pick == 1:
                    lg.info("Let's Perform Discard Function in our set:")
                    set_obj.discarditem()
                    continue
                else:
                    lg.info("Let's Perform Add Function in our set:")
                    set_obj.additem()
                    continue

            else :
                lg.info("In this section we will work on Tuple!")
                lg.info("Enter your Tuple: ")
                tup_ele = pyip.inputInt("How many elements you want in your tuple?")
                inp_tup = []
                for i in range(tup_ele):
                    tupval_type = pyip.inputInt("You wanna add ->\n1. String\n2. Integer", min=1, max=2)
                    if tupval_type == 1:
                        tup_val = inp_tup.append(pyip.inputStr("Enter next value: "))
                    else:
                        tup_val = inp_tup.append(pyip.inputInt("Enter next value: "))
                inp_tup = tuple(inp_tup)
                lg.info(f"Your new Tuple: {inp_tup}")
                tup_obj = Tuple(inp_tup)
                tup_pick = pyip.inputInt("""
                        What you wanna do in Tuple?
                        1. Check Index
                        0. Previous Menu
                        ---> """, min=0, max=1)
                if tup_pick == 0:
                    lg.info("Moving back to previous menu!")
                    continue
                else :
                    lg.info("Let's find out the index of an element in our tuple")
                    tup_obj.index()
                    continue

    except Exception as e:
        lg.error(f"{e} Pick again!")
        continue

lg.info("End of Program, Thank You!")

