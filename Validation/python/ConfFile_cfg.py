import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
        #'/store/relval/CMSSW_7_4_3/RelValZEE_13/MINIAODSIM/PU50ns_MCRUN2_74_V8-v11/00000/B81FC72C-3C07-E511-B2BA-0025905A607A.root',
        #'/store/relval/CMSSW_7_4_3/RelValZEE_13/MINIAODSIM/PU50ns_MCRUN2_74_V8-v11/00000/D25E113E-3C07-E511-832F-0025905B85EE.root',

        '/store/relval/CMSSW_7_4_3/RelValZEE_13/GEN-SIM-RECO/PU50ns_MCRUN2_74_V8-v11/00000/309E4BC9-3807-E511-9B2B-0025905A48D0.root',
        '/store/relval/CMSSW_7_4_3/RelValZEE_13/GEN-SIM-RECO/PU50ns_MCRUN2_74_V8-v11/00000/685B87C6-D306-E511-9F00-0025905A497A.root',
        '/store/relval/CMSSW_7_4_3/RelValZEE_13/GEN-SIM-RECO/PU50ns_MCRUN2_74_V8-v11/00000/7035570D-2107-E511-ACC0-003048FFCC0A.root',
        '/store/relval/CMSSW_7_4_3/RelValZEE_13/GEN-SIM-RECO/PU50ns_MCRUN2_74_V8-v11/00000/981C953F-CF06-E511-84BD-003048FFD79C.root',
        '/store/relval/CMSSW_7_4_3/RelValZEE_13/GEN-SIM-RECO/PU50ns_MCRUN2_74_V8-v11/00000/9A612ED7-2407-E511-B089-0025905B85AA.root',
        )
                            )

process.demo = cms.EDAnalyzer('Validation',
                              outputFileName = cms.string("test.root"),
                              electrons = cms.InputTag("gedGsfElectrons")
)


process.p = cms.Path(process.demo)
