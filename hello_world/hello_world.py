#!/usr/local/bin/python3
import luigi
from time import sleep


class HelloTask(luigi.Task):
    path = luigi.Paramter()

    def run(self):
        sleep(60)
        with open(self.path, 'w') as hello_file:
            hello_file.write('Hello')

    def output(self):
        return luigi.LocalTarget(self.path)


class WorldTask(luigi.Task):
    path = luigi.Paramter()

    def run(self):
        sleep(30)
        with open(self.path, 'w') as world_file:
            world_file.write('World')

    def output(self):
        return luigi.LocalTarget(self.path)


class HelloWorldTask(luigi.Task):
    id = luigi.Parameter(default='test')

    def run(self):
        sleep(60)
        with open('hello.txt', 'r') as hello_file:
            hello = hello_file.read()
        with open('world.txt', 'r') as world_file:
            world = world_file.read()
        with open('hello_world.txt', 'w') as output_file:
            content = '{} {}'.format(hello, world)
            output_file.write(content)

    def requires(self):
        return [
            HelloTask(path='results/{}/hello.txt'.format(self.id)),
            WorldTask(path='results/{}/world.txt'.format(self.id)),
        ]

    def output(self):
        path = 'results/{}/hello_world.txt'.format(self.id)
        return luigi.LocalTarget(path)


if __name__ == '__main__':
    luigi.run()
