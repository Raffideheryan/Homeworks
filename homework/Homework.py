#lesson 150

# def head(filename):
#     try:    
#         with open(filename, "r") as file:
#             res = file.readlines()
#         s = ''
#         for i in res[-10:]:
#             s += i
#         return s
#     except FileNotFoundError:
#         return "NO FILE!!!"
# print(head(input('Enter filename: ')))


#lesson 151

# def cat(filename1,filename2):
#     try:
#         with open(filename1, "r") as file:
#             res = file.read()
#         with open(filename2, "a") as file:
#             file.write(res)
#     except FileNotFoundError:
#         return "NO FILE!!!"
    
# print(cat(input("Enter file name: "), input("Enter second file name: ")))


#lesson 152

# ---?---

#lesson 153

# def max_word(filename):
#     try:
#         with open(filename, "r") as file:
#             res = file.read()
#             res = res.replace("\n", " ")
#             res = res.split(" ")
#             res.sort(key = len)
#             return res[-1]
#     except FileNotFoundError:
#         return "NO FILE!!!"

# print(max_word(input("Enter file name: ")))
            

#lesson 154 

# def func(filename):
#     try:
#         with open(filename, "r") as file:
#             res = file.readline()
#         res = res.replace(" ", "")
#         mydict = {i:res.count(i) for i in res}
#         tar = sorted(mydict, key = mydict.get)
#         return tar
#     except FileNotFoundError:
#         return "NO FILE!!!"
    
# print(func(input("Enter the file name: ")))

#lesson 155

#---?---

#lesson 156

# def func():
#     summ = 0   
#     while True:
#         try:
#             num = input("Enter the number: ")
#             if num == "" or num == " ":
#                 return f"Final result is {summ}"
#             else:  
#                 summ += int(num)
#                 print(summ)
#         except ValueError:
#                 print("Enter the number!!!")

# print(func())

#lesson 158

# def comdel(file1, file2):
#     try:
#         with open(file1, "r") as file:
#             res = file.readlines()
#         for i in res:
#             if i[0] == "#":
#                 #---?----
#         with open(file2, "w") as file:
#             file.write("".join(res))
#     except FileNotFoundError:
#         return "NO FILE!!!"

# print(comdel(input("Enter the file name: "), input("Enter the file name: ")))



#lesson 160

#-----------??------------


#lesson 162

#--------?--------



