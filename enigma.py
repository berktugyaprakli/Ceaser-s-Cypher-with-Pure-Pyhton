print("enigma app")

password = int(input("password: "))
if password != 2323:
    print("wrong password")
else:
    purpose = int(input("encription:1 / decryiption:2 "))

    if purpose == 1:
        text = input("your text: ")
        list1 = [chr(int(ord(ch)) + 3) for ch in text]
        string = ""
        for elaman in list1:
            string = string + elaman
        print("new text: ")
        print(string)
    elif purpose == 2:
        text = input("your text")
        list1 = [chr(int(ord(ch)) - 3) for ch in text]
        string = ""
        for elaman in list1:
            string = string + elaman
        print("new text: ")
        print(string)

    else:
        print("unassigned")

