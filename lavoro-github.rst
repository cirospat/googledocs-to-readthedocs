
.. _h4a6529483549719b66336a3470283f:

Il lavoro da fare su Github
***************************


|REPLACE1|

|

.. _h27d37777d6f59f417f254b4fa3a:

1. Creare il nome del progetto
==============================

Creare il nome del progetto.

Scrivere nel file ``READ.ME`` la descrizione di cosa contiene quel progetto (un po di metadatazione del progetto). Come nel caso del \ |LINK1|\ .

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

\ |STYLE0|\ 

Se si vuole far visualizzare un logo sulla parte in alto a sinistra, si procede in questo modo: alla fine del codice del file ``conf.py``, bisogna scrivere: 

.. code:: 

    latex_logo = "static/immagine.jpg"
    html_logo = "static/immagine.jpg"

dove ``immagine.jpg`` sarà l’immagine da visualizzare in alto a sinistra (logo del nostro progetto), che metteremo dentro la cartella ``static``. 

|

.. _h657a453c413f207c58413846774e759:

3. Creare il file “theme_overrides.css” e inserirlo dentro la cartella “static”
===============================================================================

Il file ``theme_overrides.css`` serve per andare a modificare la grafica base del file ``conf.py``.

Serve anche per ottimizzare la visualizzazione delle tabelle ampie sulle pagine HTML di Read the Docs.

Si crea questo file dentro la directory ``static``. Basta copiare il codice qui di seguito descritto in un file che chiameremo, appunto, ``theme_overrides.css`` dentro la cartella ``static``.

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
    
    

(guarda \ |LINK2|\ ).

L’istruzione  ``.wy-nav-content {max-width: 1920px;}`` consente di estendere per tutta la larghezza del monitor lo spazio in cui viene visualizzato il testo, dando una sensazione grafica gradevole all’intero documento.

|

.. _h1485f695e393f6b591579642211623:

Una configurazione leggera ed efficace 
=======================================

Con le tre azioni di sopra si conclude tutto il lavoro da svolgere su Github, quindi questa soluzione si presta a chi non ha dimestichezza con il linguaggio ``RST``. 

Una configurazione del progetto Github molto leggera ma efficace in termini di risultati di pubblicazione di un documento sul design Read the Docs.

\ |IMG1|\ 

Come si nota dall’elenco dei file che vengono generati dal plugin ``GGeditor`` direttamente nel repository Github abbiamo:

* un file ``README.md`` che è un file di descrizione del progetto, che provvediamo a editare noi su Github per far capire al lettore che cosa contiene il repository Github in questione. Questo file lo creiamo noi;

* il file ``conf.py`` che contiene il codice con indicazioni necessarie all’esposizione dei Google Docs sulla piattaforma di Read the Docs. \ |LINK3|\ . Basta creare un file nel repository Github, dargli il nome di ``conf.py`` e fare un copia  e incolla dal paragrafo del tutorial di GGeditor. Questo file lo creiamo noi;

* una directory ``static`` che contiene soltanto immagini ``.png`` che sono le immagini che incolliamo nel Google Doc e che nell’azione del “\ |STYLE1|\ ”, avviata dal plugin GGeditor, vengono generate automaticamente e inviate nella cartella ``static``. Questa cartella ``static`` viene generata automaticamente dal plugin GGeditor;

* il file ``theme_overrides.css`` che creeremo dentro la directory ``static``.

* i file ``.rst`` che sono i Google Doc convertiti automaticamente in file ``.rst`` dal plugin GGeditor e inviati nel repository Github. Questi file vengono generati dal componente aggiuntivo di Google doc, GGeditor;

Dalla descrizione di questi file si comprende come l’intero pacchetto su Github è molto semplice come tipologia di file. L’unico più complesso da capire è il contenuto del file ``conf.py`` e del file ``theme_overrides.css`` ma sono file che non dobbiamo nemmeno creare, perchè copiamo i contenuti dei file dal tutorial, andando a cambiare al suo interno solo il “nome” del documento da pubblicare e “il tipo di licenza” (questo solo nel file ``conf.py``) e aggiungendo il nome del file immagine qualora volessimo creare un logo del progetto da far visualizzare in alto a sinistra sul progetto di Read the Docs.

|

.. _h15816766a462d462c4a264e604e1360:

Inserire un logo in alto a sinistra nel design Read the Docs 
=============================================================

Per inserire un immagine in alto a sinistra nel design di “Read the Docs”, per creare il logo del nostro progetto, basta andare nel file ``conf.py`` e alla fine inserire questo codice:

.. code:: 

    latex_logo = "static/immagine.png"
    html_logo = "static/immagine.png"

