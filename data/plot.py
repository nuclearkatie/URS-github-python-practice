import networkx as nx
from pyvis.network import Network


def plt(infile):
    G = nx.read_gpickle(infile)

    nt = Network('500px', '500px')

    nt.from_nx(G)
    nt.show('nx.html')
    return


def make_parser():
    """Makes the Cyclus-Trailmap command line parser"""
    p = argparse.ArgumentParser(description="Cyclus-Trailmap command line",
                                epilog="python main.py cyclus_input_file.xml")
    p.add_argument('infile', nargs=1, help='Cyclus input file. Must be XML')

    return p


def main():
    p = make_parser()
    ns = p.parse_args(args=args)

    plt(ns.infile[0])

    return
    

if __name__ == '__main__':
    main()
