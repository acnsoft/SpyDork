import sys
from dork import bypassdork , wordpressdork , fileuplouddork , sqldork 

COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}

def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text






baner = """

[[red]]  _________              [[blue]]________                __    [[white]]
[[red]] /   _____/_____ ___.__. [[blue]]\______ \   ___________|  | __[[white]]
[[red]] \_____  \\____ <   |  |  [[blue]]|    |  \ /  _ \_  __ \  |/ /[[white]]
[[red]] /        \  |_> >___  |  [[blue]]|    `   (  <_> )  | \/    < [[white]]
[[red]]/_______  /   __// ____| [[blue]]/_______  /\____/|__|  |__|_ \[[white]]
[[red]]        \/|__|   \/              [[blue]]\/                  \/[[white]]


        [1] Generate Sql Dorks                  [2] Generate Wordpress Dorks

        [3] Generate File Uploud Dork           [4] Generate ByPass Dorks

"""
banner = colorText(baner)

print(banner)

x = input(">>> ")

if x == '1':
   while True:
      try:
         url = input("\033[96mEnter a country's domain extension:\033[0m ")
         if not url:
            raise ValueError 

         f = open("Latest Dorks.txt", "w+", encoding='utf8')
         countrydomain = sqldork.replace("countrydomain", "site:" + url)
         f.write(countrydomain)

         print("Dorks saved to \"Latest Dorks.txt\"")
         done = input("Press \"Enter\" to exit")
         sys.exit()

      except ValueError:
            print("\033[91mError: Please enter a valid domain extension!")

if x == '2':
   while True:
      try:
         url = input("\033[96mEnter a country's domain extension:\033[0m ")
         if not url:
            raise ValueError # raises an error if the input is left empty

         f = open("Latest Dorks.txt", "w+", encoding='utf8')
         countrydomain = wordpressdork.replace("countrydomain", "site:" + url)
         f.write(countrydomain)

         print("Dorks saved to \"Latest Dorks.txt\"")
         done = input("Press \"Enter\" to exit")
         sys.exit()

      except ValueError:
            print("\033[91mError: Please enter a valid domain extension!")

if x == '3':
   while True:
      try:
         url = input("\033[96mEnter a country's domain extension:\033[0m ")
         if not url:
            raise ValueError

         f = open("Latest Dorks.txt", "w+", encoding='utf8')
         countrydomain = fileuplouddork.replace("countrydomain", "site:" + url)
         f.write(countrydomain)

         print("Dorks saved to \"Latest Dorks.txt\"")
         done = input("Press \"Enter\" to exit")
         sys.exit()

      except ValueError:
            print("\033[91mError: Please enter a valid domain extension!") 


if x == '4':
   while True:
      try:
         url = input("\033[96mEnter a country's domain extension:\033[0m ")
         if not url:
            raise ValueError

         f = open("Latest Dorks.txt", "w+", encoding='utf8')
         countrydomain = bypassdork.replace("countrydomain", "site:" + url)
         f.write(countrydomain)

         print("Dorks saved to \"Latest Dorks.txt\"")
         done = input("Press \"Enter\" to exit")
         sys.exit()

      except ValueError:
            print("\033[91mError: Please enter a valid domain extension!")
