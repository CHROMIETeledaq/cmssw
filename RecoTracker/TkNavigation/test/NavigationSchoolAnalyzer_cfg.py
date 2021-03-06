import FWCore.ParameterSet.Config as cms

# set the geometry and the GlobalTag

process = cms.Process("NavigationSchoolAnalyze")

# process.load("Configuration.StandardSequences.Geometry_cff")
#process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
#process.load('Configuration.Geometry.GeometryExtended2023D1Reco_cff')
#process.load('Configuration.Geometry.GeometryExtended2023D4Reco_cff')
process.load('Geometry.PixelTelescope.PixelTelescopeRecoGeometry_cfi')
process.load('Configuration.StandardSequences.MagneticField_0T_cff')

#process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic', '')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2017_realistic', '')
# process.load("Configuration.StandardSequences.MagneticField_cff")
#process.load("RecoTracker.TkNavigation.NavigationSchoolESProducer_cff")
process.load('RecoTracker.TkNavigation.TelescopeNavigationSchoolESProducer_cfi')

#process.MessageLogger = cms.Service("MessageLogger",
#    destinations = cms.untracked.vstring('detailedInfo')
#)

#process.Tracer = cms.Service("Tracer",
#    indentation = cms.untracked.string('$$')
#)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("EmptySource")

process.navigationSchoolAnalyzer = cms.EDAnalyzer("NavigationSchoolAnalyzer",
#    navigationSchoolName = cms.string('BeamHaloNavigationSchool')
#    navigationSchoolName = cms.string('CosmicNavigationSchool')
    navigationSchoolName = cms.string('TelescopeNavigationSchool')
)

#process.muonNavigationTest = cms.EDAnalyzer("MuonNavigationTest")


process.p = cms.Path(process.navigationSchoolAnalyzer)


