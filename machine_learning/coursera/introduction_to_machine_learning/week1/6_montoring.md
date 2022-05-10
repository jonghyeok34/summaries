# monitoring dashboard
- monitors serve load fraction of non-null outputs
- fraction of missing input values
  - brainstorm the things taht could go wrong
  - brainstorm a few statistics/metrics that will detect the problem
# examples of metics to track
- software metrics : memory, compute, latency, throughput, server load
- input metrics
  - avg input length
  - num missing values
  - avg image brightness
- output metrics
  - time return " "(null)
  - times user redoes search 
  - times user switches to typing
  - CTR

# ML modeling is iterative, so is deployment
- ML model / data -> experiment -> error analyasis -> iterate from model/data
- deployment/monitoring -> traffic -> performance analysis -> iterate

# monitoring dashboard
- set thresholds for alarms
- adapt metrics and thresholds over time

# model maintenance
- manual retraining
- automatic retraining
- 

# scripts
```
How can you monitor a
machine learning system to make sure that it is meeting your performance expectations? In this video, you'll
learn about best practices for monitoring deployed
machine learning systems. The most common way to monitor a machine
learning system is to use a dashboard to track
how it is doing over time. Depending on your application, your dashboards may
monitor different metrics. For example, you may have one dashboard to monitor
the server load, or a different
dashboards to monitor diffraction of non-null outputs. Sometimes a speech
recognition system output is null when the things that
users didn't say anything. If this changes
dramatically over time, it may be an indication
that something is wrong, or one common one I've
seen for a lot of structured data task is monitoring the fraction
of missing input values. If that changes, it may mean that something has changed
about your data. When you're trying to
decide what to monitor, my recommendation is
that you sit down with your team and brainstorm all the things that
could possibly go wrong. Then you want to know about
if something does go wrong. For all the things
that could go wrong, brainstorm a few statistics or a few metrics that will
detect that problem. For example, if you're worried about user traffic spiking, causing the service
to become overloaded, then server loads
maybe one metric, you could track and so on
for the other examples here. When I'm designing my monitoring dashboards
for the first time, I think it's okay to start off with a lot of different
metrics and monitor a relatively large set and then gradually
remove the ones that you find over time not to
be particularly useful. Here are some examples
of metrics our views or I've seen others use
on a variety of projects. First are the software metrics, such as memory, compute, latency, throughput, server load, things that help you
monitor the health of your software
implementation of the prediction service or other pieces of software around
your learning algorithm. But these software metrics
will help you make sure that your software
is running well. Many MLOps tools will
come over the bouts already tracking these
software metrics. In addition to the
software metrics, I would often choose
other metrics that help monitor the statistical health or the performance of
the learning algorithm. Broadly, there are two types of metrics you might
brainstorm around. One is input metrics, which are metrics
that measure has your input distribution x change. For example, if you are building a speech
recognition system, you might monitor the
average input length in seconds of the length for the audio clip fed to your system. You might monitor the
average input volume. If these change for some reason, that might be something
you'll once to take a look at just to make sure this hasn't hurt the performance
of your algorithm. I mentioned just now, number or percentage of missing values is a
very common metric. When using structured data, some of which may
have missing values, or for the manufacturing
visual inspection example, you might monitor
average image brightness if you think that lighting
conditions could change, and you want to make sure
you know if it does, so you can brainstorm
different metrics to see if your input distribution
x might have changed. A second set of metrics
that help you understand if your learning
algorithm is performing well are output metrics. Such as, how often does your speech recognition
system return null, the empty string, because the things the user
doesn't say anything, or if you have built a speech recognition system
for web search using voice, you might decide to see
how often does the user do two very quick searches in a row with substantially
the same input. That might be a sign that you misrecognize their query
the first time round. It's an imperfect signal but you could try this metric
and see if it helps. Or you could monitor
the number of times the user first try to use the speech system and
then switches over to typing, that could be a sign that the user got frustrated
or gave up on your speech system and could indicate
degrading performance. Of course, for web search, you would also use maybe very course metrics like
click-through rate or CTR, just to make sure that the
overall system is healthy. These output metrics
can help you figure out if either your
learning algorithm, output y has changed in some way, or if something that comes even after your learning
algorithms output, such as the user's
switching over to typing has changed in
some significant way. Because input and output metrics are application specific, most MLOps tools will need to
be configured specifically to track the input and output metrics for
your application. You may already know that
machine learning modeling is a highly iterative
process, so as deployment. Take modeling, you would come up with a machine
learning model and some data, train the model,
that's an experiment. Then do error analysis and use the error analysis to go
back to figure out how to improve the model or your data and is by
iterating through this loop multiple
times that you then hopefully gets a good model. I encourage you to think of deployments as an
iterative process as well. When you get your first
deployments up and running and put in place a
set of monitoring dashboards. But that's only the start
of this iterative process. A running system
allows you to get real user data or real traffic. It is by seeing how
your learning algorithm performs on real data
on real traffic that, that allows you to do
performance analysis, and this in turn
helps you to update your deployment and to keep
on monitoring your system. In my experience,
it usually takes a few tries to converge to the right set of
metrics to monitor. Sometimes have deploy the
machine learning system, and it's not uncommon
for you to deploy machine learning system with
an initial set of metrics only to run the system for a few weeks and then
to realize that something could go wrong with it that you hadn't thought of before and into pick a
new metric to monitor. Or for you to have some
metric that you monitor for a few weeks and then
decide they're just metric, hardly ever changes
in does is inducible, and to get rid of that metric in favor of focusing attention
on something else. After you've chosen a set
of metrics to monitor, common practice would be to
set thresholds for alarms. You may decide based on this set, if the server load
ever goes above 0.91, that may trigger an alarm or a notification to
let you know or let the team know to see if
there's a problem and maybe spin up some more servers. Or if the fashion of
non-null plus goals above or beyond
certain thresholds that might trigger an alarm. Or if they're not, fraction
of missing values goes above or below some
set of thresholds, maybe that should
trigger an alarm, and it is okay if you adapt the metrics and the
thresholds over time to make sure that they
are flagging to you the most relevant
cases of concern. If something goes wrong with
your learning algorithm, if is a software issue such
as server load is too high, then that may require changing the software
implementation, or if it is a performance problem associated with the accuracy
of the learning algorithm, then you may need to
update your model. Or if it is an issue associated with the accuracy of
the learning algorithm, then you may need to go
back to fix that that's why many machine learning models
will need a little bit of maintenance or
retraining over time. Just like almost all software needs some level of
maintenance as well. When a model needs to be updated, you can either retrain it
manually, where in Engineer, maybe you will retrain the model perform
error analysis and the new model and
make sure it looks okay before you push
that to deployment. Or you could also put in place a system where there is
automatic retraining. Today, manual retraining is far more common than
automatically training for many applications developers
are reluctant to learning algorithm be fully
automatic in terms of deciding to retrain and pushing
new model to production, but there are some applications, especially in consumer
software Internet, where automatically
training does happen. We'll talk more about retraining
and how to vet or verify a model's performance
before pushing a new model out to production
in next week's videos. But the key takeaways are that it is only by monitoring
the system that you can spot if there may
be a problem that may cause you to go back to perform
a deeper error analysis, or that may cause you to
go back to get more data with which you can
update your model so as to maintain or improve
your system's performance. You learn more about
how to update models in the next two weeks
Materials as well. In this video,
you'll learn how to monitor the performance of
the machine learning system, so that in case something needs to be maintained or fixed, you can be alerted so they can take the appropriate action. We've talked about how to monitor the performance of a single
machine learning model. One of the most useful concepts is for more complex systems, where you don't
have just one model with a more complex
machine learning pipeline, how do you monitor the
performance of that? You'll learn about that
in the next video.
```