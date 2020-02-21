import click
import json
from graphviz import Digraph, render

def jsonToGraph(j):
    g = Digraph(format='png')
    i = 0
    for clusteroperator in j.get('items'):
        #i = i + 1
        #if i > 5:
        #    continue
        coname = clusteroperator['metadata']['name']
        g.node(coname)
        status = clusteroperator.get('status')
        if status is None:
            continue
        relatedObjects = status.get('relatedObjects')
        if relatedObjects is None:
            continue
        for r in relatedObjects:
            group = r.get('group')
            resource = r.get('resource')
            name = r.get('name')
            fq = '%s.%s.%s' % (name, resource, group)
            g.node(fq)
            g.edge(fq, coname)
    click.echo(g.source)

@click.command()
@click.argument('filename')
def run(filename):
    try:
        f = open(filename)
        j = json.load(f)
        jsonToGraph(j)
    except FileNotFoundError as e:
        click.echo(e)

if __name__=='__main__':
    run() #noqa