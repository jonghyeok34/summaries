# Case study: Smart speaker
```
What does it feel like to
work on a complex AI product, where isn't just using a single machine-learning
algorithm to map from A to B, but that learning
algorithm is part of a bigger more complex
project or product. I want to start it this week with two case studies of building
complex AI products. First, building a smart speaker so that you can start to
understand what it might feel like to maybe someday work on a complex AI product
within your own company. Let's get started. Smart speakers and voice-activated devices
like these are taking the world by storm and if you don't already
have one in your home, maybe you'll buy one someday. I'd like to go through
a case study of how you would write AI software to get a smart speaker to respond to a verbal command such as
"Hey device, tell me a joke." For this example, rather
than using Alexa, or Okay Google, or Hey Siri, or Hello Baidu as the
wake word or trigger word, to be more device-agnostic, I'm just going to
use "Hey device" as the trigger word or wake word to wake up, say, a smart speaker and let's say you wanted to tell you a joke. So how do you build
a piece of AI software to understand a command like
this and executes on it? These are the steps needed
to process the command. There can be four steps. Step one is the trigger word
or the wake word detection. The speaker uses a
machine-learning algorithm to input the audio
clip and output. Did they just hear
the wake word or the trigger word
"Hey, Device," so outputs 0 or one and once it hears the trigger
word or wake word, once it hears "Hey device," it then has to perform step two, which is speech recognition. So what the software has to do is take the audio of what came after "Hey device" and map that
to "Tell me a joke." This is also done with
machine learning. Whereas the first step here used an A to B mapping to just tell it that it heard the trigger word, this uses a different
A to B mapping to map the audio to a text
transcript of what you just said, which in this case is
the four words: tell me a joke. Now, the algorithm has to figure out what you actually want by saying these four words. And so the third step is
intent recognition. That means to take
whatever you said and to figure out what you
actually wanted to do. So, today's smart speakers
have a limited set of commands such as they can tell a joke or they can tell the time. So you can say "Hey device
what time is it." They can play music. They can sometimes help
you make a phone call. They can tell you
what's the weather, "Hey device, what's
the weather tomorrow?" So, what intent recognition does is take the four words, the speech recognition's output, and use another piece
of AI software, another A to B mapping, that
inputs those four words and outputs which of these five
or other intents do you have. So in this implementation of a machine learning algorithm, the input A is the text transcript "tell
me a joke" and the output B is which of these five types of commands
did the user just utter. Of course, your smart
speaker may be able to understand even more commands
than just these five, in which case B would
be whichever of the five or 20 or 100 commands your smart speaker
knows how to execute. No matter how you ask the smart speaker to tell
you a joke, hopefully, the intent recognition components will recognize
your intent correctly. So that you can also say
not just "Hey device, tell me a joke," but
also "Hey device, do you know any good
jokes" or "Hey device, tell me something funny." Turns out, there are
lot of ways for you to ask a smart speaker
for a joke and a well-designed intent
recognition system should recognize most of them. Finally, now that
your smart speaker has figured out that you really, really want to hear a joke, the last step is
that there will be a software engineer that
has written a piece of code to randomly select a joke and to play the joke
back through the speaker. In other words, they'll
execute a joke. Just for the record,
my favorite joke is why are there
so many shocking results in AI, because AI is
the new electricity. Shocking electricity, get it? Hope you enjoyed
that. So, all right, and in seriousness,
you can think of the four steps of the algorithm
as these four steps, where the first step is
trigger word detection, second step, speech recognition,
then intent recognition, and then finally,
execution of what are the command the user asked
the smart speaker to execute. So the process of having four steps in an AI system
like this or multiple steps, this is sometimes
called an AI pipeline, where you have
multiple AI components. Yes, it's possible to have machine
learning components which process data one step after another and it would not be unusual to have, say, four different teams in
the company where each team focuses on one of the components
of this AI pipeline. That's how we often organize projects within a large company. Let's now look at
a more complex example. One of you issue a more complex commands
like "Hey device, set timer for 10 minutes." These are the steps needed
to process the command. First step, same as before,
is trigger word detection. So input an audio
and just let me know when someone said
the trigger word hey device. Then speech recognition,
where you input the rest of the audio and transcribe
the rest of the sound, the rest of the audio, "set timer for 10 minutes." And now, intent recognition has
to input that text and output that your intent is that you want to set a timer. One difference between "set timer for 10 minutes" compared to the earlier example
of "tell me a joke" is that you need to know how long to actually
set the timer for. So in the execution step, you actually need
to do two things. One is extract the duration. That means, look at the text, set timer for 10 minutes and pull out the phrase that
tells you how long to actually set the timer for. And so if the user were
to say "Hey device, let me know when
10 minutes is up," then this extract duration step
would have to pull out, again, the 10-minute phrase right
there. And of course, there are lots of ways to
ask for a 10-minute timer. You can also say, "let me know
when 10 minutes are up" or "set an alarm for 10 minutes
from now" and hopefully, the intent recognition
and extract duration components will both be robust enough to recognize
that all of these are different ways of asking
for a 10-minute timer. Finally, to execute the command, there should be a specialized
software component in the smart speaker that can start a timer with a set duration. And after it has extracted
your intent and the duration, it would just start the timer
with that duration, so that the alarm goes off
at the end of 10 minutes. Today's smart speakers
have many functions. Other than the two
we've talked about of telling jokes and
setting a timer, here are some other
functions that many smart speakers today can execute. And the key
steps of executing these commands are trigger word or the wake word detection, speech recognition to transcribe
the text in the command, intent recognition to
figure out which of these functions or which of these commands you
want to execute, and then a specialized program to execute whichever
command you uttered. One of the challenges of
the smart speaker world is that, if you want your smart speaker to have this many different
functions, say, 20 different functions,
then you do need software engineering
teams to write 20 specialized pieces
of software. One to play music, one
to set the volume, one to make calls, one to
ask for the current time, one to convert units like from
teaspoons to tablespoons, or to answer very simple
questions, and on and on. So it's actually quite a lot
of work to write all of these specialized programs to execute all the
different commands you might want to execute in step four. And smart speakers
today actually do so many things that is
difficult for many users to keep straight in their heads exactly what they
can and cannot do. So many smart speaker
companies have been investing a lot in user training to try to let users know what are the things that smart speakers can do. Because on one hand, they can't do everything. There are lot of
things you can't ask smarts speakers to do
such as please call all of my three friends
and see when all of them are able to meet for dinner. So it's been
an ongoing processes of smart speaker companies
to explain to users what they
can and cannot do. Nonetheless, with what they
can do using voice to command, these speakers is making life much more convenient
for many people. I hope this video gave you
a sense of what it takes to build a complex AI product
such as a smart speaker. In order to help you better understand how
these complex products work, let's go on to see a second
case study of how to piece together multiple AI components to build a self-driving car. Let's go on to the next video.
```