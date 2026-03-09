# Adventure To Gitland

## Instructions

1. Copy this file.
2. Paste the copy of the file into the `Answers` directory.
3. Name the file `t04_usernames.md`, replacing usernames with your Berea usernames.
4. Replace each `**Replace This With Your Answer**` with your answer to the question above it.

Discuss with your team and assign yourselves roles. Try to pick the role you’ve had the least experience in.
Change roles each day!

```
    Complete the table below at the start of each class period:
```

|                 | Monday    | Wednesday | Friday |
|-----------------|-----------|-----------|--------|
| Driver          | Mekiyan M | Mekiyan   |        |
| Navigator       | Habiba S  | Habiba    |        |
| Quality Control |           |           |        |

___

## SECTION 1

1.a. Discuss with your partner two or more ways in which you've improved as a coder since T01. You can refer back to 
     **t01_final_story.py** for "inspiration".

```
    Mekiyan: understanding the specifics of code more.
    Habiba: new applications using code and getting introduced to logic with turtles.
```

1.b. Briefly describe any logic changes you made in your code, and why you made them.

```
     Added a while loop to check for input, if it is incorrect it reruns till the user adds the desired input and if the desired input is admissable it breaks out of the while loop and goes to the steps after.
     Added an elif statement for the third condition and left the else for a the rerun to get the correct input.
     Added the variable dead to every if statament that returns a boolean value ehich dictates whether the user is dead or not and then returned it at the end of the function.
```

1.c. Did you find it challenging following the logic of another group’s code? Why or why not?

```
    The logic of the group made sense and we were able to trace down the different logic they tried to make.
```

1.d. Briefly describe two or more of the PEP8 warnings you fixed. Does the resulting code look better or worse? Why?

```
    Extra brackets in the `if(drink == "red"):` to `if drink == "red":`condition of choice because it was not needed.
    Changed `if dead == True` to`if not is_alive:` because the definition could be simplified. 
```

___

## SECTION 2

2.a. You should notice that there are multiple branches in the Github repository. 
     Find yours and check that your code is there. Compare your branch to main. What’s different?

```        
    Main doesn't have all of our code and files because we haven't merged them into main yet
```

2.b. Do you see other groups’ branches in the repo as well? Is your code in their branch? Why or why not?

```        
   Yes, and no their code is in our branch because this is our work only, not the main file where it is going to have all of our code in it. This is my partner and I's version of the code.
```

2.c. Next, issue a pull request (this is done by clicking on "New Pull Request" button in the browser on Github). 
     A pull request is a formal request to add your code into the main branch, for all to see and share. 
     Once you’ve issued the pull request, communicate to the instructor that you are "ready for a PR review."
     After the instructor or TA approves your request, refresh Github. Is your code in the main branch now? 

```
    Yes it is after it was approved 
```

2.d. What about other groups’ code? Is it also in main branch, compared to the last time you looked at it 
     in Question 2.b.?

```
    Yes if their pr request got accepted
```

2.e. Once your code has been pulled into the main branch, go back to PyCharm. Right-click on the directory, and 
     switch back to the main branch by clicking `Git` >> `Branches` and selecting `Local Branches` >> `main`.
     Is your code in your **local** main branch? Why not?

```
Yes because the local is our system so yes it is in our system
```

2.f. Define Each Term:
```
        a. Clone:       Copying over the repo to have your own version of it on your local machine

        b. Commit:      Saving your code 

        c. Push:        Sending it to the remote (GitHub) to save just incase your code messes up on your IDE

        d. Branch:      Own copy of the code before adding it into the final product (main)

        e. Pull:        Updating project to match the main and the remote and local

        f. Pull Request: Sending a request to be put into the main branch (final product)

        g. Merge:       Combining versions of the code to make a final product

        h. Remote:      repo or banch hosted on a server

        i. Local:       Your personal machine

        j. Fetch:       Adding changes from remote without commiting

    Check your definitions against the [git glossary](https://help.github.com/articles/github-glossary/) 
    to ensure they are correct.
```

2.g. In Github, go to the [Network Graph](https://github.com/Berea-College-CSC-226/t04-main/network) (i.e., a history 
     of branching and committing history). Discuss with your partner what confusions you still have about the git 
     workflow you experienced today, using the network graph to explore what has happened. Write your unanswered 
     questions in the space to the right:

```
 How will merging two branches look like? 
```

---