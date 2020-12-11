## Port 8200

Here you had an image gallery type page.  There was an upload option, and a page to browse the uploaded images.  

At first I tried the normal things like:
- uploading a php file (got file extension blocking)
- uploading a php file with a double extension .jpg.php (got mimetype blocking)
- various other more "advanced" techniques

Then I remembered about using a comment tag inside a JPG to execute PHP.  

I constructed an image using the following:
`exiftool -Comment="<?php system('ls -aRl ..'); __halt_compiler();" test.jpg`

I then just renamed this to `test.jpg.php` and it worked.

NOTE.  I first tried system($_GET['cmd']), but kept getting an error that seemed to indicate $_GET was either null or not an array.  But because I didn't want to spend too much time on this, I just hardcoded the commands I needed, adjusted the JPEG and uploaded each time until I found what I needed.  I was hoping to spend a bit more time later to see why this was happening.  
