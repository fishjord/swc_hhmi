# Introduction to Version Control with Github

*Original material by C. Titus Brown*

Git in [visuals](http://marklodato.github.io/visual-git-guide/index-en.html).  You can see that it gets very complicated.

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

### Exercise Add “print ‘hello, world’” to the bottom of your calc.py script, make sure it runs, and then commit the changes to your repository. For extra credit, then use ‘git reset HEAD^’ to uncommit, and recommit with a different commit message.

## Working on multiple versions of your code

OK, suppose now that you want to have two versions of your code. One is the “safe” version of your code, and the other is the “daring edgy” version of your code. For example, suppose you’re adding some nifty new features but you don’t want to “break” your existing code, which you’re using to run analyses. What do you do?

The simplest (but not yet the easiest) thing to do is make a copy of your project. From within the ‘theproj’ directory, type:

    cd ..
    git clone theproj theproj_new

This makes a complete copy of the git repository and puts it into ‘theproj_new’. Let’s go there and do some wild and crazy edits.

    cd theproj_new

and edit calc.py to look like this:

    import sys
    import math

    x = []
    for line in open(sys.argv[1]):
    	num = int(line)
   	x.append(num)

    avg = sum(x) / float(len(x))

    diffs = []
    for num in x:
    	diff = num - avg
   	diffs.append(diff**2)

    stddev = math.sqrt(sum(diffs) / float(len(x)))

    print 'average is', sum(x) / float(len(x))
    print 'sumsqdiffs is', sum(diffs)
    print 'stddev is', stddev

What does the diff look like?

OK, verify that it runs and then commit it:

    git commit -am "added stddev"

Now let’s go back to the ‘safe’ repository, ‘theproj’, and edit calc.py to print the average sum sq diffs. Commit that, too:

    cd ../theproj
    git commit -am "changed to print avg sum sq diffs"

Now pretend that this has taken a month or two, and you’ve been working on both repositories. Now you decide that you want to compare, and maybe combine, the changes in the two repositories. What do you do?

Well, because these two repositories share history – until you made the changes above, they were the same repository – you can actually do this pretty easily.

Let’s start by comparing the two sets of changes. Make sure you’re in the ‘theproj’ repository, and type:

     git fetch ../theproj_new master:edgy

This will take all of the changes in the ‘theproj_new’ repository and bring them over to the ‘theproj’ repository, but as a separate bundle of changes, called a ‘branch’. Try typing ‘git branch’ and you should see two branches, one called ‘master’ and one called ‘edgy’.

So, let’s try comparing them; how do you do that? Any guesses?

    git diff edgy

OR:

    git diff master..edgy

do the same thing – they compare your current branch, ‘master’, to the ‘edgy’ branch.

You can actually switch branches pretty easily – do:
    
    git branch
    git checkout edgy

and you’ll see that the ‘*’ has moved over to ‘edgy’, to reflect that you are now on the edgy branch.

Switch back to the ‘master’ branch using ‘git checkout master’. Verify that you’re on the master branch using either ‘git status’ or ‘git branch’.

OK, let’s say you’re happy with both sets of changes. Awesome! Let’s merge them in. To do this, just type

    git merge edgy

Assuming you made only the changes we went through, this should just work, because git is smart enough to figure out that all the changes you made to both branches were syntactically orthogonal, or, to be simpler, didn’t interfere and could be merged automatically. Note that this doesn’t mean that the changes won’t interfere semantically – for example, if you changed the meaning of one of the variables, there’s no way for git to track that sort of thing. So you still need to worry about whether or not your code still works even after an automatic merge!

Note that you can now delete the ‘edgy’ branch:
    git branch -d edgy

because it’s been merged into your current branch. Generally it’s not a good idea to do this without a good reason – branches don’t take up much extra space. I generally wait until my project reaches a good resting point before cleaning up my repositories.

## Using github

First, sign up for an account and let's take a tour.  [Github website](https://github.com/)

Let’s start by going to https://github.com/ctb/theproj in a Web browser and clicking on ‘fork’ – make sure you’re logged into github.com first!

This will create a new copy of my ‘theproj’ repository under your account on github.

Now, on your laptop, go to the directory above your ‘theproj’ directory and make your own local copy of your github repository. First, grab the ‘http’ URL from your github repository; it should be under the ‘http’ tab just under the description of the project, and look something like this: ‘https://ctb@github.com/ctb/theproj.git‘

At the command line, type:

    cd ~/swc
    git clone https://<user>@github.com/<user>/theproj.git newproj

replacing the URL on the last line with YOUR github project URL.

Assuming everything worked, you’ll have a directory ‘newproj’ containing ‘calc.py’ and ‘data.txt’. This is essentially the same thing that you’ve been working on above, but now it’s a clone of my own repository that I developed when creating this tutorial.

It’s a full git repo – do ‘git log’, ‘git status’, etc. etc. after changing into the directory:

    cd newproj

OK, now, let’s make some changes!! Go in and change something in the script – put a comment at the top, or change a print statement to do something else, or whatever. Then make sure it works, and commit it:

    git commit -am "a random change"

Now you’ll want to push it to github. Ordinarily you should do everything in git with a ‘fetch’, in which you pull things into your repository; but in this case, you don’t actually have command line access to your repository! So you need to push. Type:

    git push origin master

and this will send the changes back to github under your fork of my repository. You should see them if you go back to the github.com Web page and look at ‘history’.

And voila! These changes are now publicly available to anyone who wants to fetch them into their own repository. You just need to fetch from THEIR github URL, which will be using THEIR github username.

Now, at this point, you have everything you need to work collaboratively.

----

Concluding thoughts
So, in conclusion, version control systems let you –

track changes (wanted and unwanted) in your files.

keep track of an entire history of changes.

track multiple independent “branches” of work.

collaborate sanely.

There are other reasons that I didn’t mention above, too. One reason that I almost always use version control is that it’s a backup against my own stupidity - if I delete a file, or I tweak it in some way that I can’t immediately figure out, I can always restore it, as long as I’ve got it in version control! Plus, if I’m using github, then it’s somewhere else, so even if my computer gets stolen or dies horribly, I can recover it.

So, you definitely want to use version control. Do you want to use git, in particular? That’s not so clear.

There are a lot of version control systems, and it’s not so important whether you use git or rather mercurial (hg) or subversion (which are the two other really commonly used ones at the moment). Just use version control.

That having been said, branching and merging with git is really, really easy, which is why I like it; and, in general, it’s a great tool that has relatively few drawbacks. The biggest positive is github, which is awesome; the biggest negative is the terse and rather unforgiving and complex command syntax.

We haven’t talked much about the difference between distributed version control systems (like git and hg) and centralized version control system like subversion. If you’ve used version control in the past, you’ve probably used something centralized; the disadvantage there is that you have to set up a server, and permissions, and cannot commit when you don’t have a connection to the server (like on an airplane). The advantage, however, is that there is never any ambiguity about collaboration order: you get a unique, monotonically increasing version number. Greg likes this; I don’t care that much.