# Introduction to Version Control with Github

## Create your own project:
    mkdir theproj
    cd theproj 
    git init

## Create a data file

    nano data.txt

In this file, make sure you are aware of "end line" characters.

## Create a program

    import sys

    x = []
    for line in open(sys.argv[1]):
       num = int(line)
       x.append(num)

    print 'average is', sum(x) / float(len(x))

### Now, let’s see what git knows about them:

    git status

### nothing! ok... let’s tell git about ‘em.

    git add calc.py data.txt

This converts them into tracked files, files that git knows and cares about.

Now we need to tell git that we are done making changes to these files, for now.

    git commit -am "script and data for calculating averages"

This stores those files with the note that they are part of a bundle of changes to the repository, aka a commit, for calculating averages. This may seem silly right now – you just created those files, of course you know what they are! – but just wait.

OK, now let’s change the ‘calc.py’ script to output the sum of the squares of the differences, too; make it look like this:

    import sys    

    x = []
    for line in open(sys.argv[1]):
    	num = int(line)
   	x.append(num)

    avg = sum(x) / float(len(x))

    diffs = []
    for num in x:
    	diff = num - avg
   	diffs.append(diff**2)

    print 'average is', sum(x) / float(len(x))
    print 'sumsqdiffs is', sum(diffs)

(Just pass in everything after the first ‘for’ loop.)

Now, do a ‘git status’. You’ll see that ‘calc.py’ is changed, but not ‘data.txt’. This is the first reason to like and use version control: it will tell you what’s been changed. To find out exactly what changed, type

    git diff calc.py

This will output a strange looking format known as a ‘diff’. The main thing to look for here is the ‘-‘ (which will be in front of the old lines) and the ‘+’ (which will be in front of new or changed lines). The — and +++ are for context, and the ‘@@’ tells you what line numbers have been changed.

Assuming you’re happy with these changes, do:

    git commit -am "updated calc.py to display sum sq diffs, too"

Let’s take a retrospective look at what we’ve done to the repository. Try typing ‘git log’. You will see a list of commits, along with the commit messages, tracing back what you’ve done in the past. You can compare current with past, e.g.

    git diff <old commit # prefix>

or any two past commits

    git diff <commit prefix 1>..<commit prefix 2>

and git will tell you exactly what lines have changed between those commits.

Note that you can use shorthand here: if you use the commit id ‘HEAD^’, it refers to last-commit-but-one, and ‘HEAD^^’ to last-commit-but-two’, etc. (‘git diff HEAD’ is the same as ‘git diff’ – it compares to the ‘head’ of the version control history, or the latest commit.)

—

Digression: three important terms: working copy, staged copy, and repository copy. The working copy is the edited/changed-but-not-added; the staged copy is the added-but-not-committed; and the repository copy is all the committed stuff. By using ‘commit -a’ you’re skipping the ‘add each file explicitly’ step, which I generally do.

—

Suppose you’re unhappy with the latest commit or commit message – how can you move back to an old version? This is actually fairly complicated and rich with many different possibilities, but the main thing you’ll probably end up needing to do is roll back to the latest commit – to do that, do

    git reset HEAD^

which “uncommits” the last commit, but leaves the changes in your current directory; try ‘git log’, ‘git diff’, and ‘git status’. You can now do one of two things: fix the commit (by editing, and then committing again), OR you can trash the whole commit, by doing

    git checkout -f

which says “hey, I don’t want any of these changes – trash ‘em all”. Needless to say this is a bit extreme, but it’s the most straightforward way to clean up your working copy and make it look like the latest commit. (You can do this at any time if you want to throw away all your changes; you don’t have to do a reset first.)

A third option – if you want to try something different out, without throwing away the last commit – is to make a branch. But that is a bit too complicated for right now; we’ll look at that option later.

So this is the second reason why version control is cool: it lets you keep track of each individual set of changes, from day zero. Greg refers to this as provenance of the source code, and it is important for two reasons:

First, it’s important scientifically because it allow you trace the set of changes to analysis code or modeling code in the context of a timeline. You can ask yourself, why did my model results change between last week and this week? and track down exactly where the change occurs in the source code.

Second, and far more pragmatically, if you find that you broke something subtle, it gives you a way to track down exactly what lines of code were modified. These sound like the same things, but I use these things more for tracking down bugs that I recently introduced than anything else...

Exercise Add “print ‘hello, world’” to the bottom of your calc.py script, make sure it runs, and then commit the changes to your repository. For extra credit, then use ‘git reset HEAD^’ to uncommit, and recommit with a different commit message.

## Working on multiple versions of your code
