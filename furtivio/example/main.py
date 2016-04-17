# Copyright 2015 Furtivio LLC
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from furtivio.example.helloworld import HelloWorld


def main():
    hw = HelloWorld()
    print(hw.hello())


if __name__ == "__main__":
    main()