avendo cura di caricare il file ``immagine.png`` nella cartella ``static``.

..  Attention:: 

    Queste istruzioni non possono essere dati ai documenti da pubblicare in stile \ |STYLE2|\ , ma solo ai documenti da pubblicare nello stile di base Read the Docs.

|

.. _h76707323ea2c4a39744e2f14a2a48:

Inserire la freccia “back to the top” nella pagina html
=======================================================

\ |IMG2|\ 

Al fine di permettere di risalire rapidamente in alto nella pagina HTML, torna comoda l’icona a forma di freccia sulla parte destra in basso della stessa pagina. 

Di seguito la procedura per ottenere la freccia “back to the top” sulla pagina HTML.

Creare la cartella ``_templates`` e all’interno di essa creare il file ``layout.html`` e copiare il seguente codice:

.. code-block:: python
    :linenos:

    <link href="{{ pathto("_static/theme_overrides.css", True) }}" rel="stylesheet" type="text/css" />
    
    <!-- css back top -->
    <!--<link href="../_static/jquerysctipttop.css" rel="stylesheet" type="text/css" />-->
    <link href="{{ pathto("_static/jquerysctipttop.css", True) }}" rel="stylesheet" type="text/css" />
    <!--<link href="../_static/backTop.css" rel="stylesheet" type="text/css" />-->
    <link href="{{ pathto("_static/backTop.css", True) }}" rel="stylesheet" type="text/css" />
    <!-- Script -->
    <!--<script type="text/javascript" src="../_static/jquery.min.js"></script> -->
    <script type="text/javascript" src="{{ pathto("_static/jquery.min.js", True) }}"></script> 
     {% endblock %}
    
    
    {% block footer %}
          {{ super() }}
    	   <!-- script Back To Top  -->
          <div class="footerc">
              <a id='backTop'>Back To Top</a>
     <!-- script toptoback automatico mobile/desktop -->  
     <!-- <script type="text/javascript" src="../_static/jquery.backTop.min.js"></script> -->
    <script type="text/javascript" src="{{ pathto("_static/jquery.backTop.min.js", True) }}"></script>
    <script>
                $(document).ready( function() {
                    $('#backTop').backTop({
                        'position' : 400,
                        'speed' : 300,
                        'color' : 'green',
    
    					                });
                });
            </script>
          </div>
    
    {% endblock %}
    

Nella cartella ``static`` creare i file:

* \ |LINK4|\ 

* \ |LINK5|\ 

* \ |LINK6|\ 

* \ |LINK7|\ 

copiando il codice dai rispettivi file dei link di sopra.

Sempre dento la cartella ``static``, bisogna inserire un immagine (con la freccia in alto) come questa contenuta qui dentro:  \ |LINK8|\ . 

E infine non dimenticare di inserire nel file ``conf.py`` alla fine delle righe, il seguente codice:


.. code:: 

    
    templates_path = ['_templates']

    

|

.. _h34123439147b2c6243c2b30762a182f:

Inserire lateralmente icone per la condivisione delle pagine HTML di RTD sui social network
===========================================================================================

Al fine di permettere la condivisione delle pagine del documento Read the Docs sui social network, una delle soluzioni che graficamente si adatta meglio alla grafica delle pagine RTD è fornita dalla piattaforma gratuita \ |LINK9|\ . Una volta creato l’account su \ |STYLE3|\  è possibile creare icone personalizzate (colore, dimensione) per la visualizzazione delle stesse sulle pagine html di RTD. Una volta creato il banner, sempre nella piattaforma addthis andare su “get the code” e copiare il codice che viene fornito. Tale codice è di questo tipo

.. code:: 

    <!-- Go to www.addthis.com/dashboard to customize your tools --> 
    <script type="text/javascript" src="//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-5b4c36adc4260026"></script>

e va incollato nella pagina ``layout.html`` (dentro la cartella ``_templates``) prima di ``{% endblock %}``. Tutto qui.

|

.. _h1d174020704f7c333b244d404e247c:

Inserire il popup eu-cookie nei progetti  "read the docs"
=========================================================

(\ |STYLE4|\ )

Per aggiungere il popup \ |STYLE5|\  per dare visibilità dei contenuti concernenti la privacy, basta aggiungere i tre file script di seguito elencati nella cartella ``static`` del progetto Github:

* \ |LINK10|\ 

* \ |LINK11|\ 

* \ |LINK12|\ 

Inserire nel file \ |LINK13|\  (nel blocco principale) il codice html:


