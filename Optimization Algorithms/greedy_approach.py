def convert_the_binary(number,length):
    binary = [0]*length
    for i in range(length-1,-1,-1):
        binary[i] = number%2
        number = number//2
    return binary
def main():
    number = 2
    for i in range(2**number):
        print(convert_the_binary(i,number))
main()