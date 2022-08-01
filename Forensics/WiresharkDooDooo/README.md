# WireShark doo dooo doooo

The link download a .pcapng file which contains dump of data packets sent over the 
network, on opening the file via __Wireshark__, the packets were mostly sent via the 
__TCP Handshake__ protocol and __HTTP__, I exported the files corresponding to the __HTTP PROTOCOL__
, I found two a __html file__ corresponding to packet number 827 and of 47 bytes and a
__text file__ corresponding to packet number 964 and of 4 bytes. The __text file__ read __none__
and on the opening the __html file__ the output was:

Gur synt vf cvpbPGS{c33xno00_1_f33_h_qrnqorrs}

I guessed it to be a simple __rotation cipher__ and applied __rot13__ to it

```bash
cat textplain | rot13
```
The output was: 

The flag is __picoCTF{p33kab00_1_s33_u_deadbeef}__

