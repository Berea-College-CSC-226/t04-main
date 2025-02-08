# Adventure To Gitland

## Instructions

1. Copy this file. [X]
2. Paste the copy of the file into the `Answers` directory. [X]
3. Name the file `t04_usernames.md`, replacing usernames with your Berea usernames. [X]
4. Replace each `**Replace This With Your Answer**` with your answer to the question 
above it. [X]

Discuss with your team and assign yourselves roles. 
Try to pick the role you’ve had the least experience in.
Change roles each day!

```
    Complete the table below at the start of each class period:
```

|                 | Monday | Wednesday | Friday |
|-----------------|--------|-----------|--------|
| Driver          |        | A         | A      |
| Navigator       |        | A         | A      |
| Quality Control |        | A         | A      |

___

## SECTION 1

1.a. 
Discuss with your partner two or more ways in which 
you've improved as a coder since T01. You can refer back to 
**t01_final_story.py** for "inspiration".





```
One way I've grown as a coder since T01 is solidificaiton of my understanding of
flows of execution, this was highlighted by the use of user defined functions, 
in combination with the use of a main() function.

A secondary way I've grown as a coder, is in my understanding of input parameters,
and the return of arguments. Arguments can be passed as outputs from one function into 
another? I've added the following two definitions to my main document.

DEFINED:
	Arguments – Functions, require arguments, and return values. 
	There are values that controls how a function does it job, these are local scope variable. 
	Input Parameters – Functions require parameters, a value that controls how the function does it job,  global scopes.  
    There are values the control havea function does it job, if they are in the global scope they are ____.
 

```

1.b. Briefly describe any logic changes you made in your code, and why you made them.

```
    I am reviewing the code inside of t04_refactor.py lines 320-362.
    The biggest logical changes are trying to nest the calls inside of
    user defined functions: inputRequests and outputResponses.
```

1.c. Did you find it challenging following the logic of another group’s code? 
     Why or why not?

```
     In order to understand the logic of the other groups, I am 
     reviewing and comparing the code for groups: [30,1,10,20]
 

      
```

1.d. Briefly describe two or more of the PEP8 warnings you fixed. Does the resulting code look better or worse? Why?

```
    I pulled over the following code from t01_final_story_do_not_edit.py into t04_refactored.py
    As I looked for grey squiggly lines that would indicated PEP8 warning, I only
    saw 1, that stated there was a, "duplicate code fragment".
                          print(f'Welcome {name}  to the game: Choose you own Adventure') 

    This doesn't seem accurate to me, since the error message indicated that
    the problem was with the line: 
                         name = input("What is your name? ")
    However, this particular line is required in order to get that information
    and call it into the next line.
    
    As I looked closer at the line, I actually found that the duplicate code fragment was
    only in my refactored code? 
    
    If I understand correctly, one way to resolve this is to, refactor the source code, 
    and then call it elsewhere using:
    
    from t04_refactored import team_30_adv
    team_30_adv()
    
    The only other PEP8 suggestion I found was in Team 29s code, which stated it could be 
    simplified from:
     
     if dead == True: print("You have died, please try again")
     
     to
     if dead: print("You have died, please try again").

  
   
```


___

## SECTION 2

2.a. You should notice that there are multiple branches in the Github repository. 
     Find yours and check that your code is there. Compare your branch to main. What’s different?

```        
    I've found my branch
    https://github.com/Berea-College-CSC-226/t04-main/tree/t04-konrumpf-main
    
    The primary difference I see is in the content of the t04_refactor.py file.
    This is likely because I have not committed my changes yet.
    
```

2.b. Do you see other groups’ branches in the repo as well? Is your code in their branch? Why or why not?

```        
    Yes, I am able to see branches for:
    https://github.com/Berea-College-CSC-226/t04-main/blob/t04_chikomod_johnsont7/Answers/t04_chikomod_johnsont7.md
    and
    https://github.com/Berea-College-CSC-226/t04-main/blob/rheaj_mccaslinm/Answers/t04_rheaj_mccaslinm_questions.md

I do not see their code, because I am not sure what their team number is. It's likely somewhere in
refactored.py - but I can't determine what they were responsible for. 

```

2.c. Next, issue a pull request (this is done by clicking on "New Pull Request" button in the browser on Github). 
     A pull request is a formal request to add your code into the main branch, for all to see and share. 
     Once you’ve issued the pull request, communicate to the instructor that you are "ready for a PR review."
     After the instructor or TA approves your request, refresh Github. Is your code in the main branch now? 

```
    I submitted my PR on 2/8, and since it's not be approved, I don't see it inside of
    main > t04_refactored.py
```

2.d. What about other groups’ code? Is it also in main branch, compared to the last time you looked at it 
     in Question 2.b.?

```
    Yes, I see modification for Team 5, Team 2.
```

2.e. Once your code has been pulled into the main branch, go back to PyCharm. Right-click on the directory, and 
     switch back to the main branch by clicking `Git` >> `Branches` and selecting `Local Branches` >> `main`.
     Is your code in your **local** main branch? Why not?

```
    Unable to do this since the pulled request has not be accepted. 
```

2.f. Define Each Term:
```
       a. Clone:       Copy of repo

        b. Commit:      Saving the code/files

        c. Push:        Sending the saves or commits to Github

        d. Branch:      A copy of the files that you can work on without disrupting the main

        e. Pull:        Merging files from the main onto your branch so that it stays up to date

        f. Pull Request: A request to have your code added to the main file

        g. Merge:       Combining two different files of code

        h. Remote:      On Github

        i. Local:       On computer

        j. Fetch:       gives you a list of options

    Check your definitions against the [git glossary](https://help.github.com/articles/github-glossary/) 
    to ensure they are correct.
```

2.g. In Github, go to the [Network Graph](https://github.com/Berea-College-CSC-226/t04-main/network) (i.e., a history 
     of branching and committing history). Discuss with your partner what confusions you still have about the git 
     workflow you experienced today, using the network graph to explore what has happened. Write your unanswered 
     questions in the space to the right:

```
    ![](C:\Users\OPEF-CLUE-0\Downloads\d.png) #Attempting to insert an image of what
    I think is being called the "network graph". Though, I am unsure if this path will
    be remotely accessible. Testing.... comitted file, login to GitHub, click link...
    
    
     
```

---