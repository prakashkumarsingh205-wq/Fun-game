print("Let's have some fun today")

while True:
    letter = input(
        "Type a letter (A, B, C, Q, S, H, D, Z, J) or EXIT: ").upper()

    if letter == "A":
        print("""
    /\\
   /  \\
  /____\\
  |    |
  |____|
  """)

    elif letter == "B":
        print("""
    |‾‾\\
    |___)
    |‾‾\\
    |___)
    """)

    elif letter == "C":
        print("""
     /‾‾‾\\
    |
    |
     \\___/
    """)

    elif letter == "Q":
        print("""
      _____
     /     \\
    |       |
    |       |
     \\_____/
     """)

    elif letter == "S":
        print("""
      ______
     | ^_^  |
     |      |
     | \\_/ |
      ----
    """)

    elif letter == "H":
        print("""
                   🌞
        /\\
       / Ō \\
      /_____\\
      |      |
      |  ___ |
      | |___||
        )   )
       (   (
        )   )
    """)
    elif letter == "D":
        print("""
            _____
       ____/     \\_____
      |___🛞 ________🛞 _|⁚
     """)
    elif letter == "Z":
        print("""
        ______
   ____/|_||_\\`.__
  (   _    _ _\\
  =`-(_)--(_)-'
    """)

    elif letter == "J":
        print("""
                / \\
               / Ō \\
             ''      ''
             (  ⪸  ⪵  ) 
             /    ⩕   \\
             (    ⩌   )             
              (_______) 
                |    |     
           _____|    |_____              
         /|                |\\
        / |                | \\
       / /|________________|/ \\
              """)

    elif letter == "EXIT":
        print("Exiting...")
        print("Request accepted")
        break
    else:
        print("Invalid letter, Try again later")
