from graphviz import Digraph
from hashlib import md5

def jsonToGraph(j, echo=True, coFilter=[]):
    g = Digraph(format='png')
    g.graph_attr['rankdir'] = 'LR'
    for clusteroperator in j.get('items'):
        coname = clusteroperator['metadata']['name']
        if len(coFilter) > 0:
            if coname in coFilter:
                # Filter match, continue. Add to digraph.
                g.node(md5(coname.encode()).hexdigest(), coname, fontcolor='red')
            else:
                # Cluster Operator doesn't match filter, skip
                continue
        # No filter, continue. Add to digraph.
        g.node(md5(coname.encode()).hexdigest(), coname, fontcolor='red')
        status = clusteroperator.get('status')
        if status is None:
            # If for some reason there's no status, skip
            continue
        relatedObjects = status.get('relatedObjects')
        if relatedObjects is None:
            # If for some rason there's no relatedObjects, skip
            continue
        for r in relatedObjects:
            # Extract relevant resource attributes 
            # TODO: Add filter for resource types
            group = r.get('group')
            resource = r.get('resource')
            namespace = r.get('namespace')
            name = r.get('name')
            # TODO: Improve this formatting
            fq = 'Name: %s\nType: %s\nGroup: %s\nNS: %s' % (name, resource, group, namespace)
            # Finally, add to digraph
            g.node(md5(fq.encode()).hexdigest(), fq, fontcolor='green')
            g.edge(md5(coname.encode()).hexdigest(), md5(fq.encode()).hexdigest())
    if echo:
        print(g.source)
    return g
