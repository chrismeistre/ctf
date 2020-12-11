# Metasploit CTF 2020

## Website: https://metasploitctf.com/

### Team: HackSouth

This was the first time I took part in this CTF.  I think it has a lot to offer us newbies, and I enjoyed it a lot.  A lot of web application attack techniques were being tested. 


I unfortunately didn't have enough time to still create detailed instructions for each challenge we solved, but I'll try and upload as time goes on. 


## Starting Point 

To start off with, we had access to a Kali and a Ubuntu instance that we could log onto.  The idea would be that you connect to the Kali box, and use that as a jump box to attack the Ubuntu instance.  You were not able to connect directly to the Ubuntu box.  

Initially I logged into the Kali box, and started using the terminal.  It worked okay to start off with, but using my own local box would work easier for me, because I know where everything is.  It has been customised over a while.  

I then decided to setup a SSH tunnel, through the Kali box, so that I could access everything from my local box.  

`ssh -D 1088 -i metasploit_ctf_kali_ssh_key.pem kali@3.85.108.244`

Then I just setup proxychains.conf to point to port 1088, and I could access everything locally.
