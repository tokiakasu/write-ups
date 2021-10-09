## Leviathan 6-7
Category: `binary`

## Description
There is no information for this level, intentionally.

## Analysis
```
leviathan6@leviathan:~$ ls -al
total 28
drwxr-xr-x  2 root       root       4096 Aug 26  2019 .
drwxr-xr-x 10 root       root       4096 Aug 26  2019 ..
-rw-r--r--  1 root       root        220 May 15  2017 .bash_logout
-rw-r--r--  1 root       root       3526 May 15  2017 .bashrc
-r-sr-x---  1 leviathan7 leviathan6 7452 Aug 26  2019 leviathan6
-rw-r--r--  1 root       root        675 May 15  2017 .profile
leviathan6@leviathan:~$ ./leviathan6 
usage: ./leviathan6 <4 digit code>
leviathan6@leviathan:~$ ltrace ./leviathan6 3333
__libc_start_main(0x804853b, 2, 0xffffd774, 0x80485e0 <unfinished ...>
atoi(0xffffd89f, 0, 0xf7e40890, 0x804862b)                                                                              = 3333
puts("Wrong"Wrong
)                                                                                                           = 6
+++ exited (status 0) +++
leviathan6@leviathan:~$ strings ./leviathan6
...
[^_]
usage: %s <4 digit code>
/bin/sh
Wrong
;*2$"
...
```
There is a binary which requires a 4-digit code and executes `/bin/sh` after entering the desired digit. Let's write a simple bruteforce
```
for digits in {0000..9999}
do
	$HOME/leviathan6 $digits
done
```
Time to execute
```
leviathan6@leviathan:~$ ./script.sh
...
Wrong
Wrong
Wrong
Wrong
$ whoami
leviathan7
$ cat /etc/leviathan_pass/leviathan7
leviathan7_password
```
In a ~minute we got shell and read the password

