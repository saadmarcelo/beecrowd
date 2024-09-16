'''
One day, the brothers Little Chitão and Xor Or Oh, great typists, made ​​a challenge to see who was the best in typing. For this, they obtained a computer that does not process keystrokes, ie, if it is to enter the same letter twice in a row, to press the button twice, as, press for longer, no use. They also measured the time down a key, which was exactly 1/100 second. The challenge would be who typed the word "Galopeira" consisting of letters and more, but both were very good, and arrived at a point that it was not possible to count how many letters had been typed. Then asked his help to write a program that checks the typed word and see how much time was spent typing.

Write a program that, given a typed word, tell how much time was spent to be entered.

Input

An integer C will be informed, which is the amount of test cases. Each case has a word of at least 9 and at most 10,000 letters.

Output

For each test case, print a T number, which is the time spent, in seconds, to enter the word of their test case, with precision of two decimal digits.

Input Sample	            Output Sample
3
galopeira
galopeeeeeeeeeeeeeeeeeira
galopeeira
                            0.09
                            0.25
                            0.10
'''

c = int(input())

while c>0:
    c-=1
    T= str(input())
    r=len(T)
    i = r * (1/100)
    print("%.2f" % i)
