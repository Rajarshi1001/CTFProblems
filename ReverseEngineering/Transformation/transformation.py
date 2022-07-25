encstring = open("enc").read()

hexstring = ""
with open("hex", "w") as file:
    for i in range(0, len(encstring)):
        hexchar = hex(ord(encstring[i]))[2:]
        bytes_object = bytes.fromhex(hexchar)
        ascii_string = bytes_object.decode("ASCII")
        file.write(ascii_string)

# with open("enc", "r") as f:
    # flag = f.read()

# with open("hex", "a") as file:
    # file.write(index)
