// -*- C++ -*-
//
// Package:    MiniAOD/Validation
// Class:      Validation
// 
/**\class Validation Validation.cc MiniAOD/Validation/plugins/Validation.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Matteo Sani
//         Created:  Thu, 30 Oct 2014 12:46:57 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectronFwd.h"
#include "DataFormats/PatCandidates/interface/Electron.h"

#include "TFile.h"
#include "TH1F.h"

#include <string>
#include <map>

class Validation : public edm::EDAnalyzer {
public:
  explicit Validation(const edm::ParameterSet&);
  ~Validation();
  
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
  
private:
  virtual void beginJob() override;
  virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
  virtual void endJob() override;
  
  std::map<std::string, TH1F*> plots;
  bool isMini;
  std::string outputFileName;
};

Validation::Validation(const edm::ParameterSet& iConfig) {

  isMini = iConfig.getParameter<bool>("isMini");
  outputFileName = iConfig.getParameter<std::string>("outputFileName");

  plots.insert(std::make_pair("pt", new TH1F("pt",       "", 100, 0, 100)));
  plots.insert(std::make_pair("et", new TH1F("et",       "", 100, 0, 100)));
  plots.insert(std::make_pair("eta", new TH1F("eta",     "", 50, -2.5, 2.5)));
  plots.insert(std::make_pair("sieie", new TH1F("sieie", "", 100, 0, 0.05)));
  plots.insert(std::make_pair("fbrem", new TH1F("fbrem", "", 100, 0, 1)));
  plots.insert(std::make_pair("deta", new TH1F("deta",   "", 100, -0.05, 0.05)));
  plots.insert(std::make_pair("dphi", new TH1F("dphi",   "", 100, -0.1, 0.1)));
  plots.insert(std::make_pair("eop", new TH1F("eop",     "", 100,  0.0, 5)));
}


Validation::~Validation() {

  TFile* file = new TFile(outputFileName.c_str(), "recreate");
  for(auto iterator = plots.begin(); iterator != plots.end(); iterator++)
    iterator->second->Write();
  file->Close();
}

void Validation::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {

  if (!isMini) {
    edm::Handle<reco::GsfElectronCollection> elH;
    iEvent.getByLabel("gedGsfElectrons", elH);
    
    for (unsigned int i=0; i<elH->size(); i++) {
      reco::GsfElectronRef e(elH, i);
      
      plots["pt"]->Fill(e->pt());
      plots["et"]->Fill(e->superCluster()->energy()/cosh(e->superCluster()->eta()));
      plots["eta"]->Fill(e->superCluster()->eta());
      plots["sieie"]->Fill(e->full5x5_sigmaIetaIeta());
      plots["fbrem"]->Fill(e->fbrem());
      plots["deta"]->Fill(e->deltaEtaSuperClusterTrackAtVtx());
      plots["dphi"]->Fill(e->deltaPhiSuperClusterTrackAtVtx());
      plots["eop"]->Fill(e->eSuperClusterOverP());
    }
  } else {

    edm::Handle<pat::ElectronCollection> elH;
    iEvent.getByLabel("slimmedElectrons", elH);
    
    for (unsigned int i=0; i<elH->size(); i++) {
      pat::ElectronRef e(elH, i);
      
      plots["pt"]->Fill(e->pt());
      plots["et"]->Fill(e->superCluster()->energy()/cosh(e->superCluster()->eta()));
      plots["eta"]->Fill(e->superCluster()->eta());
      plots["sieie"]->Fill(e->full5x5_sigmaIetaIeta());
      plots["fbrem"]->Fill(e->fbrem());
      plots["deta"]->Fill(e->deltaEtaSuperClusterTrackAtVtx());
      plots["dphi"]->Fill(e->deltaPhiSuperClusterTrackAtVtx());
      plots["eop"]->Fill(e->eSuperClusterOverP());
    }
  }
}


void Validation::beginJob()
{}

void Validation::endJob() 
{}

void Validation::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

DEFINE_FWK_MODULE(Validation);
