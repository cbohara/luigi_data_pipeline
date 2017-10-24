#!/usr/bin/env python
import luigi
import random
from collections import defaultdict


class Streams(luigi.Task):
    # first task in the pipeline will not have requires function
    date = luigi.DateParameter()

    def run(self):
        with self.output().open('w') as output:
            for _ in range(1000):
                output.write('{} {} {}\n'.format(
                    random.randint(0, 999),
                    random.randint(0, 999),
                    random.randint(0, 999)))

    def output(self):
        return luigi.LocalTarget(self.date.strftime('data/streams_%Y_%m_%d_faked.tsv'))


class AggregateArtists(luigi.Task):
    # any task may be customized by instantiating one or more Parameter objects on the class level
    date_interval = luigi.DateIntervalParameter()

    # requires this input in order to execute the run method
    # often the output of the task before it
    def requires(self):
        return [Streams(date) for date in self.date_interval]

    # the actual logic that needs to run
    def run(self):
        artist_count = defaultdict(int)

        for input in self.input():
            with input.open('r') as in_file:
                for line in in_file:
                    timestamp, artist, track = line.strip().split()
                    artist_count[artist] += 1

            with self.output().open('w') as out_file:
                for artist, count in artist_count.iteritems():
                    print >> out_file, artist, count

    # output used to determine if luigi needs to run the task
    # if the output already exists luigi will not run the task
    # used as input to the next task in the pipeline
    def output(self):
        return luigi.LocalTarget('data/artist_streams_%s.tsv' % self.date_interval)


if __name__ == '__main__':
    luigi.run()
