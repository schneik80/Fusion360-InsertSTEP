#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback
import os.path

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        # Check a Design document is active.
        if not design:
            ui.messageBox('No active Fusion design', 'No Design')
            return

        msg = ''
        # Set styles of file dialog.
        fileDlg = ui.createFileDialog()
        fileDlg.isMultiSelectEnabled = False
        fileDlg.title = 'Fusion Insert STEP'
        fileDlg.filter = '*.stp, *.step'

        # Show file open dialog
        dlgResult = fileDlg.showOpen()
        if dlgResult == adsk.core.DialogResults.DialogOK:
            msg += '\nFiles to Open:'
            for filename in fileDlg.filenames:
                msg += '\n\t{}'.format(filename)
        else:
            return  
        
        adsk.core.Application.log(f'{msg}')

        filename = '"' + filename + '"'
        
        command = f'Fusion.ImportComponent {filename}'

        app.executeTextCommand(command)



    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
