def text_indentation(text):
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

