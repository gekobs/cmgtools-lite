from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.Heppy.physicsutils.genutils import isNotFromHadronicShower, realGenMothers, realGenDaughters, motherRef
import numpy as np
import json


def compare_gen_particles_close(thing, other):
    """Compare two gen particles allowing for a relative diff between pt/eta/phi.

    This is to allow for association between two particles that are the same,
    but whose pt/eta/phi have changed slightly and therefore would fail
    thing.p4() == other.p4()
    """
    return (np.isclose(thing.pt(), other.pt(), rtol=1e-3) and
            np.isclose(thing.eta(), other.eta(), rtol=1e-3) and
            np.isclose(thing.phi(), other.phi(), rtol=1e-3) and
            thing.pdgId() == other.pdgId())


class GenParticleRelationshipAnalyzer( Analyzer ):
    """Module to add gen particles, and lists of mother - daughter relationships to the event.

    Note that the gen particles are a concatenation of both pruned and
    packed gen particles. The former is some custom selection, whilst the latter
    is all the final-state (stable) particles. Therefore, any duplicates in the
    packed have been filtered out from the final genParticle collection.

    To store mother-daughter relationships, we do the following.
    If particle 3 has mothers 1 and 2, and particle 4 has mothers 5, 6, 7 then:

    event.motherIndices   = [1, 2, 5, 6, 7]
    event.daughterIndices = [3, 3, 4, 4, 4]

    We have to do it this way because it isn't obvious how to store
    lists in a list of objects.
    """

    def __init__(self, cfg_ana, cfg_comp, looperName ):
        super(GenParticleRelationshipAnalyzer,self).__init__(cfg_ana,cfg_comp,looperName)
 
    def declareHandles(self):
        super(GenParticleRelationshipAnalyzer, self).declareHandles()
        # Not all gen particles, just those "interesting" ones
        self.mchandles['prunedGenParticles'] = AutoHandle( 'prunedGenParticles', 'std::vector<reco::GenParticle>' )
        # All final state (status = 1 acc. to Pythia6) particles
        self.mchandles['packedGenParticles'] = AutoHandle( 'packedGenParticles', 'std::vector<pat::PackedGenParticle>' )
                
    def beginLoop(self,setup):
        super(GenParticleRelationshipAnalyzer,self).beginLoop(setup)

    def addMotherDaughterInfo(self, event):
        genParticles = []
        prunedGenParticles = self.mchandles['prunedGenParticles'].product()
        packedGenParticles = self.mchandles['packedGenParticles'].product()
        genParticles.extend(prunedGenParticles)

        mother_indices = []
        daughter_indices = []
        # Do mother - daughter connections for pruned gen particles
        for ind, p in enumerate(prunedGenParticles):
            mothers = [motherRef(p, i)[1] for i in range(p.numberOfMothers())]
            mother_indices.extend(mothers)
            daughter_indices.extend([ind] * len(mothers))

        # Now add packed genParticles, but filtering out the duplicates
        for ind, p in enumerate(packedGenParticles):
            duplicate = any([compare_gen_particles_close(p, pr) for pr in prunedGenParticles])
            if duplicate:
                continue
            genParticles.append(p)
            # do mother-daughter relationships
            mother = p.mother(0)
            if mother:
                for jnd, prune in enumerate(prunedGenParticles):
                    if mother == prune:
                        mother_indices.append(jnd)
                        daughter_indices.append(len(genParticles)-1)

        event.allGenParticles = genParticles
        event.motherIndices = mother_indices
        event.daughterIndices = daughter_indices

    def process(self, event):
        self.readCollections( event.input )

        # if not MC, nothing to do
        if not self.cfg_comp.isMC: 
            return True
        # do MC level analysis
        self.addMotherDaughterInfo(event)
        return True


import PhysicsTools.HeppyCore.framework.config as cfg
setattr(GenParticleRelationshipAnalyzer, "defaultConfig",
    cfg.Analyzer(GenParticleRelationshipAnalyzer, name="GenParticleRelationshipAnalyzer")
)
