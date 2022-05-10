
- statistical issue/ software

# 
- data drift : sudden change - meme & new celebrities vs concept drift : many amount of f purchase is not fraud after covid
- softwaring
```One of the most
exciting moments of any machine learning
project is when you get to deploy your model, but what makes deployment hard? I think there are
two major categories of challenges in deploying
a machine learning model. First, are the machine learning or the statistical issues, and second, are the
software engine issues. Let's start with both of
these so that you can understand what you need to do to make sure that you have a successful deployment
of your system. One of the challenges of
a lot of deployments is, concept drift and, data drift. Loosely, this means what if your data changes after your system has
already been deployed? I had previously given an example from manufacturing
where you might have trained a learning
algorithm to detect scratches on smartphones under one set of lighting conditions, and then maybe the lighting
in the factory changes. That's one example of the
distribution of data changers. Let's walk through
a second example using speech recognition. I train a few speech
recognition systems, and when I built speech systems, quite often I would have
some purchased data. This would be some
purchased or licensed data, which includes both the input x, the audio, as well
as the transcript y that the speech system
supports it's output. In addition to data that you might purchase
from a vendor, you might also have historical user data
of user speaking to your application together with transcripts of that
raw user data. Such user data, of course, should be collected with very clear user opt-in permission and clear
safeguards for user privacy. After you've trained your
speech recognition system on a data set like this, you might then evaluate
it on a test set, but because speech data
does change over time, when I build speech
recognition systems, sometimes I would collect a dev set or hold
out validation set as well as test set comprising data from just
the last few months. You can test it on fairly recent data to make
sure your system works, even on relatively recent data. After you push the system to deployment, the question is, will the data change
or after you've run it for a few weeks
or a few months, has the data changed yet again? Because the data has changed, such as the language
changes or maybe people are using a brand new model of smartphone which has a
different microphone, so the audio sounds different, then the performance of a speech recognition
system can degrade. It's important for you to recognize how the
data has changed, and if you need to update your learning
algorithm as a result. When data changes, sometimes
it is a gradual change, such as the English
language which does change, but changes very slowly
with new vocabulary introduced at a
relatively slow rate. Sometimes data changes very suddenly where there's a
sudden shock to a system. For example, when COVID-19
the pandemic hit, a lot of credit card fraud
systems started to not work because the purchase patterns of individuals suddenly changed. Many people that did relatively
little online shopping suddenly started to use
much more online shopping. So the way that people were using credit cards changed
very suddenly, and his actually tripped up
a lot of anti fraud systems. This very sudden shift to the data distribution meant that many machine learning
teams were scrambling a little bit at the start of COVID to collect new
data and retrain systems in order to make them adapt to this very new
data distribution. Sometimes the terminology
of how to describe these data changes is not
used completely consistently, but sometimes the term
data drift is used to describe if the input
distribution x changes, such as if a new politician or celebrity suddenly becomes well known and he's mentioned
much more than before. The term concept drift refers
to if the desired mapping. From x to y changes such
as if, before COVID-19. Perhaps for a given user, a lot of surprising
online purchases, should have flagged
that account for fraud. After the start of COVID-19, maybe those same purchases, would not have really
been any cause for alarm, in terms of flagging. That the credit card
may have been stolen. Another example of Concept drift, let's say that x is
the size of a house, and y is the price of a house, because you're trying to
estimate housing prices. If because of inflation
or changes in the market, houses may become more
expensive over time. The same size house, will end up with a higher price. That would be Concept drift. Maybe the size of
houses haven't changed, but the price of a
given house changes. Whereas data drift would be if, say, people start
building larger houses, or start building
smaller houses and thus the input distribution of the sizes of houses
actually changes over time. When you deploy a
machine learning system, one of the most important tasks, will often be to
make sure you can detect and manage any changes. Including both Concept drift, which is when the definition of what is y given x changes. As well as Data drift, which is if the
distribution of x changes, even if the mapping from
x or y does not change. In addition to managing
these changes to the data, a second set of issues, that you will have to manage to deploy a
system successfully, are software engineering issues. You are implementing
a prediction service whose job it is to take queries x and
output prediction y, you have a lot of
design choices as to how to implement
this piece of software. Here's a checklist of questions, that might help you with making the appropriate decisions for managing the software
engineering issues. One decision you have to make
for your application is, do you need Real time predictions or are Batch predictions? For example, if you are building a speech
recognition system, where the user speaks and you need to get
a response back, in half a second, then clearly you need
real time predictions. In contrast, I have
also built systems, for hospitals that
take patient records. Take electronic health
records and run an overnight batch
process to see if there's something associated with the
patients, that we can spot. So in that type of system, it was fine if we just ran it, in a batch of patient
records once per night. Whether you need to write
real time software, they can respond within
hundreds of milliseconds or whether you can
write software that just does a lot of
computation overnight, that will affect how you
implement your software. By the way, later this week, you also get to step through an optional
programming exercise, where you get to implement a real time prediction service, on your own computer. You see that at the optional exercise at the end of this week. Second question you
need to ask is, does your prediction
service run into clouds or does it run at the edge or
maybe even in a Web browser? Today there are many
speech recognition systems that run in the cloud, because having the compute
resources of the cloud, allows for more accurate
speech recognition. There are also some speech
systems, for example, a lot of speech
systems within cars, actually run at the edge. There are also some mobile speech recognition systems that work, even if your Wi-Fi is turned off. Those would be examples of speech systems that
run at the edge. When I am deploying visual inspection
systems in factories, I pretty much almost always
run that at the edge as well. Because sometimes unavoidably, the Internet connection
between the factory, and the rest of the
Internet may go down. You just can't afford to
shut down the factory, whenever its Internet
connection goes down, which happens very rarely but maybe sometimes does happen. With the rise of
modern Web browsers, there are better tools, for deploying
learning algorithms, right there within a
Web browser as well. When building a
prediction service, it's also useful to
take into account, how much computer
resources you have. There have been quite a few
times where I trained a neural network on a
very powerful GPU, only to realize that
I couldn't afford an equally powerful set
of GPUs for deployments, and wound up having to
do something else to compress or reduce
the model complexity. So if you know how much CPU or GPU resources and maybe also how much memory resources you have for your prediction service, then that could help you choose the right software architecture. Depending on your application especially if it's
real-time application, latency and throughputs such
as measured in terms of QPS, queries per second, will be other software engineering metrics
you may need to hit. In speech recognition
is not uncommon to want to get an answer
back to the user, within half a second
or 500 milliseconds. Of this 500
millisecond budget you may be able to allocate only say, 300 milliseconds to your
speech recognition. So that gives a latency
requirement for your system. Throughput refers to
how many queries per second do you need to handle given your
compute resources, maybe given a certain
number of Cloud Service. For example, if you're building
a system that needs to handle 1000 queries per second, it would be useful to
make sure to check out your system so that you have
enough computer resources, to hit the QPS requirement. Next is logging, when building your system it may
be useful to log as much of the data as possible for analysis and review as well as to provide more data for retraining your learning
algorithm in the future. Finally, security and privacy, I find it for
different applications the required levels of security and privacy
can be very different. For example, when I was working on electronic health
records, patient records, clearly the requirements for security and privacy
were very high because patient records are very highly sensitive
information. Depending on your application
you might want to design in the appropriate level
of security and privacy, based on how sensitive
that data is and also sometimes based on
regulatory requirements. If you save this
checklist somewhere, going through this
when you're designing your software might
help you to make the appropriate
software engine choices when implementing your
prediction service. To summarize, deploying a system requires two broad sets
of tasks: there is writing the software to enable you to deploy the
system in production. There is what you
need to do to monitor the system performance and
to continue to maintain it, especially in the
face of concepts drift as well as data drift. One of the things
you see when you're building machine
learning systems is that the practices for the
very first deployments will be quite different compared to when you are
updating or maintaining a system that has already
previously been deployed. I know that to some engineers
that view deploying the machine learning model as
getting to the finish line. Unfortunately, I think
the first deployment means you may be only
about halfway there, and the second half
of your work is just starting only after
your first deployment, because even after you've
deployed there's a lot of work to feed the data back and
maybe to update the model, to keep on maintaining the model even in the face of
changes to the data. One of the things we touch on
the later videos is some of the differences between
the first deployment, such as if your product never had the speech
recognition system. But you've trained the
speech recognition system and you're deploying
for the first time, versus you already have had the learning of running
for some time and you want to maintain or
update that implementation. To summarize, in this video, you saw some of the
machine learning or statistical related issues such as concept drift and data drift. As well as some of the software engineering-related
issues such as, whether you need a batch or
real-time prediction service, and whether the compute
and memory requirements you have to take into account. Now, it turns out that when you're deploying a
machine learning model, there are a number of
common design patterns, a common deployment
patterns that are used in many applications across
many different industries. In the next video, you'll see what are some of the most common
deployment patterns, so that you can
hopefully pick the right one for your application. Let's go on to the next video.
```