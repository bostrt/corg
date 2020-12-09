import click
import json
import yaml
from graphviz import Digraph, render
from corg import graph


def doParse(file):
    try:
        with open(file.name) as jfile:
            j = json.load(jfile)
        return j
    except json.JSONDecodeError:
        pass

    try:
        with open(file.name) as yfile:
            y = yaml.load(yfile, Loader=yaml.SafeLoader)
            return y
    except yaml.YAMLError as e:
        return None


@click.group()
def cli():
    pass


@cli.command(help='Render an image of the graph and optionally save to a file.')
@click.argument('file', type=click.File('rb'), required=True)
@click.option('-o', '--output', type=click.Choice(['png', 'jpg', 'svg'], case_sensitive=False), default='svg')
@click.option('-f', '--filter', multiple=True, default=[], help='Specify a filter for Cluster Operator names. This option can be specified multiple times.')
def view(file, output, filter):
    p = doParse(file)
    if p is None:
        click.secho("Error parsing file as JSON or YAML", fg="red")
        return
    g = graph.dictToGraph(p, echo=False, coFilter=filter)
    g.render('/tmp/output.svg', view=True)


@cli.command(help='Print DOT formatted graph to stdout.')
@click.argument('file', type=click.File('rb'), required=True)
@click.option('-f', '--filter', multiple=True, default=[], help='Specify a filter for Cluster Operator names. This option can be specified multiple times.')
def dot(file, filter):
    p = doParse(file)
    if p is None:
        click.secho("Error parsing file as JSON or YAML", fg="red")
        return
    g = graph.dictToGraph(p, echo=True, coFilter=filter)


@cli.command('print', help='Print nicely formatted output to stdout.')
@click.argument('file', type=click.File('rb'), required=True)
@click.option('-f', '--filter', multiple=True, default=[], help='Specify a filter for Cluster Operator names. This option can be specified multiple times.')
def printOut(file, filter):
    p = doParse(file)
    if p is None:
        click.secho("Error parsing file as JSON or YAML", fg="red")
        return
    g = graph.dictToGraph(p, echo=True, coFilter=filter)
    # TODO: Pretty print :) 


if __name__ == '__main__':
    cli()