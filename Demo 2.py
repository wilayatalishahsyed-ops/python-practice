"""Clean up a name. A form gave you the name " aMNA rAZA ".
 Clean it so it reads Amna Raza (look up the .title() method), 
 then print Welcome, Amna Raza! Your name has 9 characters. 
 using an f-string and len()."""

 
name = " aMNA rAZA "

clean_name = name.strip().title()
characters = len(clean_name)

print(f"Welcome, {clean_name}! Your name has {characters} characters.")


name = " aMNA rAZA "

# Remove extra spaces and correct the name
clean_name = name.strip().title()

# Count characters
characters = len(clean_name)

# Print welcome message
print(f"Welcome, {clean_name}! Your name has {characters} characters.")


""" Clean an email. Clean " Ali.Khan@GMAIL.com " so it has
 no spaces and is all lowercase, then print Email: ali.khan@gmail.com
   (18 characters)."""


email = " Ali.Khan@GMAIL.com "

clean_email = email.strip().lower()

characters = len(clean_email)

print(f"Email: {clean_email} ({characters} characters)")


"""A receipt line. The item name is " wireless MOUSE ",
 the price is 2499 and the quantity is 3. Print exactly: 
 Wireless Mouse x3 = Rs 7,497. Work out the total in code;
   don't type the number."""


item_name = " wireless MOUSE "
price = 2499
quantity = 3

clean_name = item_name.strip().title()
total = price * quantity

print(f"{clean_name} x{quantity} = Rs {total:,}")

