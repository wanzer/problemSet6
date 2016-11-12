import cs50
height=cs50.get_int()

if (height<0 or height>23):
    print("Usage: positive height <= 23")
else:    
    for i in range(height):
        for j in range(height-1-i):
            print(" ", end="")
        for k in range(i+2):
            print("#", end="")
        print("")        
          