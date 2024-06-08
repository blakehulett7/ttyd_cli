import math


def text_formatter(text):
    lines = text.split("\n")
    stripped_lines = list(map(lambda line: line.strip(), lines))
    stripped_text = " ".join(stripped_lines)
    raw_text = stripped_text.lstrip()
    raw_text_size = len(raw_text)
    number_of_boxes = len(raw_text) // 80 + 1
    line_size = math.ceil(raw_text_size / number_of_boxes)
    boxes = []
    # Recursive function here?
    first_period_index = raw_text[line_size:].index(".") + line_size
    first_exclamation_index = raw_text[line_size:].index("!") + line_size
    dividing_index = min(first_period_index, first_exclamation_index) + 1
    first_box = raw_text[:dividing_index]
    return raw_text, first_box


print(text_formatter("""Oh, come off it, you airhead! I know it's tough for you, but don't
            play dumb with me! I've seen you walking around town asking for
            information about the Crystal Stars. Well, now I'm doing the
            asking, so be a good girl and tell us what you know! Right. NOW!"""))
