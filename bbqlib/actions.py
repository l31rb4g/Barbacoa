import gtk


class Actions():

    def __init__(self, view):
        pass

    def directory_chooser(self):
        dialog = self.gtk.FileChooserDialog(
            title="Select folder",
            buttons=(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_OPEN, gtk.RESPONSE_OK)
        )
        dialog.set_action(gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER)
        dialog.run()