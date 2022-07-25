#!/usr/bin/bash
#!/usr/bin/expect -f

PASSWORD="KRYPTONISGREAT"
sshpass -p $PASSWORD ssh krypton1@krypton.labs.overthewire.org -p 2231 << 'EOL'
    echo "The password to level2 is :"
    cd /krypton/krypton1
	alias rot13='tr a-zA-Z n-za-mN-ZA-M'
	var=$( cat krypton2 )
    echo $var | python -c 'import sys; print sys.stdin.read().encode("rot13")'
EOL