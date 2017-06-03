import gtk
from sugar.graphics.alert import TimeoutAlert

window = gtk.Window()

box = gtk.VBox()
window.add(box)

def _timeout_alert_response_cb(alert, response_id):
    if response_id is gtk.RESPONSE_OK:
        print 'Ok or Timeout'
    elif response_id is gtk.RESPONSE_CANCEL:
        print 'Cancel'
    box.remove(alert)
    gtk.main_quit()

alert = TimeoutAlert(10)
alert.props.title='Title of TimeoutAlert'
alert.props.msg = 'Text of timeout alert, either button will quit'
alert.connect('response', _timeout_alert_response_cb)
box.add(alert)

window.show_all()

gtk.main()
