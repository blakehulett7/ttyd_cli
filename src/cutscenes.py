from graphics import Colors, text_formatter


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
    print(Colors.reset + "Millions of X-Nauts gather around Mario and the Goomba girl")
    input()
    print(Colors.red + "Lord Crump: PUNISH HIM!")
    input()
    print(Colors.reset + "The X-Nauts gang up on both Mario and the Goomba girl, but she escapes and tells Mario to follow her")
    input()
    print(Colors.cyan + "Girl: Quick! This way!")
