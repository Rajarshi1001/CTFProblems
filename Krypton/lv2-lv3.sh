#!/usr/bin/bash
PASSWORD="ROTTEN"
sshpass -p $PASSWORD ssh krypton2@krypton.labs.overthewire.org -p 2231 << 'EOL'
	var=$(mktemp -d)
	cd $var
    ln -s /krypton/krypton2/keyfile.dat
	chmod 777 .
	ln -s /krypton/krypton2/krypton3
	chmod 777 .
    /krypton/krypton2/encrypt krypton3
    echo -e "The ciphertext is:" 
    cat ciphertext
    echo -e 
    echo -e "The Password to level 3 is:"
    output=`cat krypton3 | tr "M-ZA-Lm-za-l" "A-Za-z"` 
    echo -e $output
EOL
