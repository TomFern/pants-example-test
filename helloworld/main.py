# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from colors import green

from helloworld.config import load_config
from helloworld.greet.greeting import Greeter

# import dependencies from another project in the monorepo
from commons.string_utils import string_concat


def say_hello() -> None:
    config = load_config()
    greeter = Greeter(
        languages=list(config.languages), greetings=list(config.greetings)
    )
    sentence = greeter.greet("world")
    print(green(string_concat(sentence, ', nice to meet you')))


if __name__ == "__main__":
    say_hello()
