# week 1
## 1. deployment example

- script
```
Hi and welcome to machine learning
engineering for production. A lot of learners have asked, Hey Andrew, I've learned to train a machine
learning model, now what do I do? Machine learning models are great, but unless you know how to
put them into production, it's hard to get them to create
the maximum amount of possible value. Or for
those of you that may be looking for a position in machine learning,
many interview as well, Have you ever deployed a machine
learning algorithm production. In this four course specialization,
the first course taught by me, the 2nd, 3rd and 4th causes taught by Robert. Crowe is an expert at this from google. We hope to share with you to practical
hands on skills and techniques. You need to not just build
a machine learning model, but also to put them into production. And so by the end of this first course and
by the end of this specialization, I hope you have a good sense of the entire
life cycle of machine learning project. From training model to
put into production and really how to manage the entire
machine learning project. Let's jump in. Let's start with an example, let's say
you're using computer vision to inspect phones coming off a manufacturing line
to see if there are defects on them. So this phone shown on the left
doesn't have any stretches on it. But if there was a stretch of crack or
something, a computer vision algorithm would hopefully be able to
find this type of stretch, or defect. And maybe put the bounding box around
it as part of quality control. If you get a data set of scratched
phones you can train a computer vision algorithm maybe in your network
to detect these types of defects. But what do you now need to do in order
to put this into production deployment? This would be an example of how you
could deploy a system like this. You might have an edge device. By edge device, I mean a device that is
living inside the factory that is manufacturing these smartphones. And that edge device would have a piece
of inspection software whose job it is to take a picture of the phone,
see if there's a stretch and then make a decision on whether
this phone is acceptable, or not. This is actually commonly done in
factories is called automated visual defect inspection. What the inspection software does is
it will control camera that will take a picture of the smartphone as it
rolls off the manufacturing line. And it then has to make an API call to
pass this picture to a prediction server. And the job of the prediction server
is to accept these API calls, receive an image,
make a decision as to whether or not this phone is defective and
return this prediction. And then the inspection software it can
make the appropriate control decision whether to let it still move
on in the manufacturing line. Or whether to shove it to a side, because
it was defective and not acceptable. So after you have trained
a learning algorithm, maybe train the neural network to take
as input X, pictures of phones. And map down to y predictions about
whether the phone is defective or not. You still have to take this
machine learning model. Put it in a production server,
setup API interfaces and really write all of
the rest of the software. In order to deploy this learning
algorithm into production. This prediction server is
sometimes in the cloud and sometimes the prediction server
is actually at the edge as well. In fact in manufacturing we use edge
deployments a lot, because you can't have your factory go down every time
your internet access goes down. But cloud deployments with prediction
server, is a server in the cloud, is also used for many applications. Let's say you write all the software. What could possibly go wrong? It turns out that just because
you've trained a learning algorithm that does well on your test set,
which is to be celebrated. It's great when you do well
when you hold a test set. Unfortunately reaching that
milestone doesn't mean you're done. There can still be quite a lot of work and challenges ahead to get a valuable
production deployment running. For example, let's say your training
sets has images that look like this. There's a good phone on the left,
the one in the middle, it has a big scratch across it and
you've trained your learning algorithm to recognize that phones like
this on the left are okay. Meaning that no defects and maybe draw
bounding boxes around scratches or other defects that finds and films. When you deploy it in the factory,
you may find that the real life production deployment gives you back
images like this much darker ones. Because the lighting factory, because the
lighting conditions in the factory have changed for some reason compared to the
time when the training set was collected. This problem is sometimes called
concept drift or data drift. You learn more about these
terms later in this week. But this is one example of the many
practical problems that we, as machine learning engineers should
step up to solve if we want to make sure that we don't just do
well on the holdout test set. But that our systems actually
create value in a practical production deployment environment. I've worked on quite a few projects
where my machine learning team and I would successfully
knew a proof of concept. And by that I mean we train
a model in Jupiter notebook and it will work great and
we will celebrate that. You should celebrate it
when you have a learning, algorithm worked well in Jupiter
notebook in a development environment. But it turns out that sometimes I'll
see many projects where that success, which is a great success to
the practical deployment is still maybe another six months of work. And this is just one of many of the
practical things that a machine learning team has to watch out for and handle in
order to actually deploy these systems. Some machine learning engineers will say
is not a machine learning problem to address these problems. The dataset changes. Some machine engineers think well,
is that the machine learning problem? My point of view is that our job
is to make these things work. And so if the data set has changed is
I think of it as my responsibility when I work on a project to step in and
do what I can to access the data distribution as it
is rather than as I wish it is. So this specialization will teach you
about a lot of these important practical things for building machine learning
systems that work not just in the lab, not just in the Jupiter notebook, but
in a production deployment environment. A second challenge of deploying
machine learning models and production is that it takes a lot
more than machine learning code. Over the last decade there's been a lot
of attention on machine learning models. So your neural network or
other algorithm that learns a function mapping from
some input to some output. And that's been amazing progress
in machine learning models. But it turns out that if you look at
a machine learning system in production, if this little orange rectangle
represents the machine learning code, the machine learning model code. Then this is all the codes you need for
the entire machine learning project. I feel like for
many machine learning projects, maybe only 5-10%,
maybe even less of the code. Machine learning code. And I think this is one of
the reasons why when you have a proof of concept model
working maybe Jupiter notebook. It can still be a lot of work
to go from that initial proof of concept to the production deployment. So sometimes people refer to the POC. Or the proof of concept to production gap. And a lot of that gap is sometimes just
the sheer amount of work it is to also write all of this code out here beyond
the initial machine learning model code. So what is all this other stuff? This is a diagram that have adapted
from a paper by D Scully and others. Beyond the machine learning codes
there are also many components, especially components for
managing the data, such as data collection,
data verification, feature extraction. And after you are serving it, how to monitor the system will monitor
the data comes back, help you analyze it. But there are often many other components
that need to be built to enable a working production deployment. So in this course you learn what
are all of these other pieces of software needed for
a valuable production deployment. But rather than looking at all of these
complex piece is one of the most useful frameworks are found for organizing. The workflow of a machine learning project
is to systematically plan out the life cycle of a machine learning project. Let's go to the next video to dive into
what is the full life cycle of a machine learning project. And I hope this framework
will be very useful for all of your machine learning projects
that you plan to deploy in the future. Let's go to the next video.
```

#