.. code:: 

    <!--eu-cooki-lawt →
    <script type="text/javascript" src="{{ pathto("_static/jquery-2.1.3.min.js", True) }}"></script>
    <script type="text/javascript" src="{{ pathto("_static/jquery-eu-cookie-law-popup.js", True) }}"></script>
    <link href="{{ pathto("_static/jquery-eu-cookie-law-popup.css", True) }}" rel="stylesheet" type="text/css" />

Sempre nel file ``layout.html`` inserire il seguente codice:

.. code:: 

    <div class="eupopup eupopup-top "></div>

(il codice si trova alla riga 27 del file layout.html: \ |LINK14|\ ) 

Per modificare il testo del popup, apri il file ``jquery-eu-cookie-law-popup.js`` con notepad++, o  anche con il semplice notepad, e cerca il blocco \ |STYLE6|\ , e li modifichi ``url`` della pagina \ |STYLE7|\  ed il testo:

.. code:: 

    // PARAMETERS (MODIFY THIS PART) ///////////////////////
    _self.params = {
    cookiePolicyUrl : 'https://cirospat.readthedocs.io/it/latest/privacy.html',
    popupPosition : 'top',
    colorStyle : 'default',
    compactStyle : false,
    popupTitle : 'Questo sito web utilizza i cookie, anche di terze parti, per migliorare la vostra esperienza di navigazione web.',
    popupText : 'Chiudendo questo banner, scorrendo questa pagina o cliccando su qualunque suo elemento acconsenti all&rsquo;uso dei cookie. Per maggiori informazioni o per negare il consenso a tutti o ad alcuni cookie, consulta l&rsquo;informativa.',
    buttonContinueTitle : 'Chiudi!  ',
    buttonLearnmoreTitle : 'Leggi l&rsquo;informativa',
    buttonLearnmoreOpenInNewWindow : false,
    agreementExpiresInDays : 30,
    autoAcceptCookiePolicy : false,
    htmlMarkup : null
    };

\ |STYLE8|\  che devi aggiungere nel tuo progetto “Read the Docs” la pagina dell'\ |LINK15|\ . Ovviamente questa pagina HTML sarà del testo preventivamente editato su un Google doc.

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

il codice “#7b90f9“ usato in questo caso (il colore del rettangolo in alto a sinistra del tutorial che state leggendo) corrisponde alla tonalità cromatica verificabile a questo link: \ |LINK16|\ . Ovviamente cambiando codice numerico (con  #iniziale) è possibile generare altre tonalità da applicare al caso specifico.

..  Attention:: 

    Queste istruzioni non possono essere dati ai documenti da pubblicare in stile \ |STYLE9|\ , ma solo ai documenti da pubblicare nello stile di base Read the Docs.

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

il codice “\ |LINK17|\ ” può essere cambiato con i codici di tantissimi altri colori disponibili.

..  Attention:: 

    Queste istruzioni non possono essere dati ai documenti da pubblicare in stile \ |STYLE10|\ , ma solo ai documenti da pubblicare nello stile di base Read the Docs.

|

.. _h206b132a6447317f607c2b3751106c78:

Uno schema tipo di progetto Github che raccoglie tutte le funzioni illustrate in questa pagina del tutorial
===========================================================================================================


|REPLACE2|

A questa pagina di Github \ |LINK18|\  si trova uno “\ |STYLE11|\ ” di repository la cui restituzione come progetto Read the Docs è disponibile qui: \ |LINK19|\ . 

Lo schema tipo Github può essere clonato per creare un altro progetto Github che abbia le stesse impostazioni, che graficamente sono visibili nel relativo \ |LINK20|\ .

Quindi la funzione dello schema tipo Github è quella di facilitare tutte le procedure di editing del codice, non dovendo pensare a crearlo da zero, e dando la possibilità all’utente di cambiare le personalizzazioni (titolo del progetto e versione della licenza nel file ``conf.py``, colore testo dei capitoli/paragrafi, colore del riquadro in alto a sinistra e altre impostazioni nel file ``theme_override.css`` dentro la cartella ``static``) e di concentrarsi maggiormente sui contenuti (testo, immagini, video,..) della pubblicazione che saranno editati direttamente dentro i Google doc.

|


|REPLACE3|


.. bottom of content


.. |STYLE0| replace:: **Creare il logo in alto a sinistra**

.. |STYLE1| replace:: **Commit**

.. |STYLE2| replace:: **Docs Italia**

.. |STYLE3| replace:: **addthis**

.. |STYLE4| replace:: **istruzioni a cura di Giovan Battista Vitrano**

.. |STYLE5| replace:: **eu-cookie**

.. |STYLE6| replace:: **PARAMETERS (MODIFY THIS PART)**

.. |STYLE7| replace:: **privacy**

.. |STYLE8| replace:: **Ricordati (!)**

