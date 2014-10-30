import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
        #'/store/relval/CMSSW_7_2_0/RelValZEE_13/GEN-SIM-RECO/PU25ns_PHYS14_25_V1_Phys14-v2/00000/0E49CB8D-9259-E411-8519-0025905A60DA.root',
        #'/store/relval/CMSSW_7_2_0/RelValZEE_13/GEN-SIM-RECO/PU25ns_PHYS14_25_V1_Phys14-v2/00000/52E0373F-9959-E411-9AC8-00259059642E.root',
        #'/store/relval/CMSSW_7_2_0/RelValZEE_13/GEN-SIM-RECO/PU25ns_PHYS14_25_V1_Phys14-v2/00000/B85F9E00-9159-E411-B9CF-0025905B8582.root',
        #'/store/relval/CMSSW_7_2_0/RelValZEE_13/GEN-SIM-RECO/PU25ns_PHYS14_25_V1_Phys14-v2/00000/C8CFAD40-9959-E411-B256-0025905A6064.root',
        #'/store/relval/CMSSW_7_2_0/RelValZEE_13/GEN-SIM-RECO/PU25ns_PHYS14_25_V1_Phys14-v2/00000/C8E873A6-9059-E411-8156-0025905A60D2.root',


        '/store/relval/CMSSW_7_2_0/RelValZEE_13/MINIAODSIM/PU25ns_PHYS14_25_V1_Phys14-v2/00000/665171D5-A359-E411-A74D-0025905A6088.root',
        '/store/relval/CMSSW_7_2_0/RelValZEE_13/MINIAODSIM/PU25ns_PHYS14_25_V1_Phys14-v2/00000/9A52214C-A259-E411-86F5-0025905B8610.root',
        )
)

process.demo = cms.EDAnalyzer('Validation',
                              #isMini = cms.bool(False),
                              #outputFileName = cms.string("aodsim.root")
                              isMini = cms.bool(True),
                              outputFileName = cms.string("miniaodsim.root")
)


process.p = cms.Path(process.demo)
