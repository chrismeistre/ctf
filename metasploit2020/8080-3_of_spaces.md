## Port 8080

You are greeted with a login page, and given a valid username.  The objective is to find another valid username.  There is a hint here that says if you are observant enough, you'll be able to see how to accomplish this.  

The first thing I did was send the valid username `guest` and then an invalid one `guest2` to see if there are different error messages, or headers.  But that was not the case.  As we didn't have a password, both logins would be invalid, although `guest` is a valid username.    

What I did notice though was when you did send the `guest` (valid) username, it takes quite a bit longer to respond, versus the `guest2` (invalid) one.  

I made a little script to brute force some passwords, and was able to find the value username.  
