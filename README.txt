https://marcobonzanini.com/2015/10/24/building-data-pipelines-with-python-and-luigi/
https://gist.github.com/bonzanini/40774bf9348d35d9ea4f
------------------------------------------------------------------------------------------
http://pyvideo.org/pycon-us-2017/build-a-data-pipeline-with-luigi.html
https://github.com/iamaaronknight/luigi-exercise-template

# start daemon
luigid --background --logdir=./logs --port=8082

# kill daemon
ps -ef | grep luigid
kill [pid]

# run application
python3 hello_world.py HelloWorldTask --workers=2
------------------------------------------------------------------------------------------
https://www.youtube.com/watch?v=Ny2X_WNxrB4
https://www.slideshare.net/jonathandinu/presentation-45784222
https://github.com/hopelessoptimism/data-engineering-101

luigid is a centralized server waiting to run tasks

use python script.py --help

parameters allow you to specify input via the command line
NOTE - luigi turns all underscores into dashes
filename = luigi.Parameter()

defaults to a string
can provide static typing
evaluate = luigi.BoolParameter(default=False)

start the pipeline with luigi.ExternalTask
let's luigi know the task does not depend on anything

whenever you have a task you want to ask what are your inputs and what are you outputs
best practice = provide a single output for a task
if the output already exists Luigi will not run the task again

easy to pull in files from many different sources (s3, hdfs, localfile) and push files to many different formats
easy to deal with serializing and deserializing
pickle converts python objects to binary representation that you can store in a file

get all inputs with self.inputs() method call
self.input() alias to requires()
access specific inputs by specifying its index
self.inputs()[0]

always need to return from requires and output functions 
not required for run function
------------------------------------------------------------------------------------------
https://www.slideshare.net/lallea/data-pipelines-from-zero-to-solid
https://www.slideshare.net/lallea/test-strategies-for-data-processing-pipelines-67244458
