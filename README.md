#### https://github.com/iamaaronknight/luigi-exercise-template
#### http://pyvideo.org/pycon-us-2017/build-a-data-pipeline-with-luigi.html

### PyCon 2017 - Building a Data Pipeline with Luigi
- start daemon
    - luigid --background --logdir=./logs --port=8082
- kill daemon
    - ps -ef | grep luigid
    - kill [pid]
- run application
    - python3 hello_world.py HelloWorldTask --workers=2

- if the file exists in output() then Luigi will not rewrite the file
- if we want to re-write the text files for each run, we need to parameterize the jobs

- create a new hello_world.txt file in a specified directory every time we run the job

