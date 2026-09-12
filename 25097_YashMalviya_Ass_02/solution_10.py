# Exercise 10: Run-Length String Compression
def Run_Length_String_Compression():
    input_01 = input("Enter the string: ")
    dump = []
    count = 1
    for i in range(len(input_01) - 1):
        if input_01[i] == input_01[i + 1]:
            count += 1
        else:
            dump.append(f"{input_01[i]}{count}")
            count = 1
    large_len = "".join(dump)
    if len(large_len) > len(input_01):
        print(input_01)
    else:
        print(large_len)


Run_Length_String_Compression()
