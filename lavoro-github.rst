
.. _h4a6529483549719b66336a3470283f:

Il lavoro da fare su Github
***************************

Con il metodo proposto in questo tutorial, \ |STYLE0|\  è il seguente.

|

.. _h27d37777d6f59f417f254b4fa3a:

1. Creare il nome del progetto
==============================

Creare il nome del progetto.

Scrivere nel file ``READ.ME`` la descrizione di cosa contiene quel progetto (un po di metadatazione del progetto).

Il nome del progetto sarà richiamato dal plugin GGeditor una volta richiamato l’account Github ed editati user e password. Appariranno su un pannello i vari repository Github del nostro account e si sceglierà quello a cui inviare i Google Doc ai quali lavoreremo. 

|

.. _h777c557c582d38262c7972186a6c3026:

2. Creare un file “conf.py”
===========================

Creare un file dandogli il nome ``conf.py`` e all’interno incollare il seguente codice

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
    
    # inserire un logo in alto a sinistra (mettendo l’immagine nella cartella “static”)
    latex_logo = "static/immagine.jpg"
    html_logo = "static/immagine.jpg"


..  Important:: 

    Nella pagine del codice sostituire i seguenti parametri:


.. code:: 

    project = 'CHANGE-THIS'

al posto di CHANGE-THIS (dentro gli apici) editare il nome del titolo progetto che si vuole far comparire su Read the Docs;

.. code:: 

    copyright = '2016, CHANGE-THIS' 

al posto di CHANGE-THIS (dentro gli apici) editare il tipo di licenza che si intende adottare per il rilascio della pubblicazione su Read the Docs.

\ |STYLE1|\ 

Se si vuole far visualizzare un logo sulla parte in alto a sinistra, si procede in questo modo: alla fine del codice del file conf.py, bisogna scrivere: 

.. code:: 

    latex_logo = "static/immagine.jpg"
    html_logo = "static/immagine.jpg"

dove ``immagine.jpg`` sarà l’immagine da visualizzare, che metteremo dentro la cartella 'static'. 

|

.. _h657a453c413f207c58413846774e759:

3. Creare il file “theme_overrides.css” e inserirlo dentro la cartella “static”
===============================================================================

Al fine di ottimizzare la visualizzazione delle tabelle ampie sulle pagine html di Read the Docs si crea questo file nella directory ``static``. Basta copiare il codice qui di seguito in un file che chiameremo, appunto, ``theme_overrides.css`` dentro la cartella ``static``.

.. code-block:: python
    :linenos:

    .wy-table-responsive table td, .wy-table-responsive table th {
       white-space: inherit;
    }
    
    .wy-table-responsive table th {
       background-color: #f0f0f0;
    }
    
    .line-block, .docutils.footnote {
        line-height: 24px;
    }
    
    .admonition {
        margin-bottom: 20px;
        line-height:24px;
    }
    
    .admonition > *:not(:first-child){
        /* draw a boder around a admonition */
        border-left: solid 1px #b59e9e;
        border-right: solid 1px #b59e9e;
        padding: 12px;
        margin: -12px -12px -12px -12px;
        margin-bottom: -12px !important;
    }
    .admonition > .last, .admonition- > .last{
        /* draw a boder around a admonition */
        border-bottom: solid 1px #b59e9e !important;
    }
    
    /* adatta il nav-content a fullhd e si elimina lo spazio vuoto piccolo a destra */
    .wy-nav-content {max-width: 1920px;} 
    
    

(guarda \ |LINK1|\ ).

L’istruzione  ``.wy-nav-content {max-width: 1920px;}`` consente di estendere per tutta la larghezza del monitor lo spazio in cui viene visualizzato il testo, dando una sensazione grafica gradevole all’intero documento.

|

.. _h1485f695e393f6b591579642211623:

Una configurazione leggera ed efficace 
=======================================

Con le due azioni di sopra si conclude tutto il lavoro da svolgere su Github, quindi questa soluzione si presta a chi non ha dimestichezza con il linguaggio RST. 

Una configurazione del progetto Github molto leggera ma efficace in termini di risultati di pubblicazione di un documento sul design Read the Docs.

\ |IMG1|\ 

Come si nota dall’elenco dei file che vengono generati dal plugin GGeditor direttamente nel repository Github abbiamo:

* un file ``README.md`` che è un file di descrizione del progetto, che provvediamo a editare noi su Github per far capire al lettore che cosa contiene il repository Github in questione. Questo file lo creiamo noi;

* il file ``conf.py`` che contiene il codice con indicazioni necessarie all’esposizione dei Google Docs sulla piattaforma di Read the Docs. \ |LINK2|\ . Basta creare un file nel repository Github, dargli il nome di ``conf.py`` e fare un copia  e incolla dal paragrafo del tutorial di GGeditor. Questo file lo creiamo noi;

* una directory ``static`` che contiene soltanto immagini ``.png`` che sono le immagini che incolliamo nel Google Doc e che nell’azione del “\ |STYLE2|\ ”, avviata dal plugin GGeditor, vengono generate automaticamente e inviate nella cartella ``static``. Questa cartella ``static`` viene generata automaticamente dal plugin GGeditor;

