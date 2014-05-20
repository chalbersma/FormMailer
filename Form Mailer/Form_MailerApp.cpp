/***************************************************************
 * Name:      Form_MailerApp.cpp
 * Purpose:   Code for Application Class
 * Author:    CSDT (chris@csdteam.com)
 * Created:   2011-08-21
 * Copyright: CSDT (csdteam.com)
 * License:
 **************************************************************/

#include "Form_MailerApp.h"

//(*AppHeaders
#include "Form_MailerMain.h"
#include <wx/image.h>
//*)

IMPLEMENT_APP(Form_MailerApp);

bool Form_MailerApp::OnInit()
{
    //(*AppInitialize
    bool wxsOK = true;
    wxInitAllImageHandlers();
    if ( wxsOK )
    {
    	Form_MailerDialog Dlg(0);
    	SetTopWindow(&Dlg);
    	Dlg.ShowModal();
    	wxsOK = false;
    }
    //*)
    return wxsOK;

}
