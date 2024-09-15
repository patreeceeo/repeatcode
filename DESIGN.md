# Design

Hard code a list of problems where each item is a tuple containing:
- the numeric ID from LeetCode
- the problem slug
- the difficulty rating
- a list of topics

When the program starts, load this list into a <?> that can be queried:
- By topic -> an iterable of problems
- By problem ID -> a problem

It also loads information about the user's progress in learning the problems.
This information can be stored in a JSON file for now.

With no args, it outputs a problem in the following format:

"{problem\_slug}"

The intent is for this program to work in tandem with a simple shell script
that uses this output to launch a development environment. Maybe this
environment is LeetCode itself, maybe it's a terminal app, or a GUI app....

The problem is selected using a scheduling algorithm: Looking at when
problems for each topic were last studied, it selects the least recently
studied topic that hasn't been studied for at least N days. N is a value
associated with each topic that is a function of the user's level of
expertise with such problems. From there, it simply selects the least
recently practiced problem with that topic.

Once the user exits the development environment, the shell script can
ask, using fzf, how they fared. Their response can be fed back into
this program, using a special argument, to update the N value for that
topic. A topic is considered mature once its N value is over 30.

A Problem consists of:
- a numeric ID
- a slug
- a difficulty rating
- a set of topics

A Topic is:
- a name
- a set of problems
- an average difficulty (calculated dynamically)

A TopicPracticeItem associates a Topic with a PracticeState. It also has:
- The last time it was practiced
- the number of days to wait until it should be practiced

A ProblemPracticeItem associates a Problem with a PracticeState. It also has:
- The last time it was practiced

A PracticeState can be either:
- new
- learning
- mature

The JSON file containing info about the user's progress consists of:
- A topics key
- A problems key

The topics key points to a dictionary of topic names to PracticeStates.

# Out of Scope

With no args, it outputs a list of tags that can be piped to fzf.
The list of tags is filtered by whether the user has attempted a problem
with that tag today.

The list of tags includes:
- name
- number of problems
- average difficulty rating

Or, given a tag, it outputs a problem with that tag in a format that can be
used to start an editor instance and updates that problem's state. The
least recently practiced problem is selected.
