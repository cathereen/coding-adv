input_string="""[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
}
<<>)}]
*
[(()])"""

#input_string="""123**
#"""

d_chunk = { "(": -3, "[": -57, "{": -1197, "<": -25137, ")": 3, "]": 57, "}": 1197, ">": 25137 }

error_points = 0

def illegal_char(val):
    global error_points
    error_points += val

def main():
    for line in input_string.splitlines():
        stack = []
        for key in line:
            val = d_chunk.get(key)
            if val == None : break
            if val < 0: stack.append(val) 
            if val > 0:
                if not stack:
                    ch = 0 
                else:
                    ch = stack.pop()
                if (ch + val) != 0 :
                    illegal_char(val)
                    print("Illegal character " + key + " encountered in line " + line)
                    break
    print("The total syntax error score: " + str(error_points))

if __name__ == "__main__":
    main()
