# Github and Python Practice

This Github repo is here as a practice you can use to verify your skills. First, I would recommend getting the [Github Student Developer Pack](https://education.github.com/pack), which gives you access to some features like private repos that you would normally have to pay for. Next, make sure you go through the [First Day on Github](https://lab.github.com/githubtraining/first-day-on-github) tutorial, or the following tasks won't make much sense!

Once you're ready, start below. Feel free to message me on slack or even open an issue if you run into problems (including if I made a mistake and something doesn't work!)

- Fork this repository
- Clone your fork to your machine
- Complete each problem in its own file. You may submit a python file (.py), or something like a [Jupyter notebook](https://jupyter.org/) (.ipynb)
- Try adding, committing, and pushing along the way
- Once you have finished the problems, committed all your work, and pushed it to your fork, open a pull request (PR) to my branch. We'll reveiw it at the next meeting!

Do not forget to label your axes and use legends when applicable!

## Problems*

1. Plot the function ![](https://latex.codecogs.com/gif.latex?f(\beta)&space;=&space;\beta&space;&plus;&space;h&space;\cdot&space;tan(\beta)) as a function of beta, where h=1, from - 4 pi to 4 pi. Note that tangent is discontinuous. How many points do you need to get a good sense of the shape of the graph? Try using a small number (like 10, or 50), and then a much larger one (10000 or above)

2. Nuclear engineers often use an equation called the Point Reactor Kinetics Equations to study how neutrons in a nuclear reactor behaves in time.

![\frac{dn(t)}{dt} = \frac{\rho - \beta}{\Lambda} \cdot n(t) + \lambda \cdot c(t))](https://latex.codecogs.com/gif.latex?\frac{dn(t)}{dt}&space;=&space;\frac{\rho&space;-&space;\beta}{\Lambda}&space;\cdot&space;n(t)&space;&plus;&space;\lambda&space;\cdot&space;c(t)))

![\frac{dc(t)}{dt} = \frac{beta}{\Lambda} \cdot n(t) - \lambda \cdot c(t)](https://latex.codecogs.com/gif.latex?\frac{dc(t)}{dt}&space;=&space;\frac{beta}{\Lambda}&space;\cdot&space;n(t)&space;-&space;\lambda&space;\cdot&space;c(t))

   With some simplifications and specific conditions, a solution to point reactor kinetics is

![n(t) = A e^{w_1 t} + B e^{w_2 t}](https://latex.codecogs.com/gif.latex?n(t)&space;=&space;A&space;e^{w_1&space;t}&space;&plus;&space;B&space;e^{w_2&space;t})

   Let's use A=1.5, B=-0.5, w1 = 0.004, and w2=-5. Plot this graph over time

  a. 0 < t < 0.1 seconds

  b. 0 < t < 10 seconds

3. The "temperature" of neutrons is usually given by a [Maxwellian distribution](https://en.wikipedia.org/wiki/Maxwell%E2%80%93Boltzmann_distribution)

![n(v) = 4 \pi N e^{\frac{-m v^2}{2 kT}} v^2 \left( \frac{m}{2 \pi kT} \right )^{\frac{3}{2}} ](https://latex.codecogs.com/gif.latex?n(v)&space;=&space;4&space;\pi&space;N&space;e^{\frac{-m&space;v^2}{2&space;kT}}&space;v^2&space;\left(&space;\frac{m}{2&space;\pi&space;kT}&space;\right&space;)^{\frac{3}{2}})

   - where N represents the total number of particles
   - m is the mass of each particle
   - n is a quantity such that ndv gives the number of particles with velocities between v and v+dv
   - k is the Boltzmann constant
   - T is the absolute temperature

   use

- m = 1.67*10 -27 kg
- k = 1.38*10 -23 J/K
- N =1000

   Plot the distribution of number of particles vs. velocity at temperature T = 300K. Now add two other distributions at 600K and 1000K. Make a legend.

4. We're going to use networks in our work the rest of the year. Let's try to plot a simple social network. These same ideas can be used to map things like your friends on facebook, but also how nuclear material moves around in the lifecycle of uranium. Use whatever program or style you would like. 

   Joe knows Jill and Kamala. Kamala also knows Doug. Both Joe and Kamala also know Barack.

   Each name is a _node_, and their connections are _edges_. An edge list is given below

   |Joe | Jill|
   |Joe | Kamala|
   |Kamala | Doug|
   |Barack | Joe|
   |Barack | Kamala|

   draw a graph of this network


\* These problems were mainly adaped from a freshman-year course I took and eventually TA'd at the University of Illinois, called NPRE100