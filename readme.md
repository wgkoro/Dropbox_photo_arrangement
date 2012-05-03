## This script helps to arrange photos in Dropbox/Camera Uploads

This script replaces photos in Dropbox like 'Dropbox/Camera Uploads/year/month/day/201x-05-03 xx.xx.xx.jpg'.

### Requirement

Python 2.5 < 3.x

### How to use

#### For Windows Users

If you have'nt install python yet,
you can download 'Python 2.7.3' windows installer from [http://www.python.org/download/releases/2.7.3/](http://www.python.org/download/releases/2.7.3/).

Put 'arrangement.py', 'win.bat', 'win_test.bat' to 'Camera Uploads' directory.

Camera Uploads
├── arrangement.py
├── win.bat
└── win_test.bat

#### For Mac Users

Put 'arrangement.py', 'mac.command', 'mac_test.command' to 'Camera Uploads' directory.

Camera Uploads
├── arrangement.py
├── mac.command
└── mac_test.command

#### Run test script

Run test script by double click 'win_test.bat' or 'mac_test.command'.  
Copying file will be started.  
The test script won't delete original photos.

#### If the test script works fine

You can remove test script('win_test.bat' or 'mac_test.command').  
Run 'win.bat' or 'mac.command'.  
This script copies photo to 'Camera Uploads/year/month/day' directory,  
and remove file in top directory in 'Camera Uploads'.

#### Other scripts?

Scripts 'win_nodate.bat', 'mac_nodate.command' don't create 'date' directory.  
So, photos will be placed to 'Camera Uploads/year/month/xxxx.jpg'.

If you don't want to create 'date' directory, please use 'xxx_nodate' script.
