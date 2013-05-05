Working with Data in Python

============================



Goals

--------

* Using the csv module to read structured data

* Using lists, dictionaries, and sets to work with data

* Using for-loops to process data

* Writing functions

* Building complex functions based on simple ones

* Brief introduction to classes





Dataset

---------

We'll be working with data for the number of medals won at the olympic games since 2000.  The data is contained in datasets/olympic_medals.csv and is broken up by year and country.



Reading Data

--------------

We'll be using the 'csv' module to read data, it is one of the easier ways to read structured data from a variety of sources.  Despite the name the csv module can read structured data file with any delimiter (field seperates, ',' in the case of csv files) files as well.  Some common delimiters are tab, space, and occasionally |.



The readers in the csv package read one line at a time, the basic csv.reader returns a list where as the csv.DictReader returns a dictionary where the keys are the column headers.



###Different ways to load data

* From the directory we started ipython using `open("filename")`

  * We can see the current working directory by using `!pwd`

  * We can see the contents of our current directory by using the `!ls` (on windows use `dir`) command

  * In IPython we can use shell commands by prefixing them with an !

* Directly from a website with urllib2

* From somewhere else on the computer

  * we'd have to specify the path like `open("path/to/file")`

```python
import urllib2 #For reading from URLs

import csv     #For reading formatted data files



raw_medals_data = list()

#We're loaded the data straight from github instead of from a local file for simplicity

#We could also use open("day1.pythonadv/olympic_medals.csv") if you started ipython in the swc_hhmi directory

for line in csv.DictReader(urllib2.urlopen("https://raw.github.com/fishjord/swc_hhmi/master/day1.pythonadv/olympic_medals.csv")):

    raw_medals_data.append(line)
```
## Exploring the data



### Introduction

We've loaded the data in to a list, but what exactly does our data look like?



We can start by looking at the first record

```python
print raw_medals_data[0]
```

**Output**:

```
{'Silver Medals': '1', 'Country': 'Algeria', 'Gold Medals': '1', 'Bronze Medals': '3', 'Year': '2000'}

```

We've loaded the data in our file in to a list.  Each list item is a dictionary containing the 5 columns



* Olympic Year

* Country

* Gold Medals Won

* Silver Medals Won

* Bronze Medals Won



and our first record contains information on the number of medals Algeria won in the 2000 games. **NOTE** Python the first item in a python list is item *0* not 1.



Now what if we wanted to see the last record?

```python
print raw_medals_data[-1]
```

**Output**:

```
{'Silver Medals': '0', 'Country': 'Venezuela', 'Gold Medals': '1', 'Bronze Medals': '0', 'Year': '2012'}

```

In python, supplying a negative index is like asking for items starting from the end of the list.



###Excercises



* What year and country is the 3rd record for?

* The second to last?

* Challenge: How could we get the first 10?

* Challenge: Items 2, 4, 6 and 8?

```python
print raw_medals_data[2]

print raw_medals_data[-2]

print

print raw_medals_data[0:10]

print

print raw_medals_data[0:10:2]



print len(raw_medals_data[:])
```

**Output**:

