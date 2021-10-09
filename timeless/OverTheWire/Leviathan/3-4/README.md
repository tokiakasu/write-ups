## Leviathan 3-4
Category: `binary`

## Description
There is no information for this level, intentionally.

## Analysis
```
leviathan3@leviathan:~$ ls
level3
leviathan3@leviathan:~$ ./level3 
Enter the password> ddd
bzzzzzzzzap. WRONG
```
As always with binary `strings and trace until it is done'. This is a binary file that asks for a password, let's see what functions were called at runtime
```
leviathan3@leviathan:~$ ltrace ./level3 
__libc_start_main(0x8048618, 1, 0xffffd784, 0x80486d0 <unfinished ...>
strcmp("h0no33", "kakaka")                                            = -1
printf("Enter the password> ")                                        = 20
fgets(Enter the password> sss
"sss\n", 256, 0xf7fc55a0)                                       = 0xffffd590
strcmp("sss\n", "snlprintf\n")                                        = 1
puts("bzzzzzzzzap. WRONG"bzzzzzzzzap. WRONG
)                                            = 19
+++ exited (status 0) +++
```
As we see, this binary calls the function `strcmp()` which compares the given string with the correct string `snlprintf` and outputs the result. Let's try to use "snlprintf" as a password
```
leviathan3@leviathan:~$ ltrace ./level3 
__libc_start_main(0x8048618, 1, 0xffffd784, 0x80486d0 <unfinished ...>
strcmp("h0no33", "kakaka")                                            = -1
printf("Enter the password> ")                                        = 20
fgets(Enter the password> snlprintf
"snlprintf\n", 256, 0xf7fc55a0)                                 = 0xffffd590
strcmp("snlprintf\n", "snlprintf\n")                                  = 0
puts("[You've got shell]!"[You've got shell]!
)                                           = 20
geteuid()                                                             = 12003
geteuid()                                                             = 12003
setreuid(12003, 12003)                                                = 0
system("/bin/sh"$ whoami
leviathan3
$ exit
 <no return ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                                                = 0
+++ exited (status 0) +++
```
This works, but I don't know why executing via ltrace doesn't give us a leviathan4 shell, let's try just execute
```
leviathan3@leviathan:~$ ./level3 
Enter the password> snlprintf
[You've got shell]!
$ whoami
leviathan4
$ cat /etc/leviathan_pass/leviathan4
leviathan4_password
```

