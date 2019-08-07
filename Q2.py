# Q2.py
# By Divya Modi
import re
input_str = "foo-(a,b)-(1,2,5).(txt,jpg)"
input_str = "foo-(1,2,3)bar-abc(abd,abe,reba)-fdsafdsa(jfkdjsf,fds,fds)fdfdafdsa(fdsa,wer)fdsfdsafds"
input_str = "(1,23)(a,b)(ab)"

def possiblePatterns(s):
    num_lists = s.count("(")
    result = []
    for substr in s.split("("):
        if not substr:
            continue
        # print(substr)
        if ")" in substr:
            lst, const = substr.split(")")
            lst = lst.split(",")
            temp = []
            for i in lst:
                temp.append(i+const)
            # print(temp)
            if not result:
                result = temp
            else:
                new_res = []
                for res in result:
                    for t in temp:
                        new_res.append(res + t)
                result = new_res
            # print(result)
        else:
            if not result:
                result = [substr]
            else:
                result = [res + substr for res in result]
    print(*result, sep="\n")


possiblePatterns(input_str)

"""Write a function which takes in a simple pattern string and prints out all possible strings on the console.

For example, if the input pattern string is:

foo-(a,b)-(1,2,5).(txt,jpg)

The output will be:

foo-a-1.txt
foo-b-1.txt
foo-a-2.txt
foo-b-2.txt
foo-a-5.txt
foo-b-5.txt
foo-a-1.jpg
foo-b-1.jpg
foo-a-2.jpg
foo-b-2.jpg
foo-a-5.jpg
foo-b-5.jpg

The input pattern string may have multiple pairs of parentheses (i.e. "()"). 
Inside each pair of parentheses are list of options that are separated by commas (i.e. ","). 
You can assume that the input's parentheses are always paired up correctly. 
Also, you don't have to care about nested parentheses. 
And you can assume parentheses and commas are always special characters and 
you don't have to consider escaping them.

Other pattern examples:

foo-(1,2,3)bar-abc(abd,abe,reba)-fdsafdsa(jfkdjsf,fds,fds)fdfdafdsa(fdsa,wer)fdsfdsafds
(1,23)(a,b)(ab)
(a,b)abced
"""