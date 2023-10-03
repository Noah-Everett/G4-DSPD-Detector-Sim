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

#ifndef OutputManager_h
#define OutputManager_h

#include "globals.hh"
#include "G4AnalysisManager.hh"
#include "G4Step.hh"
#include "G4VProcess.hh"

#include "OutputMessenger.hh"
#include "ConstructionMessenger.hh"

#include <map>

using std::map;

class OutputManager
{
    public:
        static OutputManager* get_instance   ();
        static void           delete_instance();

        void add_histogram_1D( G4String, G4String, G4int, G4double, G4double );
        void add_histogram_2D( G4String, G4String, G4int, G4double, G4double, G4int, G4double, G4double );
        void add_tuple_initialize    ( G4String, G4String );
        void add_tuple_finalize      ();
        void add_tuple_column_intiger( G4String );
        void add_tuple_column_double ( G4String );
        void add_tuple_column_3vector( G4String );
        void add_tuple_column_string ( G4String );
        void add_tuple_column_boolean( G4String );
        
        void save_step( const G4Step* );

        G4int get_histogram_1D_id( G4String );
        G4int get_histogram_2D_id( G4String );
        G4int get_tuple_id       ( G4String );

        void make_histogram_photoSensor_hits( G4String );
        void make_tuple_photoSensor_hits    ();
        void make_tuple_primary             ();
        void make_tuple_photon              ();
        
        void save_step_photoSensor_hits( const G4Step*, G4String, G4ThreeVector, G4RotationMatrix, G4bool );
        void save_step_primary         ( const G4Step* );
        void save_step_photon          ( const G4Step* );

        void reset();

    private:
                 OutputManager();
        virtual ~OutputManager();

        OutputMessenger      * m_outputMessenger{ OutputMessenger  ::get_instance() };
        ConstructionMessenger* m_constructionMessenger{ ConstructionMessenger::get_instance() };
        G4AnalysisManager    * m_analysisManager{ G4AnalysisManager::Instance    () };

        G4int m_index_histogram{ 0 };
        G4int m_index_tuple    { 0 };
        G4int m_index_column   { 0 };

        map< G4String, G4int > m_histogram_1D_id;
        map< G4String, G4int > m_histogram_2D_id;
        map< G4String, G4int > m_tuple_id;

    protected:
        static OutputManager* m_instance;
};

#endif