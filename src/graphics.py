def text_formatter(text):
    lines = text.split("\n")
    stripped_lines = list(map(lambda line: line.strip(), lines))
    stripped_text = " ".join(stripped_lines)
    raw_text = stripped_text.lstrip()
    return raw_text


print(text_formatter("""Oh, come off it, you airhead! I know it's tough for you, but don't
            play dumb with me! I've seen you walking around town asking for
            information about the Crystal Stars. Well, now I'm doing the
            asking, so be a good girl and tell us what you know! Right. NOW!"""))
