"""'
Raul Seixas sang that he was born 10 thousand years ago and there was nothing in this world that he cannot know too much. The Mamomas Assassinas band sang that more than 10 thousand years "have gone by and passed" [sic] since they have failed at 5th grade. So many past events and professor MC was curious about what year each of these have happened.

You must write a program that, given a series of how many years have passed, show, for each number, in what year the event had happened. Remember that you must indicate if it had happened BC (Before Christ) or AD (Anno Domini). Use the portuguese A.C. for BC and D.C. for AD according to the output sample.

Input

The input has several lines. The first one has a positive integer number N (1 ≤ N ≤ 100000). There are N lines after the first one. Each of these N lines has a single non negative integer T, which indicates how many years have passed until 2015 AD (0 ≤ T < 231).

Output

The output has N lines. In each one there is the year A in which the correspondent time T had happened. Look at the sample output.

Input Sample	Output Sample
3
10000
15
2015
                7986 A.C.
                2000 D.C.
                1 A.C.

"""

N = int(input())
for i in range(N):
    year = int(input())
    calculate_year = year - 2015
    if calculate_year < 0:
        print("{0} D.C.".format(-calculate_year))
    elif calculate_year == 0:
        print("1 A.C.")
    else:
        print("{0} A.C.".format(calculate_year + 1))

