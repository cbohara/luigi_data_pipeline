https://marcobonzanini.com/2015/10/24/building-data-pipelines-with-python-and-luigi/
https://gist.github.com/bonzanini/40774bf9348d35d9ea4f
------------------------------------------------------------------------------------------
http://pyvideo.org/pycon-us-2017/build-a-data-pipeline-with-luigi.html
https://github.com/iamaaronknight/luigi-exercise-template

start daemon
luigid --background --logdir=./logs --port=8082

kill daemon
ps -ef | grep luigid
kill [pid]

run application
python3 hello_world.py HelloWorldTask --workers=2
------------------------------------------------------------------------------------------
#### https://www.youtube.com/watch?v=Ny2X_WNxrB4
#### https://www.slideshare.net/jonathandinu/presentation-45784222
#### https://github.com/hopelessoptimism/data-engineering-101
