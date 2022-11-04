prompt1 = str(input("What are you converting? (blocks, mb, gb) "))
if prompt1 == "blocks":
    prompt2 = str(input("What are you converting into? (mb, gb) "))
    if prompt2 == "gb":
        num = int(input("How many blocks? "))
        print("Total Gigabytes:",num/8192)
    elif prompt2 == "mb":
        num = int(input("How many blocks?"))
        print("Total Megabytes:",num/8)
elif prompt1 == "gb":
    num = int(input("How many gigabytes are you converting to blocks? "))
    print("Total Blocks:",num*8192)
elif prompt1 == "mb":
    num = int(input("How many megabytes are you converting to blocks? "))
    print("Total blocks:",num*8)
