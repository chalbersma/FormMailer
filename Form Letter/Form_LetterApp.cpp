/***************************************************************
 * Name:      Form_LetterApp.cpp
 * Purpose:   Code for Application Class
 * Author:    CSDT (chris@csdteam.com)
 * Created:   2011-08-28
 * Copyright: CSDT (csdteam.com)
 * License:
 **************************************************************/

#include "Form_LetterApp.h"

//(*AppHeaders
#include "Form_LetterMain.h"
#include <wx/image.h>
//*)

IMPLEMENT_APP(Form_LetterApp);

bool Form_LetterApp::OnInit()
{
    //(*AppInitialize
    bool wxsOK = true;
    wxInitAllImageHandlers();
    if ( wxsOK )
    {
    	Form_LetterFrame* Frame = new Form_LetterFrame(0);
    	Frame->Show();
    	SetTopWindow(Frame);
    }
    //*)
    return wxsOK;

}
