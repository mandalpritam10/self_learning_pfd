"""
in text mode, relative seek is not possible
only in binary mode, relative seek is possible, 
check the notbook for the content.
"""

with open("cursor_move_eg.txt","rb") as f:
    print(f.read())

    print(f.tell())
    
    f.seek(0)
    print(f.tell())
    print(f.read())

    f.seek(1)
    print(f.tell())
    print(f.read())

    f.seek(0)
    print(f.tell())

    f.seek(2,1)
    print(f.tell())
    print(f.read())

    f.seek(0)
    print(f.read(3))
    
    f.seek(-5,2)
    print(f.tell())
    print(f.read(-1)) #because read() and read(-1) is same