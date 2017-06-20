### PyCon 2017 - Building a Data Pipeline with Luigi
#### https://github.com/iamaaronknight/luigi-exercise-template
#### http://pyvideo.org/pycon-us-2017/build-a-data-pipeline-with-luigi.html

- How to run hello_world.py
    - start daemon
        - luigid --background --logdir=./logs --port=8082
    - run application
        - python3 hello_world.py HelloWorldTask --workers=2
