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

|                 | Monday  | Wednesday | Friday  |
|-----------------|---------|-----------|---------|
| Driver          | Mushfiq | MJ        | Mushfiq |
| Navigator       | MJ      | Mushfiq   | MJ      |
| Quality Control | Beni    | Beni      | Beni    |

___

## SECTION 1

1.a. Discuss with your partner two or more ways in which you've improved as a coder since T01. You can refer back to 
     **t01_final_story.py** for "inspiration".

```
    Since T01, we’ve improved in several concrete ways: Instead of letting code run at import time, 
    we now keep logic inside functions (plus a main() entry point) so the file doesn’t execute unintended 
    prompts when imported. We track player state (e.g., is_dead) in a single place and update it intentionally. We 
    validate and normalize inputs (strip/lower, numeric range checks), which makes the program more robust and user-friendly.

```

1.b. Briefly describe any logic changes you made in your code, and why you made them.

```
    Added a second “bad choice” check after a safe path: Even if you pick North (safe), there’s an optional risk 
    (explore the forest). This makes the narrative more interesting and matches the TODO note.  We ask for the player’s 
    name first, then direction, to keep it natural.

```

1.c. Did you find it challenging following the logic of another group’s code? Why or why not?

```
    Yes. Variables like isDead vs is_dead and uneven indentation obscured intent.
    Code that ran immediately on import mixed with function code made the flow hard to follow.
```

1.d. Briefly describe two or more of the PEP8 warnings you fixed. Does the resulting code look better or worse? Why?

```
    Moved `from time import sleep` to the top and fixed blank-line spacing between top-level defs.
    Replaced `isDead == False` with `is_dead = False` (assignment) and used boolean checks like `if is_dead:` 
    instead of `== True`. Consistent spacing, names, and layout make the code easier to read, maintain, and 
    debug—especially when multiple teams share the same file.
```

___

## SECTION 2

2.a. You should notice that there are multiple branches in the Github repository. 
     Find yours and check that your code is there. Compare your branch to main. What’s different?

```        
    Found our branch. Differences vs main: added Answers/t04_<group>_questions.md and fixes in t04_refactored.py 
    (bug fixes, extra check, PEP8). Main won't have these until PR merge.

```

2.b. Do you see other groups’ branches in the repo as well? Is your code in their branch? Why or why not?

```        
   Yes, other groups’ branches are visible. Our code is not in theirs because each branch is isolated.

```

2.c. Next, issue a pull request (this is done by clicking on "New Pull Request" button in the browser on Github). 
     A pull request is a formal request to add your code into the main branch, for all to see and share. 
     Once you’ve issued the pull request, communicate to the instructor that you are "ready for a PR review."
     After the instructor or TA approves your request, refresh Github. Is your code in the main branch now? 

```
    Created a PR and asked for review. After approval/merge, the changes should appeared in main (not confirmed yet).

```

2.d. What about other groups’ code? Is it also in main branch, compared to the last time you looked at it 
     in Question 2.b.?

```
    Some other groups’ changes are now in main; others aren’t yet if their PRs are still pending.

```

2.e. Once your code has been pulled into the main branch, go back to PyCharm. Right-click on the directory, and 
     switch back to the main branch by clicking `Git` >> `Branches` and selecting `Local Branches` >> `main`.
     Is your code in your **local** main branch? Why not?

```
    Local main didn’t update automatically. After switching to main and running `git pull origin main`, the merged changes should appeare locally.

```

2.f. Define Each Term:
```
        a. Clone:       Copy a remote repo to our computer

        b. Commit:      Save a snapshot of staged changes

        c. Push:        Send local commits to the remote

        d. Branch:      A separate file for development

        e. Pull:        Fetch + integrate remote changes

        f. Pull Request: Ask to merge our branch into another

        g. Merge:       Combine histories of two branches.

        h. Remote:      The hosted repo reference (e.g., origin).

        i. Local:       Our on-computer copy/branches.

        j. Fetch:      Get remote updates without integrating them.

    Check your definitions against the [git glossary](https://help.github.com/articles/github-glossary/) 
    to ensure they are correct.
```

2.g. In Github, go to the [Network Graph](https://github.com/Berea-College-CSC-226/t04-main/network) (i.e., a history 
     of branching and committing history). Discuss with your partner what confusions you still have about the git 
     workflow you experienced today, using the network graph to explore what has happened. Write your unanswered 
     questions in the space to the right:

```

• When to rebase vs. merge?
• Best way to handle merge conflicts?
• How to avoid extra commits by branching from an outdated main?
```

---