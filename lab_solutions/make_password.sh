#!/bin/bash

# force caller to enter password twice
read -p 'Enter password: ' pass1
read -p 'Repeat password: ' pass2

# make sure passwords match
if [ $pass1 != $pass2 ]; then
	echo "passwords do not match"
	exit 2
fi

# return sha512 hash
echo $pass1 | mkpasswd --method=sha-512 --stdin
