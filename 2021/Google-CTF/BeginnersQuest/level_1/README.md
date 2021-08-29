## Novosibirsk - Chemical plant
Category: `web(?)`

## Description
> Challenge: CCTV (rev)
You arrive at your destination. The weather isn't great, so you figure there's no reason to stay outside and you make your way to one of the buildings. No one bothered you so far, so you decide to play it bold - you make yourself a cup of coffee in the social area like you totally belong here and proceed to find an empty room with a desk and a chair. You pull out our laptop, hook it up to the ethernet socket in the wall, and quickly find an internal CCTV panel - that's a way better way to look around unnoticed. Only problem is... it wants a password.
https://cctv-web.2021.ctfcompetition.com/

## Analysis
When we enter the site, we see a login form that requires a password.

![form](https://github.com/curvtd/write-ups/blob/master/2021/Google-CTF/BeginnersQuest/level_1/images/login.png)

Based on past experience, I tried to look through the source code of the page and found a script with the "checkPassword" function, just what I needed!

![script](https://github.com/curvtd/write-ups/blob/master/2021/Google-CTF/BeginnersQuest/level_1/images/script.png)

I wasn't sure what language it was, so I went to dpaste.com to determine the programming language.

![language](https://github.com/curvtd/write-ups/blob/master/2021/Google-CTF/BeginnersQuest/level_1/images/language.png)

So, it's JavaScript. I didn't know JS at all, so I had to watch Youtube. 
> Learn JavaScript in 12 minutes: https://youtu.be/Ukg_U3CnJWI
> JavaScript Array Map: https://youtu.be/G3BS3sh3D8Q

After watching it, I begin to understand the script and now it remains to explain to myself what parts of the code do.

![explanation](https://github.com/curvtd/write-ups/blob/master/2021/Google-CTF/BeginnersQuest/level_1/images/code_explanation.png)

### Links
> ASCII table: asciitable.com
> hex converter: hexadecimaldictionary.com
> JS Event Keycodes: keycode.info
> Online board: app.ziteboard.com


## Solution
Since I now have a formula, I wrote a simple program to get the code of the symbol and the symbol itself

```
while True:
    _0xCafe = 51966
    number = int(input("Enter a number: "))
    result = number - _0xCafe

    print(f"{result} = {chr(result)} \n")
```

With the formula I got the password "GoodPassword", the password was correct and I successfully logged in.

![flag](https://github.com/curvtd/write-ups/blob/master/2021/Google-CTF/BeginnersQuest/level_1/images/flag.png)
