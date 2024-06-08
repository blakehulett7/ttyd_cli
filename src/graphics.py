import math


class Colors:
    reset = "\x1b[0m"
    red = "\x1b[31m"
    green = "\x1b[32m"
    yellow = "\x1b[33m"
    blue = "\x1b[34m"
    magenta = "\x1b[35m"
    cyan = "\x1b[36m"


def text_formatter(text):
    lines = text.split("\n")
    stripped_lines = list(map(lambda line: line.strip(), lines))
    stripped_text = " ".join(stripped_lines)
    raw_text = stripped_text.lstrip()
    raw_text_size = len(raw_text)
    number_of_boxes = len(raw_text) // 80 + 1
    line_size = math.ceil(raw_text_size / number_of_boxes)
    boxes = []
    for i in range(number_of_boxes):
        if len(raw_text) < line_size:
            boxes.append(raw_text)
        else:
            if "..." in raw_text[line_size:]:
                dividing_index = raw_text[line_size:].index(
                    "...") + 3 + line_size
            else:
                first_period_index = float("inf")
                first_exclamation_index = float("inf")
                if "." in raw_text[line_size:]:
                    first_period_index = raw_text[line_size:].index(
                        ".") + line_size
                if "!" in raw_text[line_size:]:
                    first_exclamation_index = raw_text[line_size:].index(
                        "!") + line_size
                dividing_index = min(first_period_index,
                                     first_exclamation_index) + 1
            if dividing_index == float("inf"):
                boxes.append(raw_text)
            else:
                first_box = raw_text[:dividing_index]
                boxes.append(first_box)
                raw_text = raw_text[dividing_index:].lstrip()
    for box in boxes:
        if box != "":
            print(box)
            input()
