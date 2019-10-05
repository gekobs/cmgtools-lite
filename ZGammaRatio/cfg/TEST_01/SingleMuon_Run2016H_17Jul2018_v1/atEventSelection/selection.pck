ccopy_reg
_reconstructor
p0
(cCMGTools.ZGammaRatio.analyzers.AtEventSelectionRunner
str_ignore_add
p1
c__builtin__
str
p2
S"<:EventSelectionAll>\n  <:LambdaStr> ev: ev.nJet100JECUp[0] >= 1\n  <:EventSelectionAny>\n    <:LambdaStr> ev: ev.isData[0] == 0\n    <:EventSelectionAll>\n      <:LambdaStr> ev: ev.isData[0] == 1\n      <:EventSelectionAny>\n        <:EventSelectionAll>\n          <:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleMuon'\n          <:EventSelectionAny>\n            <:EventSelectionAll>\n              <:LambdaStr> ev: ev.nMuonsSelection[0] >= 2\n            <:EventSelectionAll>\n              <:LambdaStr> ev: ev.nMuonsSelection[0] >= 1\n              <:LambdaStr> ev: ev.nElectronsSelection[0] >= 1\n        <:EventSelectionAll>\n          <:LambdaStr> ev : ev.PrimaryDataset[0] == 'SingleElectron'\n          <:EventSelectionAny>\n            <:EventSelectionAll>\n              <:LambdaStr> ev: ev.nElectronsSelection[0] >= 2\n            <:EventSelectionAll>\n              <:LambdaStr> ev: ev.nMuonsSelection[0] >= 1\n              <:LambdaStr> ev: ev.nElectronsSelection[0] >= 1\n        <:EventSelectionAll>\n          <:LambdaStr> ev : ev.PrimaryDataset[0] == 'SinglePhoton'\n          <:EventSelectionAll>\n            <:LambdaStr> ev: ev.nPhotonsSelection[0] >= 1\n        <:EventSelectionAll>\n          <:LambdaStr> ev : ev.PrimaryDataset[0] == 'DoubleEG'\n          <:EventSelectionAll>\n            <:LambdaStr> ev: ev.nPhotonsSelection[0] >= 1\n  <:EventSelectionAny>\n    <:EventSelectionAll>\n      <:LambdaStr> ev: ev.nMuonsSelection[0] >= 2\n    <:EventSelectionAll>\n      <:LambdaStr> ev: ev.nMuonsSelection[0] >= 1\n      <:LambdaStr> ev: ev.nElectronsSelection[0] >= 1\n    <:EventSelectionAll>\n      <:LambdaStr> ev: ev.nElectronsSelection[0] >= 2\n    <:EventSelectionAll>\n      <:LambdaStr> ev: ev.nPhotonsSelection[0] >= 1\n"
p3
tp4
Rp5
.