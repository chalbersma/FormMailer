/***************************************************************
 * Name:      Form_LetterMain.h
 * Purpose:   Defines Application Frame
 * Author:    CSDT (chris@csdteam.com)
 * Created:   2011-08-28
 * Copyright: CSDT (csdteam.com)
 * License:
 **************************************************************/

#ifndef FORM_LETTERMAIN_H
#define FORM_LETTERMAIN_H

//(*Headers(Form_LetterFrame)
#include <wx/menu.h>
#include <wx/frame.h>
#include <wx/statusbr.h>
//*)

class Form_LetterFrame: public wxFrame
{
    public:

        Form_LetterFrame(wxWindow* parent,wxWindowID id = -1);
        virtual ~Form_LetterFrame();

    private:

        //(*Handlers(Form_LetterFrame)
        void OnQuit(wxCommandEvent& event);
        void OnAbout(wxCommandEvent& event);
        void OnTextCtrl1Text(wxCommandEvent& event);
        //*)

        //(*Identifiers(Form_LetterFrame)
        static const long idMenuQuit;
        static const long idMenuAbout;
        static const long ID_STATUSBAR1;
        //*)

        //(*Declarations(Form_LetterFrame)
        wxStatusBar* StatusBar1;
        //*)

        DECLARE_EVENT_TABLE()
};

#endif // FORM_LETTERMAIN_H
