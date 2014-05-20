/***************************************************************
 * Name:      Form_MailerApp.h
 * Purpose:   Defines Application Class
 * Author:    CSDT (chris@csdteam.com)
 * Created:   2011-08-21
 * Copyright: CSDT (csdteam.com)
 * License:
 **************************************************************/

#ifndef FORM_MAILERAPP_H
#define FORM_MAILERAPP_H

#include <wx/app.h>

class Form_MailerApp : public wxApp
{
    public:
        virtual bool OnInit();
};

#endif // FORM_MAILERAPP_H
