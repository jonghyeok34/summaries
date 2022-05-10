# speech recognitino example
- audio -> speech recognition -> transcript
- audio -> VAD(voice activity detection) -> speech recognition -> transript

# user profile example
- user data -> user profile -> recommender system -> product recommendations

# metrics to monitor
- software metrics : 
- input metrics
- output metrics

- how quickly do they change
  - `user data` generally has `slower` drift
  - `enterprise data`(B2B applications) can shft `fast`

# scripts
```
Many AI systems are not just a single
machine learning model running a prediction service, but instead
involves a pipeline of multiple steps. So what a machine learning pipelines and how do you build monitoring systems for
that? Let's learn about that in this video. Let's continue with our speech
recognition example, you've seen how a speech recognition system may take as
input audio and output a transcript. The way that speech recognition is
typically implemented on mobile apps is not like this, but instead is
a slightly more complex pipeline. Where the audio is fed to
a module called a VAD or a voice activity detection module, whose job it is to see
if anyone is speaking. And only if the VAD module,
the voice activity detection module thinks someone is speaking, does it then
bother to pass the audio on to a speech recognition system whose job it is
to then generate the transcript. And the reason we use a voice activity
detection or VAD module is because if say, your speech recognition
system runs in the cloud. You don't want to stream more bandwidth
than you have to to your cloud server. And so the voice activity detection
module looks at the long stream of audio on your cell phone and clips or shortens the audio to just the part
where someone is talking and streams only that to the cloud server
to perform the speech recognition. So this is an example of a machine
learning pipeline where there is one step usually done by learning algorithm as well
to decide if someone is talking or not. And then the second step, also done by a learning algorithm
to generate the text transcript. When you have two learning algorithms,
one doesn't learn to detect someone's talking and
one does learn to transcribe speech. When you have two such
modules working together, changes to the first module may affect the
performance of the second module as well. For example, let's say that because of the
way a new cell phone's microphone works. The VAD module ends up clipping
the audio differently. Maybe it leaves more silence
at the start or end or less silence at the start or end. And does if the VAD's output changes, that will cause the speech
recognition systems input to change. And that could cause degraded performance
of the speech recognition system. Let's look an example
involving user profiles. Maybe I've used the data such as
clickstream data showing what users are clicking on. And this can be used to build a user
profile that tries to capture key attributes or
key characteristics of a user. For example, I once built user
profiles that would try to expect many attributes of users including whether or
not the user seemed to own a car. Because this would help us decide if it was worth trying to offer car
insurance office to that user. And so whether the user owns
a car could be yes or no or unknown, or
maybe other final graduations and these. And the typical way that the user profile
is built is with a learning algorithm to try to predict if this user of the car. This type of user profile, which can have
a very long list of predicted attributes, can then be fed to recommend a system. Another learning algorithm that then takes this understanding of the user to try
to generate product recommendations. Now, if something about
the click stream data changes, maybe this input distribution changes,
then maybe over time if we lose our ability to
figure out if a user owns a car, then the percentage of
the unknown tag here may go up. And because the user
profiles output changes, the input to the recommended
system now changes and this might affect the quality
of the product recommendations. When you have a machine
learning pipelines, these cascading effects in the pipeline
can be complex to keep track on. But if the percentage of unknown labels
does go up, this could be something that you want to be alerted to so that you can
update the recommend the system if needed to make sure you continue to generate
high quality product recommendations. So when building these complex
machine learning pipelines, which can have machine
learning based components or non-machine learning based
components throughout the pipeline. I find it useful to brainstorm metrics
to monitor that can detect changes including concept drift or data driven or
both, and multiple stages of the pipeline. So, metrics to monitor include
software metrics for perhaps each of the components in the pipeline, or perhaps
for the overall pipeline as a whole. As well as input metrics and
potentially output metrics for each of the components of the pipeline. And by brainstorming metrics associated
with individual components of the pipeline as well. This could help you spot problems such
as the voice activity detection system of putting longer or shorter audio clears
over time or the user profile system suddenly having more unknown attributes
for whether the user owns a car. And thereby alert you to
changes in the data that may require you to take action
to maintain the model. But the principle that you saw in the last
video of brainstorm all the things that could go wrong, including things
that could go wrong with individual components of the pipeline and
design metrics to track those. That principle still applies only now
you're looking at multiple components in the pipeline. Finally, how quickly does data change? The rate at which data changes
is very problem dependent. For example, let's see it built
to face recognition system. Then the rate at which people's
appearances changes usually isn't that fast. People's hairstyles and
clothing does change with fashion changes. And as cameras get better,
we've been getting higher and higher resolution pictures
of people over time. But for the most part, people's
appearances don't change that much. But there are sometimes things that
can change very quickly as well, such as if a factory gets a new batch of
material for how they make cell phones and so all the cell phones not
to change in appearance. So some applications will have data that
changes over the time scale of months or even years. And some applications with data that could
suddenly change in a matter of minutes. Speaking in very broad generalities,
I find that on average, user data generally
changes relatively slowly. If you run a consumer facing business
with a very large numbers of users, then it is quite rare for millions of users to all suddenly change
their behavior all at the same time. And so user data, if a large number of users will
usually change relatively slowly. There are a few exceptions, of course,
COVID-19 being one of them were a shock to society actually cause a lot of people's
behavior that all change at the same time. And if you look at web search traffic,
you will see trends maybe a holiday or a new movie and
people start searching for something new. They just became popular. So there are exceptions, but on average,
if you have a very large group of users, there are only a few forces. They can simultaneously change
the behavior of a lot of people or at the same time. In contrast, if you work on a B2B or
business to business application, I find an enterprise data or
business data can shift quite quickly. Because the factory making
cellphones may suddenly decide. So use a new coating for the cell
phones and suddenly the entire dataset changes because the cell phones
suddenly all look different. But if you're providing a machine
learning system to a company, then sometimes if the CEO of that
company decides to change the way that business operates,
all of that data can shift very quickly. I know that these two bullets
are speaking in generalities and there are certain exceptions
to both of these. But maybe this will give you a way of
thinking about how quickly your data is likely to change or not change. So that's it, congratulations on making
it to the end of this first weeks videos. I hope you also take a look at
the practice quizzes which will let you practice all of these concepts and
make sure you deeply understand them. And if you want, you can also take a look at this week's
optional programming exercise which will let you deploy a machine learning
model on your own computer. And I also look forward to seeing you
in next week's videos where we'll dive together much more deeply into
the modeling part of the full cycle of machine learning project. I look forward to seeing you next week.
```