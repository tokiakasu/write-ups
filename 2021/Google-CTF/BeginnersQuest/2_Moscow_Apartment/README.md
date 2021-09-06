## Moscow - Apartment
Category: `misc`

## Description
> It’s a cold day, and the snow is falling horizontally. It pierces your sight. You better use those extra pairs of socks that you were strangely given by the driver. Someone is waving on the other side of the street. You walk over to her. "Hi AGENT, I’m AGENT X, we’ve found the apartment of a person that we suspect got something to do with the mission. Come along!."

> Challenge: Logic Lock (misc)
It turned out suspect's appartment has an electronic lock. After analyzing the PCB and looking up the chips you come to the conclusion that it's just a set of logic gates!

## Analysis
We are given a ZIP-archive, unzip it and we get a picture that looks like an electric circuit and hint for the flag" 
`Flag: "CTF{" + inputs that need to be set, sorted + "}"`

This was the first time I had seen anything like this, so I started googling "electrical circuit input abc" and immediately saw the term "logic gates"

> Explanation of logic gates: build-electronic-circuits.com/logic-gates/

Now I started thinking 
> What do I need to do? > I have a logic gate, a set of letters and output 1 > The hint says: "If only inputs A, B and C should be set, the flag will be CTF{ABC}" > I need to find which letter inputs

Here I thought that all if the letters have 1 and if I put them through the logic gate, I would know which letters are actually entered (spoiler: it was a waste of time). After a full day of research, going over my own thoughts, my friend came over and said: "Lolz, it's easy, just do the reverse" We found a board, started drawing logic gates, putting 1 through all the logic gates.

![board](https://github.com/curvtd/write-ups/blob/master/2021/Google-CTF/BeginnersQuest/2_Moscow_Apartments/images/board.png)

We get the sequence "0110010011", which means the input letters "BCFIJ". 

FLAG: CTF{BCFIJ}