```
{'Silver Medals': '0', 'Country': 'Armenia', 'Gold Medals': '0', 'Bronze Medals': '1', 'Year': '2000'}

{'Silver Medals': '0', 'Country': 'Uzbekistan', 'Gold Medals': '1', 'Bronze Medals': '3', 'Year': '2012'}



[{'Silver Medals': '1', 'Country': 'Algeria', 'Gold Medals': '1', 'Bronze Medals': '3', 'Year': '2000'}, {'Silver Medals': '17', 'Country': 'Argentina', 'Gold Medals': '0', 'Bronze Medals': '3', 'Year': '2000'}, {'Silver Medals': '0', 'Country': 'Armenia', 'Gold Medals': '0', 'Bronze Medals': '1', 'Year': '2000'}, {'Silver Medals': '69', 'Country': 'Australia', 'Gold Medals': '60', 'Bronze Medals': '54', 'Year': '2000'}, {'Silver Medals': '1', 'Country': 'Austria', 'Gold Medals': '3', 'Bronze Medals': '0', 'Year': '2000'}, {'Silver Medals': '0', 'Country': 'Azerbaijan', 'Gold Medals': '2', 'Bronze Medals': '1', 'Year': '2000'}, {'Silver Medals': '0', 'Country': 'Bahamas', 'Gold Medals': '6', 'Bronze Medals': '5', 'Year': '2000'}, {'Silver Medals': '0', 'Country': 'Barbados', 'Gold Medals': '0', 'Bronze Medals': '1', 'Year': '2000'}, {'Silver Medals': '8', 'Country': 'Belarus', 'Gold Medals': '3', 'Bronze Medals': '11', 'Year': '2000'}, {'Silver Medals': '3', 'Country': 'Belgium', 'Gold Medals': '0', 'Bronze Medals': '4', 'Year': '2000'}]



[{'Silver Medals': '1', 'Country': 'Algeria', 'Gold Medals': '1', 'Bronze Medals': '3', 'Year': '2000'}, {'Silver Medals': '0', 'Country': 'Armenia', 'Gold Medals': '0', 'Bronze Medals': '1', 'Year': '2000'}, {'Silver Medals': '1', 'Country': 'Austria', 'Gold Medals': '3', 'Bronze Medals': '0', 'Year': '2000'}, {'Silver Medals': '0', 'Country': 'Bahamas', 'Gold Medals': '6', 'Bronze Medals': '5', 'Year': '2000'}, {'Silver Medals': '8', 'Country': 'Belarus', 'Gold Medals': '3', 'Bronze Medals': '11', 'Year': '2000'}]

401

```

In python you can ask for array slices, or subsets of array using the [start:end] syntax.



**NOTE** the end index is exclusive, using arr[0:3] would give you a new list containing arr[0], arr[1], arr[2].  You can also omit the starting or ending index; if omitted 0 is the implied start index and the length of the array is the implied end index.

## Extracting Information







Suppose we wanted to know how many gold medals Australia won in the year 2000, how would we extract that information from the data we have?

```python
for data in raw_medals_data:

    if data["Country"] == "Australia" and data["Year"] == "2000":

        print "Australia won %s gold medals in the year 2000" % data["Gold Medals"]
```

**Output**:

```
Australia won 60 gold medals in the year 2000

```

A for loop in python goes through each item in a collection one at a time and executes the specified block of code



Syntax:
```python for var in collection:

    #...some code...

```


Where in each iteration `var` is the current item in `collection`.  In our example the first time through the loop `data` contains the first item in the list.




```python
print "The first three items in the dataset"

print raw_medals_data[0]

print raw_medals_data[1]

print raw_medals_data[2]



print

print "Items via for-loop"

for data in raw_medals_data[0:3]:

    print data
```

**Output**:

```
The first three items in the dataset

{'Silver Medals': '1', 'Country': 'Algeria', 'Gold Medals': '1', 'Bronze Medals': '3', 'Year': '2000'}

{'Silver Medals': '17', 'Country': 'Argentina', 'Gold Medals': '0', 'Bronze Medals': '3', 'Year': '2000'}

{'Silver Medals': '0', 'Country': 'Armenia', 'Gold Medals': '0', 'Bronze Medals': '1', 'Year': '2000'}



Items via for-loop

{'Silver Medals': '1', 'Country': 'Algeria', 'Gold Medals': '1', 'Bronze Medals': '3', 'Year': '2000'}

{'Silver Medals': '17', 'Country': 'Argentina', 'Gold Medals': '0', 'Bronze Medals': '3', 'Year': '2000'}

{'Silver Medals': '0', 'Country': 'Armenia', 'Gold Medals': '0', 'Bronze Medals': '1', 'Year': '2000'}

```

