## Port 1337

This was a terminal program running on port 1337.  At first I thought it would be buffer overflow, but I wasn't sure of how to do it if we don't have access the the binary.

I tried various payloads of various lengths, but couldn't get it to crash.  So I left it a bit.

While trying to solve the other challenge (that involved buffer overflow), I came across an article mentioning string format vulnerabilities in C.  

I tried one of two of the payloads, and saw it was giving me back results as if it is vulnerable to it.

I was finally able to leak memory by using option 2 and `%9$s`, and this gave me the flag.
