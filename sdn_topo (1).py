"""Custom topology example
Two directly connected switches plus a host for each switch:
   host --- switch --- switch --- host
Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    '''Simple topology example.'''

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        h1 = self.addHost( 'h1' , ip='10.0.0.1', mac='00:00:00:00:00:01')
        h2 = self.addHost( 'h2' , ip='10.0.0.2', mac='00:00:00:00:00:02')
        h3 = self.addHost( 'h3' , ip='10.0.0.3', mac='00:00:00:00:00:03')
        h4 = self.addHost( 'h4' , ip='10.0.0.4', mac='00:00:00:00:00:04')
        ovsA = self.addSwitch( 's1' )
        ovsB = self.addSwitch( 's2' )
        ovsC = self.addSwitch( 's3' )
        ovsD = self.addSwitch( 's4' )
        

        # Add links
        self.addLink(h1, ovsA)
        self.addLink(h2, ovsB)
        self.addLink(h3, ovsC)
        self.addLink(h4, ovsD)
        self.addLink(ovsA, ovsB)
        self.addLink(ovsB, ovsC)
        self.addLink(ovsC, ovsD)
        self.addLink(ovsD, ovsA)
        #self.addLink( BSwitch, ESwitch	)
        #self.addLink( CSwitch, ESwitch	)
        #self.addLink( DSwitch, rightHost)

topos = { 'mytopo': ( lambda: MyTopo() ) }

