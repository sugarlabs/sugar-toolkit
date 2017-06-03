import gtk
from sugar.graphics.alert import ConfirmationAlert

window = gtk.Window()

box = gtk.VBox()
window.add(box)

def _alert_response_cb(alert, response_id, entry):
    print entry.get_text()
    if response_id is gtk.RESPONSE_OK:
        print 'Ok'
    elif response_id is gtk.RESPONSE_CANCEL:
        print 'Cancel'
    box.remove(alert)
    gtk.main_quit()

alert = ConfirmationAlert()
alert.props.title='Title of ConfirmationAlert'
alert.props.msg = 'Text of confirmation alert, either button will quit'
box.add(alert)
entry = alert.add_entry()
entry.set_text('this entry')
alert.connect('response', _alert_response_cb, entry)

window.show_all()

gtk.main()
