How to start Sphinx on Windows
==============================

#. Check if 'Python' >3.3, 'pip' and 'venv' are installed
#. run 'python -m venv <name-of-the-venv>'
#. Depending on the OS and terminal, activate the venv:

  #. On PowerShell run: '<name-of-the-venv>\Scripts\Activate.ps1'
  #. On CMD run: '<name-of-the-venv>\Scripts\Activate.bat'
  #. On Ubuntu run: 'source <name-of-the-venv>\bin\activate'

#. run 'pip install sphinx'
#. run 'sphinx-quickstart docs'

  #. Separate source and build directories? (y/n): y
  #. Project name: <your-project-name>
  #. Author name(s): <author-name(s)>
  #. Project release: 0.1 (actually any number, could be 0.0.1)
  #. Project language [en]: 'en' by default

#. change/update some stuff on config.py

.. autosummary::
   :toctree: generated

   main
   classes
   myFunction


