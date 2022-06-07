# Case study: Self-driving car
```
One of the most
exciting products of the AI era is
the self-driving car. Self-driving cars are also one of the most mysterious things you hear about in AI these days. In this video what I want to
do is share with you a somewhat simplified description of a self-driving car so that you understand how you
can piece together multiple AI components in order to build
these amazing things. Let's get started. These
are the key steps for deciding how to drive
your self-driving car. The car will take as input
various sensors such as pictures of what's in front of the car or to
the sides or behind, as well as maybe radar or Lidar, meaning
laser sensor readings. Given these inputs of a picture
and maybe other things, it then has to detect other cars. So given that, hopefully, you'll figure out
there's a car there, as well as where are
the pedestrians, because we want to avoid other cars as well as
avoid pedestrians. Both car detection and pedestrian detection can be
done with machine learning using input/ output
or A to B mappings that takes as input the picture and maybe radar and Lidar, sends the inputs and tells us where are the other
cars and pedestrians. Finally, now that you know where are the other cars and
where are the pedestrians, you can then feed
this information into another specialized
piece of software, it's called a motion planning piece of software that plans the motion or plans the path that you want
your car to take, so that you can make progress to your destination while
avoiding any collisions. Once you've planned out
the motion for your car, you can then translate that into specific steering angle for your steering wheel and
acceleration and brake commands, so how much to step
on the gas pedal, and how much to brake in
order to get your car to move at the desired angle
as well as speed. Let's look at the three key
steps of car detection, pedestrian detection, and
motion planning in more detail. Car detection uses
supervised learning. So, you've already seen how
a learning algorithm can take as input pictures like these and output the detected cars. For most self-driving
cars rather than using only a front-facing camera, so a camera that looks forward, also often uses cameras
that look to the left, to the right as well as to
the back so it can detect cars not just to the front
but all around it. This is usually done
using not just cameras but other sensors as well
such as radar and Lidar. Next is pedestrian detection, and using a pretty similar type of sensors as well as techniques, self-driving cars can
detect pedestrians. Finally, I briefly mentioned
a motion planning step. So, what is that?
Here's an example. Let's say you're driving
your car and there's this light blue car
in front of you. The motion planning
software's job is to tell you what is the path, shown here in red, you should drive
in order to follow the road and not
have an accident. So the motion planning
software's job is to output the path as well as the speed at which
you should drive your car in order
to follow the road, and the speed should be set so that you don't run
into the other car, but you also drive at
a reasonable speed on this road. Here's another example. If there's this gray car parked on the right side
of the road, so you want to overtake
this stopped car, then the motion planning
software's job is to plot a path like that to let you veer a little
bit to the left and safely overtake a stopped car. So far I've given a rather
simplified description of self-driving as comprising
mainly these three components. Let's look at
a bit more detail of how an actual self-driving
car might work. This is a picture
you've seen so far. Input image, radar, or Lidar, sensor readings into car detection and
pedestrian detection, and that is then fed to motion planning to help you
select your path and speed. Now in a real self-driving car, you would usually use more than just cameras, radar, and Lidar. Most self-driving cars
today will also use GPS to sense its position as
well as accelerometers, sometimes called an IMU,
this means accelerometers, and gyroscopes as well as a map because we know that cars are more likely
to be found on a road, pedestrians are more likely
to be found on sidewalks, although they are sometimes
found on the road as well. All this is usually additional information
that's fed into detect cars and
pedestrians as well as other objects, we'll
talk about in a second. Rather than just detecting
cars and pedestrians, in order to drive safely,
you also need to know where these cars and pedestrians
are going in the future. So, another common component of self-driving cars is
trajectory prediction, where there's another
AI component that tells you, not just the cars and
pedestrians you found, but also where they're likely to go in
the next few seconds, so you can avoid them
even as they're moving. To drive safely
requires more than just navigating other
cars and pedestrians. You also need to know where are the lanes so you might
detect lane markings. If there's a traffic light
you also need to figure out where's
the traffic light, and is it showing a red, yellow, or green signal. Sometimes there are
other obstacles, such as unexpected
traffic cones or maybe there's a flock of geese
walking in front of your car. That needs to be detected as well so that your car can avoid even other obstacles than
cars and pedestrians. On a large self-driving car team, it would not be that unexpected
to have a team or maybe a few people working on each of the boxes shown here in red, and it's by building all
of these components and putting them together
that you can build a self-driving car. As you can tell both from this rather complex example
of an AI pipeline, as well as the early example of the four-step AI pipeline
for the smart speaker, sometimes it takes
a team to build all of these different components
of a complex AI product. What I'd like to do in
the next video is share with you what are the key roles
in large AI teams. If you're either a one-person or small AI team now, that's okay, but I want you to
have a vision of what building a large AI team, maybe in the distant future,
might look like. Let's go on to the next video.
```