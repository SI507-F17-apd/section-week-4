# Section Week 4

> Announcements: If you haven't been able to push to git for your assignment, please tell us

## Activity 1: Graduate Student from Class Week 4

https://paper.dropbox.com/doc/SI-507-Lecture-4-September-27-2017-Class-inheritance-object-design-YVvaJSXwJNoO80yrSc9sM#:uid=048188662355237654871073&h2=Exercise

## Activity 2: Git Pull, Git Fetch and Merge

Before we proceed, let us change the default text editor if you are not comfortable using VIM, the command line text editor that you see when you forget to add the `-m` in `git commit`.

**Follow the instructions here:**  
https://help.github.com/articles/associating-text-editors-with-git/

Next,
**do the following in pairs**
- Both should fork and clone this repository: https://github.com/SI507-F17-apd/section-week-4-merging  
Since we are learning how to pull and merge, there is no need to create virtual environment in this case.  

- In `SI507F17_project1_cards.py`
    - **Person 1** should change the `__str__` method of `Card` to:  
        `return "{} of {}".format(self.rank, self.suit)`  

    - **Person 2** should fix the bug in `Deck` class's `deal_hand` removing the `i` in line 65 to:  
    `hand_cards.append(self.pop_card())`

    - **Both** should commit their changes and push to their own forked repositories (or you can call them **forks** for short)
    - **Person 1** should now send a Pull Request on Github to Person 2
        - Select Base Fork as the fork of Person 2
    - Compare **both** of your Github commit history
    - **Person 2** now should go to their own fork, open the pull request on the Github Interface, and click on Merge
    - Compare **both** of your Github commit history
    - **Person 1** should now use the command line to sync their repository to that of Person 2s. (Usually `origin` is your own repository on github, and `upstream` is the base repository that you are contributing to.)
        - `git remote add upstream <PERSON2_GIT_REPO_URL>`
        - `git pull upstream master` -- get the updates from Person 2
        - Resolve merge conflicts if any
        - `git push origin master` -- push to your fork
    - Compare **both** of your Github commit history. It should ideally be the same.


- Next let us induce a merge conflict. *(If you are not present in one of the sections, and are finding this difficult, please come to office hours).* In `SI507F17_project1_cards.py`
    - **Person 1** should change the `__str__` of Deck to:  
      `return "{0} of {1}".format(self.rank,self.suit)`  

    - **Person 2** should change the `__str__` of Deck to:  
      `return "{rank} of {suit}".format({"rank": self.rank, "suit": self.suit })`

    - Now, **Person 2** should send a pull request to **Person 1**
    - **Person 1** should now be able to see the pull request on their Github fork, but it cannot be merged from the online interface like before. **Person 1** would need to manually merge the changes from their command line. Github provides you command line instructions to do this using branches, but for now, we will just **close** the pull request and manually merge it in **Person 1's** local.
    - **Person 1** should do `git pull upstream master`
        - This will lead to a merge conflict
        - Resolve this merge conflict (Github's documentation for those who were not there in section: https://help.github.com/articles/resolving-a-merge-conflict-on-github/)
        - Check `git status`
        - `git add` the files that you just modified
        - `git commit` **without** `-m`. I repeat, it is just `git commit`
        - `git push origin master`
    - Compare **both** of your Github commit history. Person 1 will have the additional merge commit. Person 2 can setup Person 1's fork as `upstream` and sync their own local and Github to same as Person 1's.




> You can practice both these steps by creating multiple accounts for yourself, forking the main repository and following the steps for both Person 1 and 2    

---

## Activity 3: Inheritance and super()

How would you model Facebook interface and data to Python classes?

What are some of the elements you see in the Facebook interface?

- Feed is a list of posts
- Post
    - Comment is a type of post, but each post has multiple comments
    - Reply is a type of post, but each comment has a list of replies
    - Photo is also a type of post, but has a different display, and its own set of methods
    - Video
    - ...
- Profile
    - User has what you see on your own profile page
    - Page has some properties of a user, but is aimed to be public
    - Group is like a page, but has a list of users
    - Event
    - ...

Each of these elements displays some content, so it must be saved somewhere.

What are some of the actions that you can do on these elements? These would be the methods of these classes

In sum, each Class has its own variables and methods to fetch data, manipulate these variables, and save it back into Facebook's database

Let us write this hierarchy of Classes in Python! Initialize some variables and write some dummy methods. This would help you learn how to think about Classes and Inheritance. *Do this activity in pairs.*
