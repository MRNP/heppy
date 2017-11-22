
import os
import heppy.framework.config as cfg
import logging
logging.basicConfig(level=logging.INFO)

inputSample = cfg.Component(
    'test_component',
    files = [os.path.abspath('myTest.root')],
    )

selectedComponents  = [inputSample]

# event reader
from heppy.framework.chain import Chain as Events

# random variable
from heppy.analyzers.examples.simple.RandomAnalyzer import RandomAnalyzer
random = cfg.Analyzer(
    RandomAnalyzer
    )

# print in input test tree
from heppy.analyzers.examples.simple.Printer import Printer
printer = cfg.Analyzer(
    Printer,
    log_level=logging.INFO
    )

# a test for debugging
from heppy.analyzers.examples.simple.Stopper import Stopper
stopper = cfg.Analyzer(
    Stopper,
    iEv = 10
    )

# creating a simple output tree
from heppy.analyzers.examples.simple.SimpleTreeProducer import SimpleTreeProducer
tree = cfg.Analyzer(
    SimpleTreeProducer,
    tree_name = 'tree',
    tree_title = 'A test tree'
    )


# sequence of event processing
sequence = cfg.Sequence([
        random,
        # printer,
        # stopper,
        tree,
] )

from heppy.framework.services.tfile import TFileService
output_rootfile = cfg.Service(
    TFileService,
    'myhists',
    fname='histograms.root',
    option='recreate'
)

services = [output_rootfile]

# finalization of the configuration object. 
config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = services, 
                     events_class = Events )


