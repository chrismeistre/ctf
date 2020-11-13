# Website: https://0xcon.co.za/

**Description from website: **

`We're hosting a challenge at challenge.0xcon.co.za. It's a normal CTF with a flag at the end. You'll find an email address to mail the flag to and there's a prize each for the first two peeps we get mails from. We'll ship these anywhere in South Africa with Aramex and will talk shipping options with anyone overseas. Normal CTF rules apply. Try not to break it for others, and if you do, send a mail to 0xc0ffeejhb@gmail.com and we'll reset it quick. Good luck!`

# Step 1
Browsed  http://challenge.0xcon.co.za

Noted it was running Wordpress

Found a link at the bottom going to https://github.com/Elliot-Mr-Robot/

Enumerated through the code on the github page

Found what looked like a base64 encoded string randomly in the middle of a code block

Decoded it to get a string

At this point I thought, "Okay, that's the flag for the CTF, and I'm done".  I sent a message to the organiser to see, but it just didn't seem right for it to be so easy.

Reading the site again, I noted the "Path to System Admin" title.  So I decided to dig a bit deeper while I waited for a response.

# Step 2
Browsed to http://challenge.0xcon.co.za/wp-admin and saw it was presenting me with a login

Going to http://challenge.0xcon.co.za/?author=X gave me a username to try, so I decided to try that with the password I got in Step 1 (which I initially thought was the flag)

When I could log in, I realised that this is going to be a longer process than anticipated.

# Step 3
I wanted to get a shell, to explore what's on the system.

I checked and was able to edit plugins and themes using the WP interface.  I added in some PHP to create a reverse shell back to me.

And voila, I was in, but logged in as a low priviledge user.

# Step 4
This involved a LOT of enumeration to see what is going on. 

### A summary of what I found:
I found DB login details, but on enumerating the DB, I could not find anything interesting

I looked at the versions of all the services running, and tried researching about exploits for them.  But the system was quite up to date.

There were two users (Txxxxx, Exxxxx)

There were flags in both their directories

The user Txxxxx was also logged in via SSH, and it was noted the this user was the only one that could SSH in.

I found a password in his directory, but it wasn't working for su or ssh.  Initially I thought someone had been able to log in, and change the password already to mess with the rest of the CTFers.

There was a hidden directory in the /home folder, that was a shell script being triggered by a cron.  It was being run as the Exxxxx user.

Initially I first modified it so that I could gain access to a zip file that was located on the server, under this user's ownership.  I got this zip file onto my box, and ran crack on the password.  I was able to get the password for the zip, but all I got out of it was a MD5 hash.  I tried the normal password lists, and online services, but didn't get anywhere.  I setup john to run with some rules overnight, and just left it.  In case something comes from it.

At this point I also made sure that none of the user and password combinations I had would work.


# Step 5
I then modified the script to create another reverse shell to my box.  I was now logged in as the user Exxxxx.

I found a service running on port 8yyy, and 8xxx.  I wasn't sure what the 8yyy was, and with limited tools on the box, I had to make another plan to try and connect to it.

I decided to setup remote SSH tunneling to my box for the first port.  I tested it, and couldn't get anything usefull from it.  For the second port, I knew exactly what it was and how to exploit it.  But it relied on me having credentials for it.

I then remembered about the credentials I had found earlier.  I setup SSH tunneling again.

I did a little bit of brute forcing with the user and password combinations I had collected already, together with a default login username for this service.  

I was able to log in

# Step 6
At this point I knew exactly what to do get a root shell.  I loaded up msfconsole, and used the module available there.  I tested afterwards if I could also get in with just uploading a shell manually.

From here it was as simple as capturing the flag and decoding the information therein
