import subprocess
import networkx as nx
import matplotlib.pyplot as plt
from graphviz import Digraph
from tqdm import tqdm

def get_package_dependencies(package_name):
    try:
        output = subprocess.check_output(['apt-cache', 'depends', package_name], universal_newlines=True)
        dependencies = [line.split(':')[1].strip() for line in output.split('\n') if 'Depends' in line]
        return dependencies
    except subprocess.CalledProcessError:
        print(f"Error: Package '{package_name}' not found.")
        return []

def create_dependency_graph(package_name, depth=2):
    G = nx.DiGraph()
    queue = [(package_name, 0)]
    visited = set()

    with tqdm(total=100, desc="Creating dependency graph", unit="%") as pbar:
        while queue:
            pkg, level = queue.pop(0)
            if pkg not in visited and level <= depth:
                visited.add(pkg)
                dependencies = get_package_dependencies(pkg)
                for dep in dependencies:
                    G.add_edge(pkg, dep)
                    if dep not in visited:
                        queue.append((dep, level + 1))
                
                # Update progress bar
                progress = (len(visited) / (len(queue) + len(visited))) * 100
                pbar.update(progress - pbar.n)

    return G

def visualize_graph(G, output_file='dependency_graph'):
    dot = Digraph(comment='Package Dependency Graph')
    dot.attr(rankdir='LR', size='8,5')

    with tqdm(total=len(G.nodes()) + len(G.edges()), desc="Generating graph", unit="item") as pbar:
        for node in G.nodes():
            dot.node(node, node)
            pbar.update(1)
        
        for edge in G.edges():
            dot.edge(edge[0], edge[1])
            pbar.update(1)

    print("Rendering graph...")
    dot.render(output_file, view=True, format='png')

if __name__ == "__main__":
    package_name = input("Enter the package name: ")
    depth = int(input("Enter the depth of dependencies to visualize (1-3 recommended): "))
    
    G = create_dependency_graph(package_name, depth)
    visualize_graph(G, f'{package_name}_dependency_graph')
    print(f"Dependency graph for {package_name} has been generated.")
