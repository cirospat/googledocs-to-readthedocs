
.. _h747d28468046343a107a754c621e3b0:

Pubblicare con il design di Docs Italia
#######################################

Se una Pubblica Amministrazione vuole sfruttare il servizio del componente aggiuntivo di Google doc, GGeditor, per pubblicare un documento su Read the Docs ma con il design di \ |LINK1|\ , ecco alcune cose da tenere in considerazione al fine di non commettere errori che - alla fine - potrebbero non fare compilare la costruzione (build) del documento su Read the Docs e quindi pregiudicare la visualizzazione delle pagine HTML. Docs Italia parte dallo stile semplice di Read the Docs ma viene arricchito, dal Team Trasformazione Digitale, di header e footer nella visualizzazione delle pagine html e di alcune novità in termini di personalizzazioni nella visualizzazione di alcuni contenuti testuali.

Ci sono differenze nel file ``conf.py`` del progetto con lo stile basic  \ |STYLE0|\  rispetto al file ``conf.py`` del progetto con il design \ |STYLE1|\  del Team Trasformazione Digitale. Basta conoscerle e si eviteranno errori. Il file ``conf.py`` sul progetto Github è il cuore della configurazione che permette la corretta visualizzazione delle pagine html e la visualizzazione degli aggiornamenti fatti nelle pagine Google doc!

* \ |LINK2|\  un esempio di file ``conf.py`` del progetto con lo stile basic  \ |STYLE2|\ .

* \ |LINK3|\  un esempio di file ``conf.py`` del progetto con lo stile basic  \ |STYLE3|\ .

Evidente la differenza di istruzioni date nei due file.

Di seguito alcuni accorgimenti da tenere presenti nel lavoro da fare.

|

.. _h639194313702264d773f76407a5175:

Uso corretto degli apici e doppi apici nel file ‘conf.py’
*********************************************************

Nel file ``conf.py`` che si trova nel repository di Github, i doppi apici (“) vanno solo nel primo campo:

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

Nell'editing del nome dei file dei capitoli sul toctree, nel Google doc dell'index, deve essere inserito il suffisso ``.rst``. Senza l’aggiunta del suffisso, sulle pagine html dello stile Docs Italia non comparirà la struttura dell’indice in home page.

Nel caso della pubblicazione su Read the Docs \ |STYLE4|\ , (\ |STYLE5|\ ) l’assenza di  questo suffisso ``.rst`` per ogni file elencato nel toctree del file ‘index’ non costituisce un problema e l’indice viene visualizzato ugualmente sulle pagine html di Read the Docs.

Esempio di indice nel Google doc “index” nel caso di progetto \ |STYLE6|\ : si nota l’assenza del suffisso ``.rst`` ad ogni titolo dei file elencati nel toctree

.. code:: 

    .. toctree::
        :maxdepth: 3
        :caption: Indice
    
        gdocs-rtd
        tutorial
        come-usarlo
        lavoro-github
        lavoro-rtd
        user-guide
        hypothesis-partecipazione
        pubblicare-su-docs-italia
        licenza

Esempio di indice nel Google doc “index” nel caso di progetto \ |STYLE7|\ : si nota la presenza del suffisso ``.rst`` ad ogni titolo dei file elencati nel toctree

.. code:: 

    .. toctree::
        :maxdepth: 3
        :caption: Indice dei contenuti
    
        CARTA-SERVIZI-BIBLIOTECA-capitolo-1.rst
        CARTA-SERVIZI-BIBLIOTECA-capitolo-2.rst
        CARTA-SERVIZI-BIBLIOTECA-capitolo-3.rst
        CARTA-SERVIZI-BIBLIOTECA-appendice.rst

|

.. _h1573c382a5663265f406c5380716d:

HTML Logo
*********

Sui documenti pubblicati con il design Docs Italia non c’è la possibilità di fare visualizzare un logo/immagine in alto a sinistra come, invece, avviene con la versione Read the Docs basic.

