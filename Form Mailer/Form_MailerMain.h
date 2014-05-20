/***************************************************************
 * Name:      Form_MailerMain.h
 * Purpose:   Defines Application Frame
 * Author:    CSDT (chris@csdteam.com)
 * Created:   2011-08-21
 * Copyright: CSDT (csdteam.com)
 * License:
 **************************************************************/

#ifndef FORM_MAILERMAIN_H
#define FORM_MAILERMAIN_H

//(*Headers(Form_MailerDialog)
#include <wx/sizer.h>
#include <wx/stattext.h>
#include <wx/statline.h>
#include <wx/button.h>
#include <wx/dialog.h>
//*)

class Form_MailerDialog: public wxDialog
{
    public:

        Form_MailerDialog(wxWindow* parent,wxWindowID id = -1);
        virtual ~Form_MailerDialog();

    private:

        //(*Handlers(Form_MailerDialog)
        void OnQuit(wxCommandEvent& event);
        void OnAbout(wxCommandEvent& event);
        void OnButton3Click(wxCommandEvent& event);
        //*)

        //(*Identifiers(Form_MailerDialog)
        static const long ID_STATICTEXT1;
        static const long ID_BUTTON1;
        static const long ID_STATICLINE1;
        static const long ID_BUTTON2;
        //*)

        //(*Declarations(Form_MailerDialog)
        wxButton* Button1;
        wxStaticText* StaticText1;
        wxBoxSizer* BoxSizer2;
        wxButton* Button2;
        wxStaticLine* StaticLine1;
        wxBoxSizer* BoxSizer1;
        //*)

        DECLARE_EVENT_TABLE()
};

#endif // FORM_MAILERMAIN_H
