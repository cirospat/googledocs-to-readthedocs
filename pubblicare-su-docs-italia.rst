
.. _h747d28468046343a107a754c621e3b0:

Pubblicare con il design di Docs Italia
#######################################

Se una Pubblica Amministrazione vuole sfruttare il servizio del componente aggiuntivo di Google doc, GGeditor, per pubblicare un documento su Read the Docs ma con il design di \ |LINK1|\  ecco alcune cose da tenere in considerazione al fine di non commettere errori che - alla fine - potrebbero non fare compilare la costruzione (build) del documento su Read the Docs e quindi pregiudicare la visualizzazione delle pagine HTML.

|

.. _h639194313702264d773f76407a5175:

Uso corretto degli apici e doppi apici nel file ‘conf.py’
*********************************************************

Nel file ``conf.py`` che si trova nel repo di Github, i doppi apici (“) vanno solo nel primo campo:

.. code:: 

    settings_project_name = "Nome progetto"

Nel resto dei settings vanno solo i singoli apici (‘).

Su ``setting_doc_version`` e su ``setting_doc_release`` va la dicitura  ``’version: latest’`` (dentro apici singoli).


.. code:: 

    settings_copyright_copyleft = 'Comune di ...'
    settings_editor_name = 'Comune di ...'
    settings_doc_version = 'version: latest'
    settings_doc_release = 'version: latest'
    settings_basename = 'nome_progetto'
    settings_file_name = 'nome_progetto'

|

.. _h7c46341e76355a731f401733c315462:

Uso corretto dei titoli dei file Google doc dentro il toctree del file index
****************************************************************************

Nell'editing del nome dei file dei capitoli sul toctree, nel Google doc dell'index, deve essere inserito il suffisso ``.rst``. Senza l’aggiunta del suffisso sulla pagina ‘index’ del progetto Read the Docs non comparirà la struttura dell’indice.

Nel caso della pubblicazione su Read the Docs \ |STYLE0|\ , (\ |STYLE1|\ ) l’assenza di  questo suffisso ``.rst`` per ogni file nel toctree del file ‘index’ non costituisce un problema e l’indice viene visualizzato ugualmente.

|

.. _h1573c382a5663265f406c5380716d:

HTML Logo
*********

Sui documenti pubblicati con il design Docs Italia non c’è la possibilità di fare visualizzare un logo/immagine in alto a sinistra come, invece, avviene con la versione Read the Docs basic.

Quindi l’istruzione 

.. code:: 

    html_logo = "images/logo.png"

non deve essere data in questo caso. Se viene data la compilazione su Read the Docs fallisce.

|

.. _h552735384b632f4a3983f297514485:

Un progetto da clonare per la pubblicazione con il design Docs Italia
*********************************************************************

A titolo di \ |LINK2|\ , da clonare su Github, per un esigenza di un nuovo progetto di pubblicazione con il design Docs Italia, può essere usato questo repo: \ |LINK3|\  dove sono stati effettuati i dovuti controlli nel file ``conf.py`` che permette un esatta compilazione su Read the Docs, ottenendo lo status verde di passed \ |LINK4|\ . 


.. bottom of content


.. |STYLE0| replace:: **versione basic**

.. |STYLE1| replace:: **cioè senza il design Docs Italia elaborato dal Team Digitale per i documenti della PA**


.. |LINK1| raw:: html

    <a href="http://guida-docs-italia.readthedocs.io/it/latest/" target="_blank">Docs Italia (elaborato dal Team Digitale per  le pubblicazioni della PA)</a>

.. |LINK2| raw:: html

    <a href="http://joppy.readthedocs.io" target="_blank">progetto tipo</a>

.. |LINK3| raw:: html

    <a href="https://github.com/cirospat/joppy" target="_blank">https://github.com/cirospat/joppy</a>

.. |LINK4| raw:: html

    <a href="https://readthedocs.org/projects/joppy/" target="_blank">https://readthedocs.org/projects/joppy/</a>

