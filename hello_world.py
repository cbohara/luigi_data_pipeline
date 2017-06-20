#!/usr/local/bin/python3
import luigi
from time import sleep


class HelloTask(luigi.Task):
    def run(self):
        sleep(60)
        with open('hello.txt', 'w') as hello_file:
            hello_file.write('Hello')
            hello_file.close()

    def output(self):
        return luigi.LocalTarget('hello.txt')


if __name__ == '__main__':
    luigi.run()
