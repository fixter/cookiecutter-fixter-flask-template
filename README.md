# cookiecutter-fixter-flask-template

A cookiecutter template to set up a Flask web app with foundation, sass, react, and flux for Fixter projects.

## Setting up a project.

Before doing anything with this template you will need to install some tools. This template needs Python 2, nodejs,
npm, bower, and cookiecutter.

Once Python and Pip are intalled just do ```pip install cookiecutter``` to install cookiecutter.

If you aren't using a Jetbrains IDE (i.e. intellij or pycharm) then also install virtualenv. ```pip install virtualenv```

Once all these dependencies are installed, run ```cookiecutter https://github.com/fixter/cookiecutter-fixter-flask-template.git```
in the folder you wish store your application. Cookiecutter will then ask you several questions about the app. It is important
that all the fields you fill out are in the same format as the default values.

Next you have to install all the python libraries, node libraries, and bower libraries.

To install the python libraries:

- If you are using pycharm or intellij, go to settings set up a virtual environment. Then go to the server.py file, where
    pycharm or intellij will ask to install the missing requirements.
- If you aren't using a jetbrains ide then create a python virtual environment on the command line inside the project by
    typing ```virtualenv ENV``` which will create a folder called ENV. I guess you can name your virtual environment whatever you want, but
    for git purposes just use ENV.
    To start using your virtual environment you have to activate it. You do this with ```source ENV/bin/activate```.
    This changes your global path so now you are looking at a vanilla instance of python located in your ENV folder.
    Now any libraries you install will go into this virtual env. To install all the libraries, do ```pip install -r requirements.txt```.
    When you are done using this virtual env you should deactivate it with ```deactivate```
    
Now you should have all the necessary python dependencies.

Next you need to install all the front-end libraries with bower and npm:

- First you should do the node libraries with ```npm install``` inside the folder that contains package.json.
- Then to install bower components run ```bower install``` inside the folder with bower.json.
 

We are almost ready to start developing! 

You now have start your gulp tasks. Gulp will compile scss files and react files for you.

When you are developing you should always run ```npm start``` which runs your gulp tasks. Specifically it runs the react
and sass compilation scripts and then starts to watch scss and react files for changes. If it sees a change it will recompile
*automagically*.

If the watch ever fails or you forget to start the watch, you can always run ```npm build``` to run the sass and react scripts.

We are finally finished setting up the project! To test that everything was built properly run ```python server.py``` and
navigate to http://localhost:5000 and you should see the default page.

Now, have fun developing. Just remember to stay frosty.
    
