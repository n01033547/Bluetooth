import sys

lp = open("itemlist.txt", "w")

items = {
    "8725000174958": "Beer",
    "4043058010443": "Tobacco",
    "50008667": "Rizzla",
    "X001FYH5BD": "Raspberry Pi 3",
    "Version 2": "QR Code",
	"my QR code": "This is my QR Code"
}

count = 0

try:
    while True:
        code = raw_input("Scan: ")
        if code in items:
            count += 1
            item = items.get(code)
            print("Added " + item)
            lp.write(item + "\n")
        else:
            print("We don't have that product in our database!")
        if count == 3:
	    lp.close()
            print("Basket full!")
            lp.write("\x1E") # cut & present
            lp.close()
			lp.flush()
			count= 0

except KeyboardInterrupt:
    lp.close()
    print ("\nExit")