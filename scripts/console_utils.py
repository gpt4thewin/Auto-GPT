from colorama import Fore, Style
import random
import time
import speak
from config import Config

cfg = Config()

def print_with_color(text, color=None):
    if color:
        print(color + text + Style.RESET_ALL, end="", flush=True)
    else:
        print(text, end="", flush=True)

def print_to_console(
        title,
        title_color,
        content,
        content_color=None,
        speak_text=False,
        min_typing_speed=0.05,
        max_typing_speed=0.01):
    global cfg
    if speak_text and cfg.speak_mode:
        speak.say_text(f"{title}. {content}")
    print_with_color(title + " " + Style.RESET_ALL, title_color)
    if content:
        if isinstance(content, list):
            content = " ".join(content)
        words = content.split()
        for i, word in enumerate(words):
            print_with_color(word + " ", content_color)
            if i < len(words) - 1:
                print(" ", end="", flush=True)
            typing_speed = random.uniform(min_typing_speed, max_typing_speed)
            #time.sleep(typing_speed)
            # type faster after each word
            min_typing_speed = min_typing_speed * 0.95
            max_typing_speed = max_typing_speed * 0.95
    print()