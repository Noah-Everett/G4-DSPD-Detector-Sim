//
// ********************************************************************
// * License and Disclaimer                                           *
// *                                                                  *
// * The  Geant4 software  is  copyright of the Copyright Holders  of *
// * the Geant4 Collaboration.  It is provided  under  the terms  and *
// * conditions of the Geant4 Software License,  included in the file *
// * LICENSE and available at  http://cern.ch/geant4/license .  These *
// * include a list of copyright holders.                             *
// *                                                                  *
// * Neither the authors of this software system, nor their employing *
// * institutes,nor the agencies providing financial support for this *
// * work  make  any representation or  warranty, express or implied, *
// * regarding  this  software system or assume any liability for its *
// * use.  Please see the license in the file  LICENSE  and URL above *
// * for the full disclaimer and the limitation of liability.         *
// *                                                                  *
// * This  code  implementation is the result of  the  scientific and *
// * technical work of the GEANT4 collaboration.                      *
// * By using,  copying,  modifying or  distributing the software (or *
// * any work based  on the software)  you  agree  to acknowledge its *
// * use  in  resulting  scientific  publications,  and indicate your *
// * acceptance of all terms of the Geant4 Software license.          *
// ********************************************************************

#include "RunAction.hh"

RunAction::RunAction() {
}

RunAction::~RunAction() {
    m_outputManager->delete_instance();
}

void RunAction::BeginOfRunAction(const G4Run*) {
    m_analysisManager = G4AnalysisManager::Instance();
    m_analysisManager->SetDefaultFileType( "root" );
    m_analysisManager->SetFileName( m_outputMessenger->get_fileName() );
    m_analysisManager->SetVerboseLevel( 1 );
    m_analysisManager->SetActivation( true );
    m_analysisManager->OpenFile();

    m_outputManager->make_histograms();
    m_outputManager->make_tuples();
}

void RunAction::EndOfRunAction(const G4Run* run) {
    m_analysisManager = G4AnalysisManager::Instance();
    G4cout << "DELETING OUTPUTMANAGER" << G4endl;
    G4cout << "HERE 1" << G4endl;
    m_analysisManager->Write();
    G4cout << "HERE 1" << G4endl;
    m_analysisManager->CloseFile();
    G4cout << "HERE 1" << G4endl;
}