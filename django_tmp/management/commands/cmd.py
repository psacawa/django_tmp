import shtab
from django.core.management import BaseCommand
from argparse import ArgumentParser


class Command(BaseCommand):
    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument("-f", "--foo")
        shtab.add_argument_to(parser, ["-s", "--print-completion"])

    def handle(self, *args, **kwargs):
        print(f"{args=} {kwargs=}")
