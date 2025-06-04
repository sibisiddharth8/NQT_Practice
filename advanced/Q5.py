"""
Jack is a sports teacher at St. Patrick’s School. He makes games not only to make the student fit but So smart. So, he lined up all the N number classes. of students in his class. At each position, he has fixed a board with the Integer number printed on it. Each number is unique and in exactly the range of N. Let us say there are 10 students, then the boards will be printed with numbers from 1 to 10 in a random order given by the sequence A[ ]. As a rule, all students wear a jersey with their numbers printed on it. So if there are students, each will have a unique jersey number just like a football team. Now, in the beginning, all the students will stand as per the increasing order of their jersey numbers, from left to right. The only difference will be their respective board number which is placed at their respective location. The board location is fixed and cannot be changed. We can consider the arrangement as below. Suppose there are students, and the board is placed in the order of [2 3 1 5 4].
Board — 2, 3, 1, 5, 4
Student’s Jersey — 1, 2, 3, 4, 5
Now the game begins.

After every beat of the drum, each student will have to move to that location (index), where his board is pointing to. In the above case student with jersey #1 is standing with board #2, so now he will have to move to location #2. Similarly, all the other students will do.
So after the first beat of the drum, the alignment will be:
Board — 2, 3, 1, 5, 4.
This keeps going on and on until all the students are back to the way they were at the beginning. So, after 6 beats of the drum, all the students will be aligned the same way as before.

Given N and the order of the board of the respective positions, find the number of beats required to bring back the students to their original position.
So, for the above case, the answer is 6

Example 1:

Input:
3 -> Input integer, N
{1, 2, 3} ->Input integer. B[], board alignment.
Output:
1 -> Output
Explanation:
All the students will be standing in board positions;
Board — 1, 2, 3
Student’s Jersey –1, 2, 3
After the first beat of the drum:
Jersey #1 will move to index 1.
Jersey #2 will move to index 2.
Jersey #3 will move to index 3.
Hence, they will be back in their position in just 1 beat.
So, the answer is 1.

Example 2:

Input:
5 -> Input integer, N
{2, 3, 1, 5, 4} -> Input integer, B[ ], board alignment.
Output:
6 -> Output
Explanation:
All the students will be standing as below, with the board positions:
Board — 2, 3, 1, 5, 4
Student’s Jersey — 1, 2, 3, 4, 5
After Beat-1of the drum:
Jersey #1 has moved to index 2.
Jersey #2 has moved to index 3.
Jersey #3 has moved to index 1.
Jersey #4 has moved to index 5.
Jersey #5 has moved to index 4.

Board – 2, 3, 1, 5, 4
Student’s Jersey — 3, 1, 2, 5, 4

After Beat-2 of the drum:
Jersey #3 has moved to index 2.
Jersey #1 has moved to index 3.
Jersey #2 has moved to index 1.
Jersey #5 has moved to index 5.
Jersey #4 has moved to index 4.

Board — 2, 3, 1, 5, 4
Student’s Jersey — 2, 3, 1, 4, 5

After Beat-3 of the drum:
Board — 2, 3, 1, 5, 4
Student’s Jersey — 1, 2, 3, 5, 4

After Beat-4 of the drum:
Board — 2, 3, 1, 5, 4
Student’s Jersey — 3, 1, 2, 4, 5

After Beat-5 of the drum:
Board — 2, 3, 1, 5, 4
Student’s Jersey — 2, 3, 1, 5, 4

After Beat-6 of the drum:
Board — 2, 3, 1, 5, 4
Student’s Jersey — 1, 2, 3, 4, 5

Hence, they will be back in their positions after 6 beats.
So, the answer is 6.
"""

num_of_boards = int(input())
boards = list(map(int, input().strip("{} ").split(",")))
stud_jerseys = sorted(boards)
org = stud_jerseys[:]

count = 0

while True:
    temp_stud_jerseys = [0 for i in range(num_of_boards)]
    for i in range(num_of_boards):
        temp_stud_jerseys[boards[i]-1] = stud_jerseys[i]
    count+=1
    if(org == temp_stud_jerseys):
        break
    stud_jerseys = temp_stud_jerseys[:]
print(count)         