'''I will create a list of jokes with punchlines which will be shown randomly.
2025-05-13 EJS'''

import random

jokes = [("Why was Cinderella so bad at soccer?", 
          "She kept running away from the ball!"),
            ("What do you call a well-balanced horse?",
           "Stable."),
            ("What do you call an angry carrot?",
            "A steamed vegetable!"),
            ("Where do polar bears keep their money?",
             "In a snow bank!"),
            ("What did the triangle say to the circle?",
             "You're pointless."),
            ("What do lawyers wear to court?",
             "Lawsuits."),
            ("What did one toilet say to another?",
             "You look flushed."),
            ("What lights up a soccer stadium?",
             "A soccer match."),
            ("What does corn say when it gets a compliment?",
             "Aw, shucks!"),
            ("Why do cows wear bells?",
             "Because their horns don't work.")
          ]

choice = int(random.random()*10)
print(jokes[choice][0])
print("....\n"+jokes[choice][1])
