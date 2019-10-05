from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.HeppyCore.framework.event import Event

##__________________________________________________________________||
class AtEventAttributesPost(Analyzer):
    def process(self, event):
        self.readCollections( event.input )

        attrs_to_move = [
            'cutflowId',
            'bintypeId', 'bintypeIdJECUp', 'bintypeIdJECDown',
            'nVert',
            'nMuonsVeto', 'nElectronsVeto', 'nElectronsLoose', 'nPhotonsVeto',
            'nMuonsSelection', 'nElectronsSelection', 'nPhotonsSelection',
            'nIsoTracksVeto', 'nIsoTracksNoMuVeto', 'nIsoTracksNoEleVeto', 'nIsoTracksNoMuEleVeto',
            # 'nJet40failedId',
            'nJet40', 'nJet100', 'nBJet40',
            'nJet40JECUp', 'nJet100JECUp', 'nBJet40JECUp',
            'nJet40JECDown', 'nJet100JECDown', 'nBJet40JECDown',
            'mht40_pt', 'mht40JECUp_pt', 'mht40JECDown_pt',
            'ht40', 'ht40JECUp', 'ht40JECDown',
            'nJet40Fwd', 'nJet40FwdJECUp', 'nJet40FwdJECDown',
            'mtw', 'mll',
            'minDelRJetMu', 'minDelRJetMuJECUp', 'minDelRJetMuJECDown',
            'minDelRJetEle', 'minDelRJetEleJECUp', 'minDelRJetEleJECDown',
            'minDelRJetPhoton', 'minDelRJetPhotonJECUp', 'minDelRJetPhotonJECDown',
            ###
            'Flag_HBHENoiseFilter',
            'Flag_HBHENoiseIsoFilter',
            'Flag_EcalDeadCellTriggerPrimitiveFilter',
            'Flag_goodVertices',
            'Flag_eeBadScFilter',
            'Flag_globalTightHalo2016Filter',
            ]

        if self.cfg_comp.isMC:
            attrs_to_move.extend([
                'lheHTnoT', 'nLheElectrons', 'nLheMuons', 'nLheTaus',
            ])

        if self.cfg_ana.metnohf:
            attrs_to_move.extend([
                'mtwNoHF',
            ])

        for name in set(attrs_to_move):
            val = getattr(event, name)
            if len(val) == 0: val = [-999.]
            else: val = val[0]
            if hasattr(val, 'item'): val = val.item() # e.g., convert numpy.float64 to python float
            setattr(event, name, val)

##__________________________________________________________________||
