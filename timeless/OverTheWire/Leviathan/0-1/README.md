## Leviathan 0-1
Category: `unix`

## Description
There is no information for this level, intentionally.

## Analysis
First of all, let's see what files we have

```
leviathan0@leviathan:~$ ls -a
.  ..  .backup  .bash_logout  .bashrc  .profile
leviathan0@leviathan:~$ ls .backup/
bookmarks.html
```

There is a hidden folder with html document, tried `cat` file and got a bunch of random links. I don't see the point in trying to find our password manually, so let's use `grep`.
```
leviathan0@leviathan:~$ cat .backup/bookmarks.html | grep password
<DT><A HREF="http://leviathan.labs.overthewire.org/passwordus.html | This will be fixed later, the password for leviathan1 is rioGegei8m" ADD_DATE="1155384634" LAST_CHARSET="ISO-8859-1" ID="rdf:#$2wIU71">password to leviathan1</A>
```

Flag found - rioGegei8m
