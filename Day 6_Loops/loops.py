# # # for i in range(5):
# # #     print("Workout")

# # # #For loop
# # # for i in range(5):
# # #     print("Hello")

# # # for i in range(5):
# # #     print(i)

# # # for i in range(1, 6):
# # #     print(i)

# # #when we have to repeat the value like "Drink Water"
# # # for i in range (1, 9):
# # #     print("Drink Water")

# # # break --- for i in range (5):
# # #range(5) = give me 5 numbers = 0,1,2,3,4
# # #i = i meaning = current number
# # # first round -> i = 0
# # # second round -> i = 1
# # # third round -> i = 2
# # # fourth round -> i = 3
# # # fifth round -> i = 4

# # # understand third value in range()
# # # range(start, stop, step)
# # # start = start from where ? 2
# # # stop = stop from where ? 11
# # # step = jump by how much ? 2
# #print even number in 2 to 10 range
# # for i in range(2, 11, 2):
# #     print(i)

# #reverse loop - count backwards (10,9,8,7,6,5,4,3,2,1)
# for i in range(10, 0, -1):
#     print(i)

# # #While loop (when we dont know the how many times should repeat)
# # count = 1
# # while count <= 5:
# #     print(count)
# #     count += 1

# # #While loop = infinite loops
# # count = 1
# # while count <= 5:
# #     print(count)
# #     # count += 1 (infinite loop removed this line code bcz count not increase by 1, then count value is always 1)
# # while count <= 5: means 1 <= 5, 2 <= 5, 3 <= 5, 4 <= 5, 5 <= 5
# # count += 1 (count increase by 1 --> 1 += 1, 2 += 1, 3 += 1, 4 += 1 )

#nested loops (loop inside amother loops)
#go to gym 3 days and everyday perform 4 excecise
# for day in range(1,4):
#     print("Day", day)

#     for excercise in range(1,5):
#         print("Excercise", excercise)

# for module in range(1,4):
#     print("\nModule", module)
#     for tc in range(1,5):
#         print("Executing Test Case",tc)

#print table 1 to 3
for table in range(1,4):
    print("\nTable of", table)
    for i in range(1,11):
        print(table, "X", i, "=", (table * i))






