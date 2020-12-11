## Port 6868

You are presented with a website where you can register.  

Once you register you see that they are taking the first letter of your first name, the first letter of your middle name and the last letter of your last name, to form some sort of UID.  

It also indicates that you can access your notes at `/notes/FML/id`

Where `FML` is my UID (FIRST MIDDLE LAST)  

On the front page you find other users, and using the same format for the UID, you can get `BD`, `TW` and `MC`.  

I wrote a small script to enumerate all the notes.

There was a note of them talking about the admin, `Beta`, as well as an indication of what her middle names might be.  The middle names spelled out `UDD`.

So I had `BUDD`, and knew I needed one more character.  I could brute force it, but thought I'll just try and add a Y to make it `BUDDY`.  

That worked and I could see the notes.  I then looked at the URL for the files, and was able to enumerate her files using the format `/files/BUDDY/1`, etc.

