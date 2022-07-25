# Trivial File Transfer Protocol 

This challenge was quite interesting. The contents of the file contains a pcapng file 
which basically contains __dump__ of packets of data transferred over a network. This is stored in 
__PCAP Next Generation__ File Format, which is a standard mode of storing data. Pcapng containes 
several blocks of data which containes information like _enhanced packet block_, _interface description block_
_interface statistics block_, _simple packet block_, _named resolution block_ etc.

I used _WireShark_ to open the .pcapng file and analysed the data transmitted over the network
There was a file named _instructions.txt_ and three .bmp files named as __picture1.bmp__,
__picture2.bmp__, __picture3.bmp__, __plan__. On saving these exported files I opened the 
__instructions.txt__ file. 

The contents of the file: 
GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA

This turned out to be __substitution cipher__=__ROT13__ :)
```bash
cat instructions.txt | rot13 > hint.txt
```
On putting the spaces, the __hint.txt__ file reads:
TFTP DOESNT ENCRYPT OUR TRAFFIC SO WE MUST DISGUISE OUR FLAG TRANSFER. FIGURE OUT A WAY TO HIDE THE FLAG AND I WILL CHECK BACK FOR THE PLAN

I checked out the contents of the __plan__ file:
VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF
This also surprisingly turned out to be __substitution cipher__=__ROT13__ :)
```bash
cat plan | rot13 > hint2.txt
```
On putting the spaces in the text, the contents of the __hint.txt__ file reads:
I USED THE PROGRAM AND HID IT WITH-DUE DILIGENCE. CHECK OUT THE PHOTOS

Then I tried __steghide__ to decode the three .bmp files
```bash
sudo apt install steghide
```
Each of the three images asked for a __passphrase__ while extracting with __steghide__
I looked at the text inside __hint2.txt__ where it was mentioned as HID IT WITH
__DUE DILIGENCE__. So I thought the password to be __DUE DILIGENCE__ and the __picture3.bmp__
when extracted with steghide with the passphrase gave a file named as __flag.txt__

```bash
steghide extract -sf picture3.bmp
```

The following __flag__ is: 
picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}