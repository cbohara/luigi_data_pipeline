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
