Color palette from image
------------------------
These are some experiments to find an appropriate pastel color from an image.  

This app uses [Pillow](https://python-pillow.org/) - a fork from PIL (Python Imaging Library).  
This app also uses [Flask](http://flask.pocoo.org/) to preview the images + background colors.  


### How to install
Add a bunch of images to the `static/img` folder.  
Start the app by installing Flask + Pillow into a virtual environment.  

```bash
# if you dont have virtualenv (I use pip3 for python3 packages)
$ pip3 install virtualenv

# cd into root (not app folder) then create virtual env
$ virtualenv venv

# activate virtual environment 
$ source venv/bin/activate

# Install Flask + Pillow (etc.) from requirements file
$ pip3 install -r requirements.txt

# Run the app
$ cd app && python3 __init__.py

# When you are done working in virtual env deactivate it from root folder
$ cd ../
$ deactivate
```