How would you modify  to print out the number of medals won by Australia in the year 2012?

```python
for data in raw_medals_data:

    if data["Country"] == "Australia" and data["Year"] == "2012":

        print "Australia won %s gold medals in the year 2012" % data["Gold Medals"]
```

**Output**:

```
Australia won 18 gold medals in the year 2012

```

This works, but we have to duplicate a lot of code to answer each question.  



A better solution would be to encasulate the logic in a function.  



A function is a named chunk of code that performs some task.  Good functions should perform a single task and have a descriptive name.  In Python function names are commonly all lower case with words seperated by underscores.

```python
def num_gold_medals(medals_data, country, year):

    for data in medals_data:

        if data["Country"] == country and data["Year"] == year:

            print "%s won %s gold medals in %s olympics" % (country, data["Gold Medals"], year)



num_gold_medals(raw_medals_data, "Australia", "2002")

num_gold_medals(raw_medals_data, "Australia", "2004")

num_gold_medals(raw_medals_data, "United States", "2004")
```

**Output**:

```
Australia won 2 gold medals in 2002 olympics

Australia won 49 gold medals in 2004 olympics

United States won 118 gold medals in 2004 olympics

```

Exercise: How could we use this function to write another that would output the number of silver medals won by a country?

```python
def num_silver_medals(medals_data, country, year):

    for data in medals_data:

        if data["Country"] == country and data["Year"] == year:

            print "%s won %s silver medals in %s olympics" % (country, data["Silver Medals"], year)



num_silver_medals(raw_medals_data, "Australia", "2000")

num_silver_medals(raw_medals_data, "Australia", "2004")

num_silver_medals(raw_medals_data, "United States", "2004")
```

**Output**:

```
Australia won 69 silver medals in 2000 olympics

Australia won 77 silver medals in 2004 olympics

United States won 75 silver medals in 2004 olympics

```

We could easily continue along these lines to make a function that found the number of bronze medals a country won in a given year, but wouldn't it be better be able to pass the type of medal we're interested as an argument?



Exercise: Using `num_silver_medals(...)` as a starting point, write a function that takes the type of medal as an argument




```python
def num_medals(medals_data, country, year, medal):

    for data in medals_data:

        if data["Country"] == country and data["Year"] == year:

            print "%s won %s %s in %s olympics" % (country, medal, data[medal], year)



num_medals(raw_medals_data, "Australia", "2002", "Bronze Medals")

num_medals(raw_medals_data, "Australia", "2004", "Bronze Medals")

num_medals(raw_medals_data, "United States", "2004", "Bronze Medals")
```

**Output**:

```
Australia won Bronze Medals 0 in 2002 olympics

Australia won Bronze Medals 30 in 2004 olympics

United States won Bronze Medals 72 in 2004 olympics

```

This is certainly more general purpose than the previous functions, but what if we don't want to just print out a message, what if we want to actually do something with the number of medals?



We can modified the function to return the number of medals instead of printing out a message.  This way the function caller can decide what to do with the value.

```python
def num_medals(medals_data, country, year, medal):

    for data in medals_data:

        if data["Country"] == country and data["Year"] == year:

            return int(data[medal])

        

    return 0  # Not every country participated in all the olympic games in the dataset



print "Germany won %d gold medals in 2012" % num_medals(raw_medals_data, "Germany", "2012", "Gold Medals")
```

**Output**:

```
Germany won 45 gold medals in 2012

```

Exercise: Using the `num_medals(...)` function, write a new function named `count_medals` that returns the total number of medals won by a country in a given year.

```python
def count_medals(medals_data, country, year):

    return num_medals(medals_data, country, year, "Gold Medals") + \

        num_medals(medals_data, country, year, "Silver Medals") + \

        num_medals(medals_data, country, year, "Bronze Medals")



print "Germany won %d medals total in 2012" % count_medals(raw_medals_data, "Germany", "2012")
```

**Output**:

```
Germany won 94 medals total in 2012

```

