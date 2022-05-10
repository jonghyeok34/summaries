# common deployment cases

1. new product/capability
2. automate/assist with manual task
3. replace previous ML system
- Key ideas:
  - gradual rampu with monitoring
  - rollback

## visaul inspection example
- shadow mode : person and ml check simultaneously
- blue green deployment : gradually go to next version

## degrees of automation
- human only -> shadow mode -> ai assistance -> partial automation -> full automation

# scripts
```
When you train the learning algorithm, the best way to deploy it is usually
not to just turn it on and hope for the best because, well,
what if something goes wrong? When deploying systems are a number of
common use cases or types of use cases as well as different patterns for
how you deploy depending on your use case. Let's go through that in this video. In the last video, I alluded to some
of the differences between a first deployment versus a maintenance and
update deployment. Let's flesh this out into
a little bit more detail. One type of deployment is if you
are offering a new product or capability that you had
not previously offered. For example, if you're offering a speech
recognition service that you have not offered before, in this case, a common
design pattern is to start up a small amount of traffic and
then gradually ramp it up. A second common deployment use case is if
there's something that's already being done by a person, but we would now like
to use a learning algorithm to either automate or assist with that task. For example, if you have people in the
factory inspecting smartphones scratches, but now you would like to use a learning
algorithm to either assist or automate that task. The fact that people were previously doing
this gives you a few more options for how you deploy. And you see shadow mode deployment
takes advantage of this. And finally, a third common deployment
case is if you've already been doing this task with a previous implementation
of a machine learning system, but you now want to replace it
with hopefully an even better one. In these cases,
two recurring themes you see are that you often want a gradual
ramp up with monitoring. In other words, rather than sending tons
of traffic to a maybe not fully proven learning algorithm, you may send it
only a small amount of traffic and monitor it and then ramp up
the percentage or amount of traffic. And the second idea you see
a few times is rollback. Meaning that if for some reason the
algorithm isn't working, it's nice if you can revert back to the previous system
if indeed there was an earlier system. Let's start with an example in visual
inspection where perhaps you've had human inspectors inspect
smartphones for defects for scratches. And you would now like to automate some
of this work with a learning algorithm. When you have people
initially doing a task, one common deployment pattern is
to use shadow mode deployment. And what that means is that you will start
by having a machine learning algorithm shadow the human inspector and
running parallel with the human inspector. During this initial phase, the learning
algorithms output is not used for any decision in the factory. So whatever the learning algorithm says, we're
going to go the human judgment for now. So let's say for this smartphone
the human says it's fine, no defect. The learning algorithm says it's fine. Maybe for this example of a big stretch
down the middle, person says it's not okay and the learning algorithm agrees. And maybe for this example with a smaller
stretch, maybe the person says this is not okay, but the learning algorithm makes a
mistake and actually thinks this is okay. The purpose of a shadow mode deployment
is that allows you to gather data of how the learning algorithm is performing and
how that compares to the human judgment. And by something the output you can
then verify if the learning algorithm's predictions are accurate and
therefore use that to decide whether or not to maybe allow the learning algorithm
to make some real decisions in the future. So when you already have some system that
is making good decisions and that system can be human inspectors or even an older
implementation of a learning algorithm. Using a shadow mode deployment can
be a very effective way to let you verify the performance of a learning algorithm before letting them
make any real decisions. When you are ready to let a learning
algorithm start making real decisions, a common deployment pattern is
to use a canary deployment. So there's a phone, algorithm says it's
okay, rejects that, says that's okay, rejects that, rejects that. And in a canary deployments you would roll
out to a small fraction, maybe 5%, maybe even less of traffic initially and start
let the algorithm making real decisions. But by running this on only
a small percentage of the traffic, hopefully, if the algorithm makes
any mistakes it will affect only a small fraction of the traffic. And this gives you more of
an opportunity to monitor the system and ramp up the percentage of traffic
it gets only gradually and only when you have greater
confidence in this performance. The phrase canary deployment is
a reference to the English idiom or the English phrase canary in a coal mine,
which refers to how coal miners used to use canaries to
spot if there's a gas leak. But with canary the deployment,
hopefully this allows you to spot problems early on before there are maybe overly
large consequences to a factory or other context in which you're
deploying your learning algorithm. Another deployment pattern that is
sometimes used is a blue green deployment. Let me explain with the picture. Say you have a system,
a camera software for collecting phone pictures in your factory. These phone images are sent to a piece
of software that takes these images and routes them into some
visual inspection system. In the terminology of
a blue green deployments, the old version of your software is called
the blue version and the new version, the Learning algorithm you just
implemented is called the green version. In a blue green deployment, what you do is
have the router send images to the old or the blue version and
have that make decisions. And then when you want to
switch over to the new version, what you would do is have the router
stop sending images to the old one and suddenly switch over to the new version. So the way the blue green deployment
is implemented is you would have an old prediction service may be
running on some sort of service. You will then spin up
a new prediction service, the green version, and
you would have the router suddenly switch the traffic over from
the old one to the new one. The advantage of a blue green deployment
is that there's an easy way to enable rollback. If something goes wrong, you can just
very quickly have the router go back reconfigure their router to send traffic
back to the old or the blue version, assuming that you kept your blue version
of the prediction service running. In a typical implementation
of a blue green deployment, people think of switching over
the traffic 100% all at the same time. But of course you can also use a more
gradual version where you slowly send traffic over. As you can imagine, whether use shadow
mode, canary mode, blue green, or some of the deployment pattern, quite a
lot of software is needed to execute this. MLOps tools can help with implementing
these deployment patterns or you can implement it yourself. One of the most useful
frameworks I have found for thinking about how to deploy a system is
to think about deployment not as a 0, 1 is either deploy or not deploy,
but instead to design a system thinking about what is
the appropriate degree of automation. For example,
in visual inspection of smartphones, one extreme would be if there's no
automation, so the human only system. Slightly mode automated would be if
your system is running a shadow mode. So your learning algorithms
are putting predictions, but it's not actually used in the factory. So that would be shadow mode. A slightly greater degree of automation
would be AI assistance in which given a picture like this of a smartphone, you may have a human
inspector make the decision. But maybe an AI system can affect
the user interface to highlight the regions where there's a scratch
to help draw the person's attention to where it may be
most useful for them to look. The user interface or UI design
is critical for human assistance. But this could be a way to get
a slightly greater degree of automation while still keeping the human in the loop. And even greater degree of automation
maybe partial automation, where given a smartphone, if the learning algorithm is
sure it's fine, then that's its decision. It is sure it's defective,
then we just go to algorithm's decision. But if the learning algorithm is not sure,
in other words, if the learning algorithm prediction
is not too confident, 0 or 1, maybe only then do we
send this to a human. So this would be partial automation. Where if the learning algorithm
is confident of its prediction, we go the learning algorithm. But for the hopefully small subset
of images where the algorithm is not sure we send that to
a human to get their judgment. And the human judgment can also be very
valuable data to feedback to further train and improve the algorithm. I find that this partial automation is
sometimes a very good design point for applications where the learning algorithms
performance isn't good enough for full automation. And then of course beyond partial
automation, there is full automation where we might have the learning
algorithm make every single decision. So there is a spectrum of using
only human decisions on the left, all the way to using only the AI
system's decisions on the right. And many deployment applications
will start from the left and gradually move to the right. And you do not have to get all
the way to full automation. You could choose to stop using AI
assistance or partial automation or you could choose to go to
full automation depending on the performance of your system and
the needs of the application. On this spectrum both AI assistance and partial automation are examples
of human in the loop deployments. I find that the consumer
Internet applications such as if you run a web search engine,
write online speech recognition system. A lot of consumer software Internet
businesses have to use full automation because it's just not feasible to someone
on the back end doing some work every time someone does a web search or
does the product search. But outside consumer software Internet,
for example, inspecting things and factories. They're actually many applications where
the best design point maybe a human in the loop deployments rather
than a full automation deployment. In this video,
you saw a few patterns of deployments, such as a shadow mode deployment,
canary deployment, blue green deployment. And you also saw how you can pick
the most appropriate degree of automation depending on your application, which could be a human in the loop
deployments or full automation. As we went through these ideas, you heard
me mention a few times the importance of monitoring to help you spot problems
if any so they can address them. Let's dive into the details of how to
monitor the system in the next video.
```