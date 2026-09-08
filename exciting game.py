print("Let's have some fun today")

prompt = "Type a letter (A, B, C, O, S, H, D, Z, J, E, F, G, Q, I, K, L) or EXIT: "
while True:
    letter = input(prompt).upper()

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

    elif letter == "O":
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
    elif letter == "E":
        print("""
                /
               / 
              /______ 
                    / 
                   /   
                  /     
                    """)
    elif letter == "F":
        print("""
                _____
             __/_____\\___
           ◜             \\___     /
       ↙ ◜                    \\__/  
      <-(                  ____/  \\
         ◟                /       \\
           ◟_____________/  
               \\_____/ 
              """)
    elif letter == "G":
        print("""
           __    
          |
          |   __ 
          |__|  |
             """)
    elif letter == "Q":
        print("""
      _____
     /     \\
    |       |
    |       |
     \\_____/
            \\  /
             \\/  
             """)
    elif letter == "I":
        print("""
      _____________           
         |     |
         |     |
         |     |
      ___|_____|___  
             """)
    elif letter == "K":
        print("""
           |  / 
           | / 
           |/  
           |\\  
           | \\ 
           |  \\   
             """)
    elif letter == "L":
        print("""
                  _↿__ 
               \ (    )/ 
               \(  💡  )/
                (______)
                  |___|       
             """)

    elif letter == "EXIT":
        print("Exiting...")
        print("Request accepted")
        break
    else:
        print("Invalid letter, Try again later")
