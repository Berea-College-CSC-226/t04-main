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

|                 | Monday | Wednesday | Friday |
|-----------------|--------|-----------|--------|
| Driver          | Pier   | Yoseph    | Yoseph |
| Navigator       | Yoseph | Pier      | Pier   |
| Quality Control | Pier   | Yoseph    | Yoseph |

___

## SECTION 1

1.a. Discuss with your partner two or more ways in which you've improved as a coder since T01. You can refer back to 
     **t01_final_story.py** for "inspiration".

```
I fixed long lines (>79) and added spaces after commas. I also switched mixedCase to snake_case. 
The code reads cleaner and is easier to review.
```

1.b. Briefly describe any logic changes you made in your code, and why you made them.

```
I simplified nested if/else and added early returns/checks for “dead”. 
This made the story flow clear and avoided unreachable code.

```

1.c. Did you find it challenging following the logic of another group’s code? Why or why not?

```
A little. Variable names weren’t clear and some flags weren’t initialized. Comments helped once I added them.
```

1.d. Briefly describe two or more of the PEP8 warnings you fixed. Does the resulting code look better or worse? Why?

```
- Fixed missing blank lines between top-level functions.
- Added a single space after commas and around operators.
- Kept lines ≤79 chars.
Looks better because the structure and spacing guide your eye.

```

___

## SECTION 2

2.a. You should notice that there are multiple branches in the Github repository. 
     Find yours and check that your code is there. Compare your branch to main. What’s different?

```        
My branch has the refactored chapter (input checks + early death check). Main still had the older version until the PR.

```

2.b. Do you see other groups’ branches in the repo as well? Is your code in their branch? Why or why not?

```        
Yes, I see other branches. My code isn’t in theirs because each team works on its own branch.

```

2.c. Next, issue a pull request (this is done by clicking on "New Pull Request" button in the browser on Github). 
     A pull request is a formal request to add your code into the main branch, for all to see and share. 
     Once you’ve issued the pull request, communicate to the instructor that you are "ready for a PR review."
     After the instructor or TA approves your request, refresh Github. Is your code in the main branch now? 

```
Yes. After the PR was approved and merged, my chapter appears in main.
```

2.d. What about other groups’ code? Is it also in main branch, compared to the last time you looked at it 
     in Question 2.b.?

```
Some are merged; others are still pending review. The network graph shows which ones landed.
```

2.e. Once your code has been pulled into the main branch, go back to PyCharm. Right-click on the directory, and 
     switch back to the main branch by clicking `Git` >> `Branches` and selecting `Local Branches` >> `main`.
     Is your code in your **local** main branch? Why not?

```
Not until I update. I need to pull/fetch on my machine so my local main gets the new commits.
```

2.f. Define Each Term:
```
        a. Clone:       Make a local copy of a remote repo.

        b. Commit:      Save a snapshot of changes with a message.

        c. Push:       Send local commits to the remote repo.

        d. Branch:      A separate line of work/history.

        e. Pull:        Get changes from remote and update local.

        f. Pull Request: Ask to merge your branch into another (e.g., main).

        g. Merge:       Combine changes from one branch into another.
        
        h. Remote:       The server-side repo (e.g., GitHub).

        i. Local:       Your copy on your computer.
        
        j. Fetch:       ownload remote commits without merging yet.

    Check your definitions against the [git glossary](https://help.github.com/articles/github-glossary/) 
    to ensure they are correct.
```

2.g. In Github, go to the [Network Graph](https://github.com/Berea-College-CSC-226/t04-main/network) (i.e., a history 
     of branching and committing history). Discuss with your partner what confusions you still have about the git 
     workflow you experienced today, using the network graph to explore what has happened. Write your unanswered 
     questions in the space to the right:

```
I see the different branches and merges in the network graph, but I still get confused about the best time to make a new branch versus just committing on main. 
I also wonder when to use fetch vs. pull, since both bring updates down. 
Finally, I’m not sure what happens if two groups push changes to main at almost the same time—how does GitHub handle that?


```

---