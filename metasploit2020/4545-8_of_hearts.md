## Port 4545

You are able to download two files:
- 8_of_hearts.elf
- 8_of_hearts.enc

I opened up 8_of_hearts.elf in Ghidra, and got the decompiled main() function.  

Looking at the code again now, I realise there was perhaps another intended way of doing this, but my eye was drawn to the fact that it looked like there was a XOR function being used on the file.  

Pressed for a bit of time, I simple loaded up Cyberchef, uploaded the 8_of_hearts.enc, and used the XOR (with key: `A`) function on there.  From the header I saw result is a valid PNG file.  

The way I saw now while writing this is that you could potentially just run the 8_of_hearts.elf, and send a string of repeating `buffalo`, and that also decrypts the file.  
