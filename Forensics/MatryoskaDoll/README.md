# Matryoshka Doll

Matryoshka dolls are classified as dolls of decreasing size. This link downloads a file
named as dolls.jpg. Using __binwalk__ utility to extract the embedded files present in 
the image results in __`_dolls_extracted`__ folder. On navigating to the folder, we get 
multiple images. On executing binwalk repeatedly on those images and extracting the .xip
files, we obtain the __flag.txt__ file which contains the flag.

> The workflow is descirbed as follows:

```bash
binwalk -e dolls.jpg
cd _dolls.jpg.extractec
unzip -d 4286C 4286C.zip
cd 4286C/base_images
binwalk -e 2_c.jpg
cd _2_c.jpg.extracted/
unzip -d 2DD3B 2DD3B.zip
cd 2DD3B/base_images
binwalk -e 3_c.jpg
cd _3_c.jpg.extracted/
unzip -d 1E2D6 1E2D6.zip
cd 1E2D6/base_images
binwalk -e 4_c.jpg
cd _4_c.jpg.extracted/
cat flag.txt
```
The obtained flag is __picoCTF{336cf6d51c9d9774fd37196c1d7320ff}__


