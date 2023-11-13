#!/usr/bin/python3
""" text_indentation returns "text" in the specified format:
2 newlines after each ['.', '?', ':']
"""


def text_indentation(text):
    """ prints "text" with 2 newlines after each of these char: ['.', '?', ':']
    checks if "text" is a str
    first loop removes spaces after each required chars
    second loop adds 2 newlines after each required chars
    """
    if not isinstance(text,str):
        raise TypeError("text must be a string")
    else :
        i = 0
        line = [""]
        for c in text:
            if  not c in ".?:":
               line[i] += c
            else:
              line[i] += c
              if line[i][0] == " ":
                 print(line[i][1:])
              else:
                   print(line[i])
              print("")
              line.pop(0)
              line.append("")
        if not c in ".:?":
            if line[i][0] == " ":
                if line[i][-1] == " ":
                  print(line[i][1:-1],end="")
                else:
                    print(line[i][1:],end="")
            else :
                if line[i][-1] == " ":
                  print(line[i][:-1],end="")
                else:
                 print(line[i],end="")

