## Port 8123

You are giving a website where you can go reset your password.  Part of the reset is that they give you a hint.

When I looked at the response coming back from the api call, I saw that it's including the md5 hash.

The hint was ```The password begins with 'ihatesalt'```.

I further checked some of the HTML and javascript, and was able to determine the password must be between a length of 9 and 14.  

I saved the hash into a file, and ran: `john -mask=ihatesalt?a?a?a?a?a -min-len=9 -max-len=14 --format=Raw-md5 crack.txt`

It cracked it in 38 seconds.

Once you log in, you are given the file for the flag.
