# FileTypes

The link basically downloads a pdf which is initially __corrupted__ since it was a shutil
archive file. On reading the  contents of the file using __micro__ , the __#!/bin/sh__ line was commented
. I changed teh extension of the file from __Flag.pdf__ to __Flag.sh__ and gave it executablee
permissions using:
```bash
chmod +x Flag.sh
```
Then, I tried using __binwalk__
```bash
	binwalk flag -e 
	cd _flag.extracted
	binwalk 64     
	binwalk -e 64                                   
	lzip -d flag                            
	binwalk flag.out
	mv flag.out flag.lz4
	lz4 -d flag.lz4 
	binwalk flag
	mv flag flag.lzma   
	lzma -d flag.lzma 
	binwalk flag                                   
	binwalk flag -e                                 
	cd _flag.extracted
	lzop -d -k flag2.lzop -o flag3      
	lzip -d -k flag3
	xz -d -k flag4.xz
	cat 0
```

The output was
>7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f
>6630725f3062326375723137795f32373866316131387d0a

On converting the __hexcode__ to string, the flag was obtained

The flag is: __picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_278f1a18}__