Another question we might wish to ask is "How many medals did a country win over all the years?"  If we wanted to build this on top of the `count_medals(...)` function we've already built we will need to know all the years in the dataset.

```python
years = []

for data in raw_medals_data:

    years.append(data["Year"])

    

print years
```

**Output**:

```
['2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2000', '2002', '2002', '2002', '2002', '2002', '2002', '2002', '2002', '2002', '2002', '2002', '2002', '2002', '2002', '2002', '2002', '2002', '2002', '2002', '2002', '2002', '2002', '2002', '2002', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2004', '2006', '2006', '2006', '2006', '2006', '2006', '2006', '2006', '2006', '2006', '2006', '2006', '2006', '2006', '2006', '2006', '2006', '2006', '2006', '2006', '2006', '2006', '2006', '2006', '2006', '2006', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2008', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012', '2012']

```

Whoops, this isn't quite what we wanted, if each year appears more than once we'll end up over-counting the number of medals!



We've got a few options.  First we could check to see if the list already contains the year we're about to add.

```python
years = []

for data in raw_medals_data:

    if data["Year"] not in years:

        years.append(data["Year"])

    

print years
```

**Output**:

```
['2000', '2002', '2004', '2006', '2008', '2010', '2012']

```

This isn't so bad if we are working with a small dataset with few unique values.  A better approach however would be to use a `set()`.  A set is an unordered collection of unique objects.

```python
def list_years(medals_data):

    years = set()

    for data in medals_data:

        years.add(data["Year"])

    return years

    

print "The dataset contains data for the years %s" % list_years(raw_medals_data)
```

**Output**:

```
The dataset contains data for the years set(['2002', '2000', '2006', '2004', '2008', '2010', '2012'])

```

Exercise: Use the `list_years(...)` function and the `count_medals(...)` function to write a function `total_medals_won_by_country` that counts the number of medals won by a country across the entire dataset

```python
def total_medals_won_by_country(medal_data, country):

    total_medals = 0

    for year in list_years(medal_data):

        total_medals += count_medals(medal_data, country, year)

    return total_medals

    

print "Ireland won %d medals over all years in the dataset" % total_medals_won_by_country(raw_medals_data, "Ireland")

print "Great Britain won %d medals over all years in the dataset" % total_medals_won_by_country(raw_medals_data, "Great Britain")

print "Greece won %d medals over all years in the dataset" % total_medals_won_by_country(raw_medals_data, "Greece")

print "Hungary won %d medals over all years in the dataset" % total_medals_won_by_country(raw_medals_data, "Hungary")
```

**Output**:

```
Ireland won 9 medals over all years in the dataset

Great Britain won 322 medals over all years in the dataset

Greece won 59 medals over all years in the dataset

Hungary won 145 medals over all years in the dataset

```

Exercise: Write a function to count the total number of medals awarded in a year.



Hint: Count the number of medals each country won in the given year

```python
def list_countries(medal_data):

    countries = set()

    for data in medal_data:

        countries.add(data["Country"])

    return countries



def total_medals_won_by_year(medal_data, year):

    total_medals = 0

    for country in list_countries(medal_data):

        total_medals += count_medals(medal_data, country, year)

    return total_medals

        

print "There were %d total medals awarded in 2000" % total_medals_won_by_year(raw_medals_data, "2000")

print "There were %d total medals awarded in 2012" % total_medals_won_by_year(raw_medals_data, "2012")
```

**Output**:

```
There were 2005 total medals awarded in 2000

There were 1946 total medals awarded in 2012
```



```

Exercise: How could we use everything we've written so far to count how many medals were awarded total?

```python
def total_medals_awarded(medal_data):

    total_medals = 0

    for year in list_years(medal_data):

        total_medals += total_medals_won_by_year(medal_data, year)

    return total_medals



print "%d medals were awarded across all countries and years in the dataset" % total_medals_awarded(raw_medals_data)
```

**Output**:

```
9529 medals were awarded across all countries and years in the dataset

