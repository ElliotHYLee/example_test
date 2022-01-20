from IPython.display import YouTubeVideo, VimeoVideo
import ipywidgets as widgets
import numpy as np
import json
ans = {}

   
def showResult(ans):
    # serialized = json.dumps(ans, indent=4)
    print("Question 1: ", end="")
    print("Correct") if (ans["q1"](1, 2) == 3) else  print("Incorrect")
    print("Question 2: ", end="")
    print("Correct") if (ans["q2"](0, 10) == 55) else  print("Incorrect")
    print("Question 3: ", end="")
    print("Correct") if (ans["q3"](2, 10) == 10) else  print("Incorrect")

        