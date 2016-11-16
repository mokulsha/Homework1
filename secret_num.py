secret = 36

guess = int(raw_input("Take a guess: "))
print guess
i = 1 # tries

while (guess != secret):
    if (guess < secret):
        print("Wrong. Secret number is higher.")
    else:
        print ("Wrong. Secret number is lower.")

    guess = int(raw_input("Take a guess: "))
    i = i + 1

print "Yes, you guessed it! The secret number was", secret