Quindi l’istruzione 

.. code:: 

    html_logo = "images/logo.png"

non deve essere data in questo caso. Se viene data la compilazione su Read the Docs fallisce.

Può essere editato cancelletto prima:

.. code:: 

    # html_logo = "images/logo.png"

così facendo l’istruzione non ha effetto in quanto tutto ciò che viene dopo cancelletto sul file ``conf.py`` rappresenta un testo di commento e non un'istruzione da eseguire. 

|

.. _h682146b5f1b604e4e625585a4c3b49:

Un ‘progetto tipo’ da clonare per la pubblicazione con il design Docs Italia
****************************************************************************

A titolo di \ |LINK4|\ , da clonare su Github, per l’esigenza di creazione di un nuovo progetto di pubblicazione con il design \ |STYLE8|\ , può essere usato questo repository su Github: \ |LINK5|\  dove sono state effettuate le necessarie verifiche nel file ``conf.py`` che permette un esatta compilazione del progetto sul design Docs Italia, ottenendo lo status verde di \ |STYLE9|\  \ |LINK6|\ . 

Qui il file ``conf.py`` \ |LINK7|\ . 

E qui di seguito le uniche cose da personalizzare nel file ``conf.py``:

.. code:: 

    settings_project_name = "cambiami"
    settings_copyright_copyleft = 'Comune di ...'
    settings_editor_name = 'Comune di ...'
    settings_doc_version = 'version: latest'
    settings_doc_release = 'version: latest'
    settings_basename = 'cambiami'
    settings_file_name = 'cambiami'

Se sul sito Read the Docs avete dato, ad esempio, al progetto il titolo  “\ |STYLE10|\ ”, allora nel campo ``settings_basename`` e nel file ``settings_file_name`` date lo stesso nome così

.. code:: 

    settings_basename = 'linee-guida-open-data-comune-vattelapesca'
    settings_file_name = 'linee-guida-open-data-comune-vattelapesca'

|


|REPLACE1|


.. bottom of content


.. |STYLE0| replace:: **Read the Docs**

.. |STYLE1| replace:: **Docs Italia**

.. |STYLE2| replace:: **Read the Docs**

.. |STYLE3| replace:: **Docs Italia**

.. |STYLE4| replace:: **versione basic**

.. |STYLE5| replace:: **cioè senza il design Docs Italia elaborato dal Team Digitale per i documenti della PA**

.. |STYLE6| replace:: **Read the Docs**

.. |STYLE7| replace:: **Docs Italia**

.. |STYLE8| replace:: **Docs Italia**

.. |STYLE9| replace:: **passed**

.. |STYLE10| replace:: **linee guida open data comune vattelapesca**


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

.. |LINK1| raw:: html

    <a href="http://guida-docs-italia.readthedocs.io/it/latest/" target="_blank">Docs Italia (elaborato dal Team Digitale per  le pubblicazioni della PA)</a>

.. |LINK2| raw:: html

    <a href="https://github.com/cirospat/googledocs-to-readthedocs/blob/master/conf.py" target="_blank">Qui</a>

.. |LINK3| raw:: html

    <a href="https://github.com/cirospat/joppy/blob/master/conf.py" target="_blank">Qui</a>

.. |LINK4| raw:: html

    <a href="http://joppy.readthedocs.io" target="_blank">progetto tipo</a>

.. |LINK5| raw:: html

    <a href="https://github.com/cirospat/joppy" target="_blank">https://github.com/cirospat/joppy</a>

.. |LINK6| raw:: html

    <a href="https://readthedocs.org/projects/joppy/" target="_blank">https://readthedocs.org/projects/joppy/</a>

.. |LINK7| raw:: html

    <a href="https://github.com/cirospat/joppy/blob/master/conf.py" target="_blank">https://github.com/cirospat/joppy/blob/master/conf.py</a>

