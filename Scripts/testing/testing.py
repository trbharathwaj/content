import demistomock as demisto
from CommonServerPython import *
mails = []
MAIL_CONTEXT_KEY = "Mailboxes"

attrs = 'mail'
filterstr = r"(&(objectClass=User))"
if isError(resp[0]):
    demisto.results(resp)
else:
    data = demisto.get(resp[0], "Contents")
    for item in data:
        mails += [item["mail"]] if item["mail"] else []

    demisto.setContext(MAIL_CONTEXT_KEY, ",".join(mails))
