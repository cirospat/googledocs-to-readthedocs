
.. _h4a6529483549719b66336a3470283f:

Il lavoro da fare su Github
***************************

Con il metodo proposto in questo tutorial, \ |STYLE0|\  è il seguente.

.. _h67656a17d554b4e5466df117c585e:

Creare il nome del progetto
===========================

Creare il nome del progetto.

E scrivere nel file READ.ME la descrizione di cosa contiene quel progetto.

Il nome del progetto sarà richiamato dal plugin GGeditor, come il repository in cui inviare i Google Doc ai quali lavoreremo. 

.. _h5431481c17334b93c28187b18275111:

Creare un file “conf.py”
========================

Creare un file dandogli il nome “conf.py” e all’interno incollare il seguente codice

=


.. code-block:: python
    :linenos:

    # -*- coding: utf-8 -*-
    
    from __future__ import unicode_literals
    import sys, os
    
    on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
    
    sys.path.append(os.path.abspath(os.pardir))
    
    __version__ = '1.0'
    
    # -- General configuration -----------------------------------------------------
    
    source_suffix = '.rst'
    master_doc = 'index'
    project = 'CHANGE-THIS'
    copyright = '2016, CHANGE-THIS'
    
    # The name of the Pygments (syntax highlighting) style to use.
    pygments_style = 'sphinx'
    
    extlinks = {}
    
    # -- Options for HTML output ---------------------------------------------------
    
    html_theme = 'default'
    
    html_static_path = ['static']
    
    def setup(app):
        # overrides for wide tables in RTD theme
        app.add_stylesheet('theme_overrides.css') # path relative to static
    
    """
      You might want to uncomment the “latex_documents = []” if you use CKJ characters in your document.
      Because the pdflatex raises exception when generate Latex documents with CKJ characters.
    """
    #latex_documents = []
    

Nella pagine del codice sostituire:

* project \ |STYLE1|\  'CHANGE-THIS' al posto di CHANGE-THIS mettere il nome del titolo progetto che si vuole far comparire su Read the Docs;

* copyright \ |STYLE2|\  '2016, CHANGE-THIS' al posto di CHANGE-THIS mettere la licenza che si intende adottare per il rilascio della pubblicazione su Read the Docs.
* 

.. _h31165d707f7077b24286a5e24323a2d:

Finito 
=======

Ecco tutto il lavoro da fare su Github

.. bottom of content


.. |STYLE0| replace:: **l’unico lavoro che c’è da fare sull’account di Github**

.. |STYLE1| replace:: **=**

.. |STYLE2| replace:: **=**
