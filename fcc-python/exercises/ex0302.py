# try & except 

hours = input("Enter hours: ")
rate = input("Enter rate: ")

try:
    fh = float(hours)
    fr = float(rate)
except:
    print("error: please enter numeirc input")
    quit()

print(fh, fr)
if fh > 40:
    # print ("overtime pay")
    reg = fh * fr
    otp = (fh - 40.0) * (fr * 0.5)
    # print(reg, otp)
    xp = reg + otp
else:
    # print("Regular pay")
    xp = fh * fr

print("Pay: ", xp)