.. |STYLE9| replace:: **Docs Italia**

.. |STYLE10| replace:: **Docs Italia**

.. |STYLE11| replace:: **schema tipo**


.. |REPLACE1| raw:: html

    Con il metodo proposto in questo tutorial, il lavoro che c’è da fare sull’account di &nbsp;&nbsp;<button class="btn btn-pill btn-info"type="button"><strong>Github</strong></button>&nbsp;&nbsp; è il seguente.
.. |REPLACE2| raw:: html

    <img src="https://schema-tipo.readthedocs.io/it/latest/_static/logo.jpg" width="250"/>
    
    <p><span style="background-color: #6462d1; color: #ffffff; display: inline-block; padding: 3px 8px; border-radius: 10px;">Asino siciliano</span></p>
.. |REPLACE3| raw:: html

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

.. |LINK1| raw:: html

    <a href="https://github.com/cirospat/googledocs-to-readthedocs/blob/master/README.md" target="_blank">file READ.ME di questo tutorial</a>

.. |LINK2| raw:: html

    <a href="http://ggeditor.readthedocs.io/en/latest/how2Readthedocs.html#step-4-theme-overrides-css" target="_blank">qui</a>

.. |LINK3| raw:: html

    <a href="http://ggeditor.readthedocs.io/en/latest/how2Readthedocs.html#step-3-conf-py" target="_blank">Il codice del file “conf.py” viene fornito nel tutorial di GGeditor</a>

.. |LINK4| raw:: html

    <a href="https://github.com/cirospat/newproject/blob/master/docs/static/jquerysctipttop.css" target="_blank">jquerysctipttop.css</a>

.. |LINK5| raw:: html

    <a href="https://github.com/cirospat/newproject/blob/master/docs/static/backTop.css" target="_blank">backTop.css</a>

.. |LINK6| raw:: html

    <a href="https://github.com/cirospat/newproject/blob/master/docs/static/jquery.min.js" target="_blank">jquery.min.js</a>

.. |LINK7| raw:: html

    <a href="https://github.com/cirospat/newproject/blob/master/docs/static/jquery.backTop.min.js" target="_blank">jquery.backTop.min.js</a>

.. |LINK8| raw:: html

    <a href="https://github.com/cirospat/newproject/blob/master/docs/static/hfctop.png" target="_blank">https://github.com/cirospat/newproject/blob/master/docs/static/hfctop.png</a>

.. |LINK9| raw:: html

    <a href="https://www.addthis.com" target="_blank">https://www.addthis.com</a>

.. |LINK10| raw:: html

    <a href="https://github.com/cirospat/newproject/blob/master/docs/static/jquery-2.1.3.min.js" target="_blank">jquery-2.1.3.min.js</a>

.. |LINK11| raw:: html

    <a href="https://github.com/cirospat/newproject/blob/master/docs/static/jquery-eu-cookie-law-popup.js" target="_blank">jquery-eu-cookie-law-popup.js</a>

.. |LINK12| raw:: html

    <a href="https://github.com/cirospat/newproject/blob/master/docs/static/jquery-eu-cookie-law-popup.css" target="_blank">jquery-eu-cookie-law-popup.css</a>

.. |LINK13| raw:: html

    <a href="https://github.com/cirospat/newproject/blob/master/docs/_templates/layout.html" target="_blank">layout.html</a>

.. |LINK14| raw:: html

    <a href="https://github.com/cirospat/newproject/blob/master/docs/_templates/layout.html" target="_blank">https://github.com/cirospat/newproject/blob/master/docs/_templates/layout.html</a>

.. |LINK15| raw:: html

    <a href="https://cirospat.readthedocs.io/it/latest/privacy.html" target="_blank">informativa privacy</a>

.. |LINK16| raw:: html

    <a href="http://www.color-hex.com/color/7b90f9" target="_blank">http://www.color-hex.com/color/7b90f9</a>

.. |LINK17| raw:: html

    <a href="http://www.color-hex.com/color/176a90" target="_blank">#176a90</a>

.. |LINK18| raw:: html

    <a href="https://github.com/cirospat/rtd-schematipo" target="_blank">https://github.com/cirospat/rtd-schematipo</a>

.. |LINK19| raw:: html

    <a href="https://schema-tipo.readthedocs.io" target="_blank">https://schema-tipo.readthedocs.io</a>

.. |LINK20| raw:: html

    <a href="https://schema-tipo.readthedocs.io" target="_blank">progetto Read the Docs</a>


.. |IMG1| image:: static/lavoro-github_1.png
   :height: 322 px
   :width: 601 px

.. |IMG2| image:: static/lavoro-github_2.png
   :height: 49 px
   :width: 49 px
