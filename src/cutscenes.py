from graphics import Colors, text_formatter, print_red, print_cyan, print_green, print_reset


def opening_sequence():
    print("Welcome to TTYD!")
    input("Always press ENTER to continue...")
    print("Go buy this game from Nintendo, it is awesome!!")
    input()
    print("We all know the opening book sequence. Imagine the book and backstory and boat and dialogue...")
    input()
    print("It's so beautiful!")
    input()
    print("Alright enough preamble, Mario gets dropped off at the Rogueport Docks.")
    input()
    print("In this tool, you move by inputting your actions as numbers. Press ENTER to continue...")
    input()


def goombella_crump_sequence():
    print("\nMario walks along the dock towards the town entrance.")
    input()
    print("Suddenly, Mario hears a voice cry out!")
    input()
    print(Colors.cyan + "Girl: Hey! What do you want?!? Get away from me, freak!!!")
    input()
    print(Colors.red + "Freak:")
    input()
    text_formatter("""Oh, come off it, you airhead! I know it's tough for you, but don't
            play dumb with me! I've seen you walking around town asking for
            information about the Crystal Stars. Well, now I'm doing the
            asking, so be a good girl and tell us what you know! Right. NOW!""")
    print(Colors.cyan + "Girl: Never! I don't have anything to say to you creeps! Eww!")
    input()
    print(Colors.red + "Freak:")
    input()
    text_formatter("""I suppose it wouldn't be right if a sassy little lass like you met 
            with an untimely demise... Buh! Buh! Buh huh huh! Boys, we're
                   taking this firebrand to our fortress!""")
    print("Creep: As you command, Lord Crump! We're on it!")
    input()
    print(Colors.reset + "Lord Crump and his creeps get closer to the girl.")
    input()
    print(Colors.cyan + "Girl: N-No! Stop right there, you weirdos! I'll scream! Really!")
    input()
    print(Colors.reset +
          "Mario walks up to them, and the Goomba girl takes cover behind him")
    input()
    print(Colors.cyan + "Girl: Like I'd go anywhere with smelly lunatics like you! Hmph! Not likely!")
    input()
    print(Colors.red + "Lord Crump (Aforementioned Freak): Whuh? *to Mario* What do you think YOU'RE doing, chump? You think you can screw up my plans?!?")
    input()
    print(Colors.reset + "Mario is confused")
    input()
    print(Colors.red + "Lord Crump: Gah! It's always something... Looks like I'm going to have to give you a little taste of the old CRUMP-A-BOMB!")
    input()
    print(Colors.reset + "-----BATTLE-----")


def post_crump_opener():
    print(Colors.cyan + "Girl: You did it! You did it! YESSS! And you got Star Points!!!")
    input()
    text_formatter("""Yeah, I bet you know, but you get these things called Star Points when
      you win battles. When you get 100 points, you'll go up a level. Don't
      forget that, OK?""")
    print(Colors.red + "Lord Crump:")
    text_formatter("""Buh! Buh! Buh huh huh! OK, you got a couple decent shots in, I'll
            give you that. But...unfortunately for you...that means...""")
    print("IT'S GO TIME!")
    input()
    print(Colors.reset + "Millions of creeps gather around Mario and the Goomba girl")
    input()
    print(Colors.red + "Lord Crump: PUNISH HIM!")
    input()
    print(Colors.reset + "The creeps gang up on both Mario and the Goomba girl, but she escapes and tells Mario to follow her")
    input()
    print(Colors.cyan + "Girl: Quick! This way!")
    input()
    print(Colors.reset + "Mario escapes as the creeps continue attacking")
    input()
    print(Colors.cyan + "Girl: Phew! What a bunch of loons! Let's just sneak out of here, what do you say?")
    input()
    print(Colors.reset +
          "Mario nods, as he and the girl continue into the main section of Rogueport")
    input()
    print(Colors.red + "Lord Crump: Buh-HUUUUUH?!?")
    input()
    print("Lord Crump: *to creeps* STOPPP!!!")
    input()
    print(Colors.reset +
          "The creeps quit attacking, as Lord Crump looks for Mario and the girl")
    input()
    print(Colors.red + "Lord Crump: Where'd they go?!? Huh? You! Johnson! Did you see them? Did anyone?")
    input()
    print(Colors.reset + "The creeps are clueless")
    input()
    print(Colors.red + "Lord Crump: Uh... Crud! They bolted!")
    input()
    return


