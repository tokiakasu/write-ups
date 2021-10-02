## Leviathan 1-2
Category: `binary`

## Description
There is no information for this level, intentionally.

## Analysis
```
leviathan1@leviathan:~$ ls
check
leviathan1@leviathan:~$ file check 
check: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=c735f6f3a3a94adcad8407cc0fda40496fd765dd, not stripped
```

Binary CTF has two ways, "simple `strings strace ltrace`" or "understand this machine code however you want with `radare2 IDA Ghidra`". Let's try the simplest way with `strings check`.
```
GLIBC_2.0
PTRhp
QVh;
secrf
love
UWVS
t$,U
[^_]
password: 
/bin/sh
Wrong password, Good Bye ...
```
Almost nothing interesting except the execution of `/bin/sh` after entering the password. This probably means that after entering the password we get control of a new user, I suggest the next level user leviathan2. To confirm my assumption, let's check the permissions of the file
```
leviathan1@leviathan:~$ ls -l 
total 8
-r-sr-x--- 1 leviathan2 leviathan1 7452 Aug 26  2019 check
```
My hypothesis turned out to be correct! Here we see the setuid bit "s", which tells the OS to execute this program with the userid of its owner, and the owner is leviathan2. To use `strace` and `ltrace` properly, I watched a video on binary exploitation (I highly recommend watching the full playlist on binary exploitation when it's time to dive into reverse)
> Simple Tools and Techniques for Reversing a binary - https://youtu.be/3NTXFUxcKPc

We get useful definitions of `strace` and `ltrace` so that there is less confusion
> strace - intercepts system calls make by the glibc and other libraries directly into the Linux Kernel

> ltrace - intercepts library calls and system calls made by your application to C libraries such as the glibc

Calling `strace` outputs too much machine slang and gibberish of system calls, but if we call `ltrace`, the program stops at the lib function "getchar()" to enter values and then we see a function call "strcmp()" which compares the entered values with the correct password `sex`. Let's try the password
```
leviathan1@leviathan:~$ ltrace ./check 
__libc_start_main(0x804853b, 1, 0xffffd784, 0x8048610 <unfinished ...>
printf("password: ")                                                                                                    = 10
getchar(1, 0, 0x65766f6c, 0x646f6700password: dsdsd
)                                                                                   = 100
getchar(1, 0, 0x65766f6c, 0x646f6700)                                                                                   = 115
getchar(1, 0, 0x65766f6c, 0x646f6700)                                                                                   = 100
strcmp("dsd", "sex")                                                                                                    = -1
puts("Wrong password, Good Bye ..."Wrong password, Good Bye ...
)                                                                                    = 29
+++ exited (status 0) +++
leviathan1@leviathan:~$ ./check 
password: sex
$ bash
leviathan2@leviathan:~$ 
```
Now we can check thepassword for this user in /etc/leviathan_pass
```
leviathan2@leviathan:~$ cat /etc/leviathan_pass/leviathan2
ougahZi8Ta
```

