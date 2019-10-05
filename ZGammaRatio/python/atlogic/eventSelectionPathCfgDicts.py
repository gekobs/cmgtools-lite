# Misc
isMC   = "ev: ev.isData[0] == 0"
isData = "ev: ev.isData[0] == 1"

# PDs
PD_MET            = "ev : ev.PrimaryDataset[0] == 'MET'"
PD_HTMHT          = "ev : ev.PrimaryDataset[0] == 'HTMHT'"
PD_JetHT          = "ev : ev.PrimaryDataset[0] == 'JetHT'"
PD_SingleElectron = "ev : ev.PrimaryDataset[0] == 'SingleElectron'"
PD_SingleMuon     = "ev : ev.PrimaryDataset[0] == 'SingleMuon'"
PD_SinglePhoton   = "ev : ev.PrimaryDataset[0] == 'SinglePhoton'"
PD_DoubleEG       = "ev : ev.PrimaryDataset[0] == 'DoubleEG'"

# Cutflows
nMuonsVeto          = "ev: ev.nMuonsVeto[0] {}"
nElectronsVeto      = "ev: ev.nElectronsVeto[0] {}"
nPhotonsVeto        = "ev: ev.nPhotonsVeto[0] {}"
nMuonsSelection     = "ev: ev.nMuonsSelection[0] {}"
nElectronsSelection = "ev: ev.nElectronsSelection[0] {}"
nPhotonsSelection   = "ev: ev.nPhotonsSelection[0] {}"

# No vetoes
cutflow_Signal       = dict(All = (
    nMuonsVeto         .format("== 0"),
    nElectronsVeto     .format("== 0"),
    nPhotonsVeto       .format("== 0"),
    ),)
cutflow_SingleMu     = dict(All = (
    nMuonsSelection    .format(">= 1"),
    #nElectronsVeto     .format("== 0"),
    #nPhotonsVeto       .format("== 0"),
    ),)
cutflow_DoubleMu     = dict(All = (
    nMuonsSelection    .format(">= 2"),
    #nElectronsVeto     .format("== 0"),
    #nPhotonsVeto       .format("== 0"),
    ),)
cutflow_SingleEle    = dict(All = (
    #nMuonsVeto         .format("== 0"),
    nElectronsSelection.format(">= 1"),
    #nPhotonsVeto       .format("== 0"),
    ),)
cutflow_DoubleEle    = dict(All = (
    #nMuonsVeto         .format("== 0"),
    nElectronsSelection.format(">= 2"),
    #nPhotonsVeto       .format("== 0"),
    ),)
cutflow_SinglePhoton = dict(All = (
    #nMuonsVeto         .format("== 0"),
    #nElectronsVeto     .format("== 0"),
    nPhotonsSelection  .format(">= 1"),
    ),)
cutflow_SingleMuEle  = dict(All = (
    nMuonsSelection    .format(">= 1"),
    nElectronsSelection.format(">= 1"),
    #nPhotonsVeto       .format("== 0"),
    ),)

##__________________________________________________________________||
event_selection_path_cfg_tree_production = dict(All = (
    'ev: ev.nJet100JECUp[0] >= 1',
    dict(Any = (
        isMC,
        dict(All = (
            isData,
            dict(Any = (
                dict(All = (
                    PD_SingleMuon,
                    dict(Any = (
                        cutflow_DoubleMu,
                        cutflow_SingleMuEle,
                    )),
                )),
                dict(All = (
                    PD_SingleElectron,
                    dict(Any = (
                        cutflow_DoubleEle,
                        cutflow_SingleMuEle,
                    )),
                )),
                dict(All = (
                    PD_SinglePhoton,
                    cutflow_SinglePhoton
                )),
                dict(All = (
                    PD_DoubleEG,
                    cutflow_SinglePhoton,
                )),
            )),
        )),
    )),
    dict(Any = (
        cutflow_DoubleMu,
        cutflow_SingleMuEle,
        cutflow_DoubleEle,
        cutflow_SinglePhoton,
    )),
))
