def solve(s):
    m = {}
    for ch in s:
        if m.get(ch):
            m[ch] += 1
        else:
            m[ch] = 1
    
    for ch in s:
        if m[ch]==1:
            return ch

    return 'none'

if __name__ == "__main__":
    str = input("Enter the word : ")
    print(solve(str))