* il file ``theme_overrides.css`` che creeremo noidentro la directory ``static``.

* i file ``.rst`` che sono i Google Doc convertiti automaticamente in file ``.rst`` dal plugin GGeditor e inviati nel repository Github. Questi file vengono generati dal componente aggiuntivo di Google doc, GGeditor;

Dalla descrizione di questi file si comprende come l’intero pacchetto su Github è molto semplice come tipologia di file. L’unico più complesso da capire è il contenuto del file ``conf.py`` e del file ``theme_overrides.css`` ma sono file che non dobbiamo nemmeno creare, perchè copiamo i contenuti dei file dal tutorial, andando a cambiare al suo interno solo il “nome” del documento da pubblicare e “il tipo di licenza” (questo solo nel file ``conf.py``).

|

.. _h15816766a462d462c4a264e604e1360:

Inserire un logo in alto a sinistra nel design Read the Docs 
=============================================================

Per inserire un immagine in alto a sinistra nel design di “Read the Docs” basta andare nel file ``conf.py`` e alla fine inserire questo codice:

.. code:: 

    latex_logo = "static/immagine.png"
    html_logo = "static/immagine.png"

avendo cura di caricare il file ``immagine.png`` nella cartella ``static``.

Queste istruzioni non possono essere dati ai documenti da pubblicare in stile Docs Italia, ma solo ai documenti da pubblicare nello stile di base Read the Docs.

|

.. _h775782304944104a63b1778f5f7e:

Cambiare il colore di sfondo del rettangolo in alto a sinistra
==============================================================

Cambiare colore sul rettangolo superiore in alto è possibile. Qui di seguito si riporta il codice da inserire sul file ``theme_overrides.css`` che si trova dentro la cartella ``static``:

.. code:: 

    }
    
    .wy-side-nav-search {
        background-color: #7b90f9;
    }

il codice “#7b90f9“ usato in questo caso (il colore del rettangolo in alto a sinistra del tutorial che state leggendo) corrisponde alla tonalità cromatica verificabile a questo link: \ |LINK3|\ . Ovviamente cambiando codice numerico (con il #iniziale) è possibile generare altre tonalità da applicare al caso specifico.

Queste istruzioni non possono essere dati ai documenti da pubblicare in stile Docs Italia, ma solo ai documenti da pubblicare nello stile di base Read the Docs.

|

.. _h42f507fa1c6a29605c5a1a3a442f:

Cambiare il colore dei titoli dei capitoli, paragrafi, sottoparagrafi, ecc.
===========================================================================

Come prima, è anche possibile cambiare il colore dei titoli dei capitoli, paragrafi, sottoparagrafi, ecc. Sempre sul file ``theme_overrides.css`` si riporta il seguente codice:

.. code:: 

    }
    
    h1, h2, h3 {
        color: #176a90 !important;
    }

il codice “\ |LINK4|\ ” può essere cambiato con i codici di tantissimi altri colori disponibili.

Queste istruzioni non possono essere dati ai documenti da pubblicare in stile Docs Italia, ma solo ai documenti da pubblicare nello stile di base Read the Docs.

|


|REPLACE1|


|REPLACE2|


.. bottom of content


.. |STYLE0| replace:: **l’unico lavoro che c’è da fare sull’account di Github**

.. |STYLE1| replace:: **Logo**

.. |STYLE2| replace:: **Commit**


.. |REPLACE1| raw:: html

    <script id="dsq-count-scr" src="//guida-readthedocs.disqus.com/count.js" async></script>
    
    <div id="disqus_thread"></div>
    <script>
    
    /**
    *  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
    *  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/
    /*
    
    var disqus_config = function () {
    this.page.url = PAGE_URL;  // Replace PAGE_URL with your page's canonical URL variable
    this.page.identifier = PAGE_IDENTIFIER; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
    };
    */
    (function() { // DON'T EDIT BELOW THIS LINE
    var d = document, s = d.createElement('script');
    s.src = 'https://guida-readthedocs.disqus.com/embed.js';
    s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
    })();
    </script>
    <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
.. |REPLACE2| raw:: html

    <a href="https://twitter.com/cirospat?ref_src=twsrc%5Etfw" class="twitter-follow-button" data-show-count="false">Follow @cirospat</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

.. |LINK1| raw:: html

    <a href="http://ggeditor.readthedocs.io/en/latest/how2Readthedocs.html#step-4-theme-overrides-css" target="_blank">qui</a>

.. |LINK2| raw:: html

    <a href="http://ggeditor.readthedocs.io/en/latest/how2Readthedocs.html#step-3-conf-py" target="_blank">Il codice del file “conf.py” viene fornito nel tutorial di GGeditor</a>

.. |LINK3| raw:: html

    <a href="http://www.color-hex.com/color/7b90f9" target="_blank">http://www.color-hex.com/color/7b90f9</a>

.. |LINK4| raw:: html

    <a href="http://www.color-hex.com/color/176a90" target="_blank">#176a90</a>


.. |IMG1| image:: static/lavoro-github_1.png
   :height: 322 px
   :width: 601 px
