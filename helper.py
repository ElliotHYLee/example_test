from IPython.display import YouTubeVideo, VimeoVideo
import ipywidgets as widgets
import numpy as np
import json
ans = {}

def answer1(value):
    ans["q1"] = value
    
def answer2(value):
    ans["q2"] = value
    
def answer3(value):
    ans["q3"] = value
    
def answer4(value):
    ans["q4"] = value

def email(email):
    ans["email"] = email

    
def showResult(ans):
    # serialized = json.dumps(ans, indent=4)
    print("Question 1: ", end="")
    print("Correct") if (ans["q1"](1, 2) == 3) else  print("Incorrect")
    print("Question 2: ", end="")
    print("Correct") if (ans["q2"](0, 10) == 55) else  print("Incorrect")
    print("Question 3: ", end="")
    print("Correct") if (ans["q3"](2, 10) == 10) else  print("Incorrect")

        