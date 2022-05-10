# recognition
```
One of the successes of deep learning
has been speech recognition. Deep learning has made speech recognition
much more accurate than maybe a decade ago. And this is allowing many of us to
use speech recognition in our smart speakers on our smartphones for
voice search and in other context. You may have heard occasionally
about the research work that goes into building
better speech models. But what else is needed to actually
build a valuable production deployment speech recognition system. Let's use the machine learning project
life cycle to set through a speech recognition example so you can understand
all the steps needed to actually build and deploy such a system. I've worked on speech recognition systems
in a commercial context before and so the first step of that was scoping
have to first define the project and just make a decision to
work on speech recognition, say for voice search as part
of defining the project. That also encourage you
to try to estimate or maybe at least estimate the key metrics. This will be very problem dependence. Almost every application will have his
own unique set of goals and metrics. But the case of speech recognition,
some things I cared about where how accurate is the speech
system was the latency? How long does the system take
to transcribe speech and what is the throughput? How many queries per second we handle. And then if possible, you might also
try to estimate the resources needed. So how much time, how much compute
how much budget as well as timeline. How long will it take to
carry out this project? I'll have a lot more to say on
scoping in week three of this course. So we'll come back to this topic and
describe this in greater detail as well. The next step is the data stage where
you have to define the data and establish a baseline and
also label and organize the data. What's hard about this? One of the challenges of practical
speech recognition systems is the data label consistently,
here's an audio clip of a fairly typical recording you might get if you're
working on speech recognition for voice search, let me play this audio clip, And the question is given this
audio clip that you just heard "Um today's whether", would you want
to transcribe it like that? Which if you have
transcriptionist label the data, this would be a perfectly
reasonable transcription. Or would you want to
transcribe it like that? Which is also a completely
reasonable transcription or should the transcriptionist say, well
there's often a lot of noise and audio, you know, maybe there's a sound of
a conclave, something fell down and you don't want to transcribe noise. So maybe it's just noise and
you should transcribe it like that. It turns out that any of these three ways
of transcribing the audio is just fine. I would probably prefer either
the first or the second, not the third. But what what hurts your learning
algorithm's performance is if one third of the transcription is used the first,
one third, the second and one third third way of trans driving. Because then your data is inconsistent and
confusing for the learning algorithm, because how is the learning
algorithm supposed to guess which one of these conventions specific transcription has
happened to use for an audio clip. So Spotting correcting
consistencies like that. Maybe just asking everyone to standardize
on this first convention that can have a significant impact on
your learning algorithm’s performance. So we'll come back later in this course
to dive into some best practices for how to spot inconsistencies and
how to address them. Other examples of data
definition questions for an audio clip like today's whether,
how much silence do you want before and after each clip after a speaker
has stopped speaking. Do you want to include another 100
milliseconds of silence after that? Or 300 milliseconds or
500 milliseconds, half a second? Or how do you perform
volume normalization? Some speakers speak loudly, some are less
loud and then there's actually a tricky case of if you have a single audio
clip with some really loud volume and some really soft volume,
all within the same audio clip. So how do you perform volume
normalization. questions like all of these are data
definition questions. A lot of progress in machine learning. That is a lot of machine learning research was driven by researchers
working to improve performance on benchmark data set. In that model, researchers
might download the data set and just work on that fixed data set. And this mindset has led to tremendous
progress in machine learning so no complaints at all about this mindset,
but if you are working on a production system then you don't
have to keep the data set fix. I often edit the training set or even at
the test set if that's what's needed in order to improve the data quality to
get a production system to work better. So what are practical ways to do this
effectively not an ad hoc way, but systematic frameworks for
making sure you have high quality data. You learn more about this
later in this course and later in the specialization as well. After you've collected your data set,
the next step is modeling, in which you have to select and train
the model and perform error analysis. The three key inputs that go into training
a machine learning model are the code that is the algorithm or the neural network
model architecture that you might choose. You also have to pick hyperparameters and
then there's the data and running the code with your
hyperparameters on your data gives you the machine learning model the
celebrate, a machine learning model for learning from, say,
audio clips to text transcripts. I found that in a lot of research work or academic work you tend to hold
the data fixed and vary the code and may be vary the hyperparameters in
order to try to get good performance. In contrast, I found that for
a lot of product teams, if your main goal is to just build and deploy a working
valuable machine learning system, I found that it can be even more
effective to hold the code fixed and to instead focus on optimizing the data
and maybe the hyperparameters, In order to get a high performing model, A machine learning system
includes both codes and data and also hyperparameters that there maybe a bit easier to optimize than the code or
data. And I found that rather than taking
a model-centric view of trying to optimize the code to your fixed
data set for many problems, you can use an open source implementation
of something you download of Git-hub and instead just focus on optimizing the data. So during modeling, do you have to select
and train some model architecture. Maybe some neural network architecture
error analysis can then tell you where your model still falls short. And if you can use that error analysis
to tell you how to systematically improve your data,
maybe improve the code too. That's okay. But often if error analysis can tell you
how to systematically improve the data, that can be a very efficient way for
you to get to a high accuracy model. And part of the trick is you don't want
to just feel like you need to collect more data all the time because
we can always use more data. But rather than just
trying to collect more and more and more data, which is helpful but
can be expensive if their analysis can help you be more targeted in exactly
what data to collect, that can help you'd be much more efficient
in building an accurate model. Finally, when you have
trained the model and when error analysis seems to
suggest is working well enough, you're then ready to go into deployment,
Check speech recognition. This is how you might
deploy a speech system. You have a mobile phone. This would be an edge device with software
running locally on your phone. That software taps into the microphone
to record what someone is saying. Maybe for voice search and
in a typical implementation of speech recognition,
you would use a VAD module. VAD stands for a voice activity detection. Yeah. And it's usually a relatively
simple algorithm. Maybe a learning algorithm and
the job of the VAD allows the smartphone to select out just the audio that
contains hopefully someone speaking so that you can send only that audio
clip to your prediction server. And in this case maybe the prediction
server lives into cloud. This would be a common deployment pattern. The prediction server then
returns both the transcript so the user, so you can see what
the system thinks you said. And it also returns to search results. If you're doing voice search and
the transcript and search results are then displayed in the front and
code running on your mobile phone. So implementing this type of
system would be the work needed to deploy a speech model in
production even after it's running though you still have to monitor and
maintain the system. So here's something that happened to
me once my team had built a speech recognition system and
it was trained mainly on adult voices. We pushed into production,
random production and we found that over time more and
more young individuals, kind of teenagers, you know, sometimes even younger seem to
be using our speech recognition system and the voices are very young
individuals just sound different. And so my speech systems
performance started to degrade. We just were not that good at recognizing
speech as spoken by younger voices. And so he had to go back and find a way to collect more data
are the things in order to fix it. So one of the key challenges when it
comes to deployment is concept drift or data drift,
which is what happens when the data distribution changes,
such as there are more and more young voices being fed to
the speech recognition system. And knowing how to put in place
appropriate monitors to spot such problems and then also how to fix
them in a timely way is a key skill needed to make sure your production
deployment creates a value you hope it will. To recap in this video. You saw the full life cycle of a machine
learning project using speech recognition as the running example. So from scoping to data to
modeling to deployment. Next I want to briefly share
review the major concepts and sequencing you learn about in this course. So come with me to the next video.
```