```

## Classes



We can think of a lot of things we might be interested in counting with this dataset. Classes are a way to group a set of conceptually related data and operations.  We can combine together the functions we've written so far in to a single medal counting object

```python
class MedalCounting:

    def __init__(self, medals_data):

        self.medals_data = medals_data

    

    def num_medals(self, country, year, medal):

        for data in self.medals_data:

            if data["Country"] == country and data["Year"] == year:

                return int(data[medal])

            

        return 0

            

    def count_all_medals(self, country, year):

        return self.num_medals(country, year, "Gold Medals") + \

            self.num_medals(country, year, "Silver Medals") + \

            self.num_medals(country, year, "Bronze Medals")

            

    def list_years(self):

        years = set()

        for data in self.medals_data:

            years.add(data["Year"])

        return years

    

    def total_medals_won_by_country(self, country):

        total_medals = 0

        return self.count_medals(country, self.list_years(), ["Gold Medals", "Silver Medals", "Bronze Medals"])
```
Challenge: We could vastly improve our counting by doing all the counting in a single pass over the data.  Use the template below to implement a more efficent counting method

```python
class MedalCounting:

    def __init__(self, medals_data):

        self.medals_data = medals_data

    

    def count_medals(self, country, years, medals):

        num_medals = 0

        for data in self.medals_data:

            if data["Country"] == country and data["Year"] in years:

                for medal in medals:

                    num_medals += int(data[medal])

                    

        return num_medals
```

**Output**:

```
Ireland won 9 medals over all years in the dataset

```

```python
class MedalCounting:

    def __init__(self, medals_data):

        self.medals_data = medals_data

    

    def count_medals(self, countries, years, medals):

        num_medals = 0

        for data in self.medals_data:

            if data["Country"] in countries and data["Year"] in years:

                for medal in medals:

                    num_medals += int(data[medal])

                    

        return num_medals

            

    def count_all_medals(self, country, year):

        return self.count_medals([country], [year], ["Gold Medals", "Silver Medals", "Bronze Medals"])

    

    def count_silver_medals(self, country, year):

        return self.count_medals([country], [year], ["Silver Medals"])

 

    def total_medals_won_by_country(self, country):

        return self.count_medals(country, self.list_years(), ["Gold Medals", "Silver Medals", "Bronze Medals"])

        

    def total_medals_won_by_year(self, year):

        return self.count_medals(self.list_countries(), year, ["Gold Medals", "Silver Medals", "Bronze Medals"])

    

    def total_medals_awarded(self):

        return self.count_medals(self.list_countries(), self.list_years(), ["Gold Medals", "Silver Medals", "Bronze Medals"])

    

    def list_years(self):

        years = set()

        for data in self.medals_data:

            years.add(data["Year"])

        return years

    

    def list_countries(self):

        countries = set()

        for data in self.medals_data:

            countries.add(data["Country"])

        return countries



counter = MedalCounting(raw_medals_data)

print "There are %d years in the dataset" % len(counter.list_years())

print "There are %d total countries in the data set" % len(counter.list_countries())

print "Ireland won %d medals over all years in the dataset" % counter.total_medals_won_by_country("Ireland")

print "Brazil won %d silver medals in 2012" % counter.count_silver_medals("Brazil", "2012")

print "There were %d total medals awarded in 2000" % counter.total_medals_won_by_year("2000")

print "There were %d total medals awarded in 2012" % counter.total_medals_won_by_year("2012")

print "There were %d total medals awarded over all years in the dataset" % counter.total_medals_awarded()
```

**Output**:

```
There are 7 years in the dataset

There are 110 total countries in the data set

Ireland won 9 medals over all years in the dataset

Brazil won 34 silver medals in 2012

There were 2005 total medals awarded in 2000

There were 1946 total medals awarded in 2012

There were 9529 total medals awarded over all years in the dataset

```

```python
```
