#!/usr/local/bin/python3
import luigi


class HelloTask(luigi.Task):
    def run(self):
        with open('hello.txt', 'w') as hello_file:
            hello_file.write('Hello')
            hello_file.close()


if __name__ == '__main__':
    luigi.run()
