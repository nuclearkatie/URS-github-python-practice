# New practice data!

There are three data files here, as well as a starting python file corresponding to the pickle file (.gpickle). They all contain data generated from the same [Cyclus](http://fuelcycle.org/) input file that I use for testing my own code.

Without going into too much detail, my own work, called [Trailmap](https://github.com/cnerg/trailmap), creates a graph using the python package [NetworkX](http://networkx.org/), as well as pathways through the graph. This information is used as the input into your visualizations, but it can be put into several different formats.

First, I can just turn my graph into a list of edges, something that you've worked with before. This can be found in the file edges.csv

Next, I can return the graph object directly, in a file format called pickling. I included a graph.gpickle file, and the beginning of a python code to handle that file, plot.py.

Finally, I included a list of pathways, similar to the pathways you've played with before. You can try using this to generate the graph if you want. I'm also interested in overlaying individual pathways onto the larger graph, perhaps in red so they stand out from the rest. Since your visualizations are interactive, it would be cool to find a way to flip through each of the pathways. Just a thought...

Start by playing around with automating these!

Don't forget to update your fork! [This issue](https://github.com/nuclearkatie/URS-github-python-practice/issues/1) reminds you how, or checkout the [Git Workflows](https://docs.google.com/presentation/d/1E37ZyFhwGERMQsMbgMp6mx3a325xpeuFOAsuiDT871E/edit) presentation (access through UW account)