def plaza_entrance():
    print(Colors.reset + "Meanwhile, Mario and the goomba girl enter the Rogueport Plaza")
    input()
    print(Colors.cyan + "Girl: Wow, Mister! You...totally saved me! Thanks!")
    input()
    print("Girl: I have just GOT to give you a little reward!")
    input()
    print(Colors.reset + "She kisses Mario")
    input()
    print("Mario nods")
    input()
    print(Colors.cyan + "Girl: My name's Goombella. I'm a student at the University of Goom. Nice to meet ya!")
    input()
    print(Colors.reset + "Mario nods")
    input()
    print(Colors.cyan + "Goombella: So, uh... Who are you?")
    input()
    print(Colors.reset + "Mario exclaims")
    input()
    print(Colors.cyan + "Goombella: ...Mario? Wait, you mean, like, that famous guy? Wow! I can't believe I met you here!")
    input()
    print("Goombella: Cool... Anyway, no offense, but it looks like you just rolled into town yourself. Right?")
    input()
    print("Goombella:")
    text_formatter("""Me, I already HATE it here! There are freaks and weirdos
            EVERYWHERE! It's nasty! I mean, I know the place is called
            Rogueport, so I should have expected it, but sheesh! I'd never come
            to a place like this if there weren't some legendary treasure here.""")
    print(Colors.reset + "Mario exclaims and raises his hand")
    input()
    print(Colors.cyan +
          "Goombella: What? You're looking for the legendary treasure, too? Seriously?")
    input()
    print(Colors.reset + "Mario nods")
    input()
    print(Colors.cyan + "Goombella: Whoa whoa WHOA, bucko! Whatcha got there?")
    input()
    print(Colors.reset + "Mario shows Goombella the map")
    input()
    print(Colors.cyan + "Goombella: Omigosh! Is... Isn't that a treasure map?! You HAVE to tell me where you got that!")
    input()
    print(Colors.reset + "Mario raises his hand")
    input()
    print(Colors.cyan + "Goombella: ...Princess Peach? What?")
    input()
    print(Colors.green + "Voice: Great hoogly-boogly! If it isn't Master Mario!")
    input()
    print(Colors.reset + "Toadsworth appears. A group of Piantas can be seen in the background, beating up a guard with a spear")
    input()
    print(Colors.green + "Toadsworth:")
    input()
    text_formatter("""Bit of a coincidence, bumping into one another in this sort of
            place, hm? Ho ho! So tell me, Master Mario, what in the world
            brings you to this wretched little burg?""")
    print(Colors.reset + "Mario responds by raising his hand")
    input()
    print(Colors.green + "Toadsworth:")
    text_formatter("""...Hmm? Ah! Indeed?!? Princess Peach sent you a letter and a
            treasure map? And she told you she'd meet you here in Rogueport?!?
            Intriguing...""")
    print(Colors.reset + "Mario responds again")
    input()
    print(Colors.green + "Toadsworth:")
    text_formatter("""You're asking me where Princess Peach is? Erm... I was about to ask
            you that. We stoped in this town to acquire a spot of fuel for our
            ship, don't you know... I only took my eye off her for a moment,
            but as soon as I did, she vanished.""")
    print(Colors.reset + "Mario is shocked")
    input()
    print(Colors.green + "Toadsworth:")
    text_formatter("""You know how headstrong she is, Mario... I just assumed she'd be
            back momentarily... But at this point, I fear we must embrace the
            possibility that she may never return. I've been at a loss as to
            what to do. I've been fraught with worry, I tell you!""")
    print(Colors.reset + "Mario responds")
    input()
    print_green("Toadsworth:")
    text_formatter("""But I'm feeling better with you here, Master Mario. Surely we'll
            find her! Surely! But I know my place, Master Mario...and this is
            not it. I leave this task to you.""")
    print_reset("Mario responds")
    input()
    print_green("Toadsworth:")
    text_formatter("""I believe I'll recline in the Inn right over there and enjoy a spot
            of tea, perhaps. In fact, I highly recommend it, particularly if
            you find your HP (Heart Points) running low. Just drop on INN! Ho
            ho! ...Yes, anyway, a little rest there will fill all of your HP. I
            must say, though, the rest of this town is a bit...rough. Yes,
            rough, indeed...""")
    print_reset("Toadsworth walks into the Inn while huffing to himself")
    input()
    print_cyan("Goombella:")
    text_formatter("""Um... Princess Peach? Did he mean, like, Peach, the Mushroom Kingdom
           princess?!? The princess who always gets nabbed by Bowser, the Koopa
           king? The one you rescue? Wait a sec'! This is crazy! Princess...
           PEACH sent you that treasure map?""")
    print_reset("Mario nods")
    input()
    print_cyan("Goombella:")
    text_formatter("""Whoa. This is really intense. Well, where could she have gone, then,
           do you think? You think maybe she got sick of waiting and went to
           find the treasure on her own?""")
    print_reset("Mario thinks")
    input()
    print_cyan("Goombella")
    text_formatter("""Oooh! Oooh! I know, Mario! Come with me! One of my professors is
           here researching that treasure. We'll show him your map! If we start
           looking for the treasure, then maybe we'll catch up to Princess
           Peach!""")
    print_reset("Mario nods")
    input()
    print_cyan("Goombella: Great! We're all good, then! Let's go, Mario!")
    input()
    print_reset("Goombella joined your party!")
    input()
    print("Goombella's Abilities: A Primer")
    input()
    print("You've unlocked her Tattle ability on the menu")
    input()
    print("-----Rogueport Plaza-----")
    print("1. Move")
    print("2. Tattle <---")
    print("3. Save")
    input()
    print("Use this to get information about nearby people, places, and objects.")
    input()
    print("For example:")
    input()
    print("-----Rogueport Plaza-----")
    print("""This is Rogueport Plaza. It's the center of town, and the main business district. \nIt's a crossroads where many people meet, \nincluding more than a few shady characters.""")
    input()
    text_formatter("""Goombella can give you hints when she answers, so ask her for information
    often! And of course, Goombella can be quite helpful in battle, too. She jumps
    in the air to attack enemies with a nasty Headbonk. She can also look up enemy
    HP and weaknesses with her Tattle ability!""")
    print("-----Primer Over-----")
    input()
    print_cyan("Goombella:")
    text_formatter("""First off, we gotta go find my professor. Thing is, since I just got
        to town myself...I, um, don't actually know where he lives. So keep
        an eye out!""")
    input()
    print_reset("End of cutscene")
