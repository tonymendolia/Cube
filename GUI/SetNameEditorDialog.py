from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = lambda s: s
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


class SetNameEditorDialog(QtWidgets.QDialog):
    """
    Largely generated dialog to to edit set names and codes.
    """
    
    #-------------------------------------------------------------------------------
    def __init__(self, parent, mainFrameParent):
        """Additional initializer."""
        
        super(SetNameEditorDialog, self).__init__(parent)
        
        self._mainFrameParent = mainFrameParent
        self._db = self._mainFrameParent.getDatabase()
        self._editedItems = []
        
        self.setupUi(self)

        self.addSetNames(self._db.getMtgSetNames())
        self.applyButton.setEnabled(False)
        self.__connectSignals()
        self.show()
        
#==========================================================================#
#                              Events                                      #
#==========================================================================#

#-------------------------------------------------------------------------------
    def __connectSignals(self):
        """
        Sets up events handling.
        """
        
        self.setNamesTreeWidget.itemChanged.connect(self.__itemEdited)
        self.doneButton.clicked.connect(self.__doneButtonClicked)
        self.cancelButton.clicked.connect(self.__cancelButtonClicked)
        self.applyButton.clicked.connect(self.__applyButtonClicked)

#-------------------------------------------------------------------------------
    def __itemEdited(self, item, column):
        """
        Called when an item is edited
        """
        
        self.applyButton.setEnabled(True)
        
        self._editedItems.append(item)

#-------------------------------------------------------------------------------
    def __doneButtonClicked(self):
        """
        Called when Done button is clicked
        """
        
        self.apply()
        self.close()

#-------------------------------------------------------------------------------
    def __cancelButtonClicked(self):
        """
        Called when Cancel button is clicked. Exits without doing anything.
        """
        
        self.close()

#-------------------------------------------------------------------------------
    def __applyButtonClicked(self):
        """
        Called when Apply button is clicked.
        """
        
        self.apply()
        
        
            
            
#==========================================================================#
#                              Public                                      #
#==========================================================================#

#-------------------------------------------------------------------------------
    def addSetNames(self, setNames):
        """Additional initializer."""
        
        for setName, setCode in setNames.iteritems():
            newItem = QtWidgets.QTreeWidgetItem(self.setNamesTreeWidget)
            newItem.setText(0, setName)
            newItem.setText(1, setCode)
            newItem.setFlags(QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled)
            
            #The original set name and code are stored in the items. These
            #are the values which come straight from the database
            newItem.origMtgSetName = setName
            newItem.origMtgSetCode = setCode
            
            self.setNamesTreeWidget.resizeColumnToContents(0)
            self.setNamesTreeWidget.resizeColumnToContents(1)
            
#-------------------------------------------------------------------------------
    def apply(self):
        """Applies changes."""
        
        for item in self._editedItems:
            origMtgSetName = item.origMtgSetName
            newMtgSetName = str(item.text(0))
            origMtgSetCode = item.origMtgSetCode
            newMtgSetCode = str(item.text(1))
            
            self._db.editSetName(origMtgSetName=origMtgSetName, 
                                 newMtgSetName=newMtgSetName,
                                 origMtgSetCode=origMtgSetCode, 
                                 newMtgSetCode=newMtgSetCode)
            
            self.applyButton.setEnabled(False)
            self._editedItems = []
            
        self._mainFrameParent.saveDatabase(self._db)
        
#==========================================================================#
#                              Generated                                   #
#==========================================================================#
    def setupUi(self, SetNameEditorDialog):
        SetNameEditorDialog.setObjectName(_fromUtf8("SetNameEditorDialog"))
        SetNameEditorDialog.resize(366, 424)
        self.verticalLayout = QtWidgets.QVBoxLayout(SetNameEditorDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.setNamesTreeWidget = QtWidgets.QTreeWidget(SetNameEditorDialog)
        self.setNamesTreeWidget.setAlternatingRowColors(True)
        self.setNamesTreeWidget.setObjectName(_fromUtf8("setNamesTreeWidget"))
        self.setNamesTreeWidget.header().setVisible(True)
        self.verticalLayout.addWidget(self.setNamesTreeWidget)
        self.line = QtWidgets.QFrame(SetNameEditorDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.applyButton = QtWidgets.QPushButton(SetNameEditorDialog)
        self.applyButton.setObjectName(_fromUtf8("applyButton"))
        self.horizontalLayout.addWidget(self.applyButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelButton = QtWidgets.QPushButton(SetNameEditorDialog)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.doneButton = QtWidgets.QPushButton(SetNameEditorDialog)
        self.doneButton.setObjectName(_fromUtf8("doneButton"))
        self.horizontalLayout.addWidget(self.doneButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(SetNameEditorDialog)
        QtCore.QMetaObject.connectSlotsByName(SetNameEditorDialog)

    def retranslateUi(self, SetNameEditorDialog):
        SetNameEditorDialog.setWindowTitle(_translate("SetNameEditorDialog", "Edit set names and codes", None))
        self.setNamesTreeWidget.setSortingEnabled(True)
        self.setNamesTreeWidget.headerItem().setText(0, _translate("SetNameEditorDialog", "Name", None))
        self.setNamesTreeWidget.headerItem().setText(1, _translate("SetNameEditorDialog", "Code", None))
        __sortingEnabled = self.setNamesTreeWidget.isSortingEnabled()
        self.setNamesTreeWidget.setSortingEnabled(True)
        self.setNamesTreeWidget.setSortingEnabled(__sortingEnabled)
        self.applyButton.setText(_translate("SetNameEditorDialog", "Apply", None))
        self.cancelButton.setText(_translate("SetNameEditorDialog", "Cancel", None))
        self.doneButton.setText(_translate("SetNameEditorDialog", "Done", None))


