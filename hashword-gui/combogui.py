#!/usr/bin/python

######################################################################################
# hashword-gui written by: 									
#   Joshua "MrSchism" Embrey [mrschism@sdf.org]					
#   Joseph "Arcarna" Preston [jpreston86@gmail.com]					
# Intial commit: December 2, 2013 							
# Current version: December 4, 2013							
######################################################################################

# Declare imports
import wx # Import wx for GUI elements
import hashlib # Import hashlib for sha2 functionality.

# Create Seed Dialog box
class SeedDialog(wx.Dialog):
    def __init__(self, parent, id=-1, title="hashword"):
        wx.Dialog.__init__(self, parent, id, title, size=(-1, 200))

        self.mainSizer = wx.BoxSizer(wx.VERTICAL) # define mainSizer BoxSizer element
        self.buttonSizer = wx.BoxSizer(wx.HORIZONTAL) # Define buttonSizer BoxSizer element
        self.label = wx.StaticText(self, label="Hashword generator v 1.2 (build 20131207)\nPlease enter your hashword seed.\n\n*NOTE: hashword seeds are case sensitive.*") # Define label StaticText element
        self.label2 = wx.StaticText(self, label="Hashword Seed:") # Define label2 StaticText element
        self.field = wx.TextCtrl(self, value="", size=(300, 20)) # Define field TextCtrl element
        self.okbutton = wx.Button(self, label="Generate", id=wx.ID_OK) # Define okbutton Button element

        self.mainSizer.Add(self.label, 0, wx.ALL, 8 ) # Add Label to mainSizer
        self.mainSizer.Add(self.label2, 0, wx.ALL, 8 ) # Add label2 to mainSizer
        self.mainSizer.Add(self.field, 0, wx.ALL, 8 ) # Add field to mainSizer

        self.buttonSizer.Add(self.okbutton, 0, wx.ALL, 8 ) # Add okbutton to buttonSizer

        self.mainSizer.Add(self.buttonSizer, 0, wx.ALL, 0) # Add buttonSizer to mainSizer

        self.Bind(wx.EVT_BUTTON, self.onOK, id=wx.ID_OK) # Bind "OK" function to ID_OK (ok button)
        self.Bind(wx.EVT_TEXT_ENTER, self.onOK) # Bind OK function to enter key

        self.SetSizer(self.mainSizer) # Set sizer as mainSizer
        self.result = None # set result to none
        
# Define okay and cancel events
    def onOK(self, event): # On OK...
        self.result = self.field.GetValue() # ...make the result the value of the field...
        self.Destroy()  # Then self-destruct window

    def onCancel(self, event): # on cancel (or window close)...
        self.result = None # ...leave the result blank...
        self.Destroy() # Then self-destruct window

# Create initial frame
class Frame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(320, 100))
        
        self.panel = wx.Panel(self) # Define panel as a panel element
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow) # Bind close to close window 
        self.btnShort = wx.Button(self.panel, -1, "Short Hashword") # define btnShort as a button element
        self.Bind(wx.EVT_BUTTON, self.GetShort, self.btnShort) # bind opening GetShort to btnShort
        self.btnLong = wx.Button(self.panel, -1, "Long Hashword") # define btnLong as a button element
        self.Bind(wx.EVT_BUTTON, self.GetLong, self.btnLong) # bind opening GetLong to btnLong
        self.txt = wx.TextCtrl(self.panel, -1, size=(300, -1)) # define txt as a TxtCtrl element
        self.txt.SetValue('') # set txt's value to blank
		
        sizer = wx.BoxSizer(wx.VERTICAL) # define sizer as a BoxSizer element
        sizer.Add(self.btnShort) # add btnShort to sizer
        sizer.Add(self.btnLong) # add btnLong to sizer
        sizer.Add(self.txt) # add txt to sizer

        self.panel.SetSizer(sizer) # set sizer for panel to sizer
        self.Show() # show frame

# Define core function
    def GetShort(self, e):
        dlg = SeedDialog(self) # set dlg as SeedDialog
        dlg.ShowModal() # Show dialog when the OK from SeedDialog is used
        self.txt.SetValue("#" + hashlib.sha256(dlg.result).hexdigest()) # set the value of txt as a hash symbol followed by the sha512 hash of the result of what was input into SeedDialog
    def GetLong(self, e):
		dlg = SeedDialog(self) # set dlg as SeedDialog
		dlg.ShowModal() # Show dialog when the OK from SeedDialog is used
		self.txt.SetValue("#" + hashlib.sha512(dlg.result).hexdigest()) # set the value of txt as a hash symbol followed by the sha512 hash of the result of what was input into SeedDialog
        
# Define exit window
    def OnCloseWindow(self, e):
        self.Destroy() # Self-destruct

# Standard end-application info
app = wx.App() # Define app as an application
frame = Frame(None, 'Hashword Generator') # Define frame with name
app.MainLoop() # Loop the app to keep it open
