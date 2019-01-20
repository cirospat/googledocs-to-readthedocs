
.. _h305104c304e4b5e363d34c61406852:

Da Google Doc direttamente a Read the Docs con ``GGeditor``
###########################################################


|REPLACE1|


|REPLACE2|

Le spiegazioni contenute in questo documento rappresentano una via facile per migliorare la qualità dei documenti pubblicati sul web e sono la traduzione in italiano del \ |LINK1|\ . Fondamentalmente il tutorial spiega come usare Google doc, ed un componente aggiuntivo, per pubblicare documenti con lo stile di Read the Docs e con il design di \ |LINK2|\ .

Questo documento nasce subito dopo la produzione del tutorial “\ |LINK3|\ ”.


.. admonition:: Per questo tutorial i seguenti ringraziamenti particolari

    Ringraziare queste persone è importante perché hanno permesso di ampliare le possibilità d’uso di ``Read the Docs`` come piattaforma di pubblicazione documentale:
    
    Hsin Yuan Yeh, Andrea Borruso, Giovan Battista Vitrano, Salvatore Fiandaca, Pablo Persico.

|

.. _h387bd41572c6e60811453b41204663:

Vantaggi dell’uso di “Read the Docs”
====================================

L’uso di “\ |STYLE0|\ ” come piattaforma di pubblicazione di documenti ha i seguenti vantaggi sul formato “\ |STYLE1|\ ”:

|REPLACE3|

|

.. _h28105e656d4d48041184d771d3b4a1a:

GGeditor
========


|REPLACE4|

|

\ |LINK4|\  è un componente plugin che si installa direttamente da Google Doc (della suite di Google Drive) cercandolo nei componenti aggiuntivi e installandolo. Rappresenta uno strumento molto utile e comodo in quanto i servizi di Google Drive oggi sono molto usati anche nelle Pubbliche Amministrazioni, oltre che dai privati, per la facilità d’uso e per la funzionalità di condivisione dei documenti in gruppo.

Il lavoro principale che svolge il componente aggiuntivo GGeditor è quello di trasformare semplice testo editato su un foglio di Google doc in un file con linguaggio ``.rST`` dentro il repository di Github, che a sua volta permette la compilazione automatica dello stesso documento su Read the Docs.


|REPLACE5|

|


.. admonition:: Le principali funzioni e punti di forza di GGeditor sono

    * Facile inizio per chi non ha dimestichezza con i file RST, anche per chi non ha idea dei marcatori di RST.
    
    * Alimentato da Google Docs. Quasi la totalità di quello che vedi su Google Docs è quello che ottieni su Readthedocs. Lo stesso è per l'intero gruppo di lavoro.
    
    * Un click per commissionare il lavoro sul repository di Github.
    
    * Puoi vedere in anteprima il file RST generato dall'interno di Google Docs e scaricarlo nel tuo PC.
    
    * Supporta headings, bold, italic, hyperlink, subscript e superscript.
    
    * Supporta note a margine, immagini, liste di articolo e tabelle.
    
    * Supporta caratteri a larghezza intera (CKJ) nelle intestazioni e nelle tabelle.
    
    * Supporta i link interni ai bookmarks, headings e le Google Docs tabelle native di contenuti (in document table of contents).
    
    * Supporta i link relativi ai file RST generati dai Google Docs all'interno della stessa directory e sotto-directory Google Docs.
    
    * Supporta la tabella dei contenuti  (cross-document table of content (.. toctree::)) per fare generare l'indice a Readthedocs.
    
    * Supporta tutti gli stili di "admonitions" di Readthedocs.
    
    * Supporta account multipli per compilare i file nei repository di diversi account Github.
    
    * Supporta la conversione di tabelle con i tags HTML to let look-and-feel e la stessa cosa è possibile per i blogger.

--------

.. toctree::
  :maxdepth: 2

  Home <https://googledocs.readthedocs.io>


.. toctree:: 
    :maxdepth: 3
    :caption: Indice 

    gdocs-rtd
    tutorial
    come-usarlo
    tabelle
    inserire_immagini_video
    lavoro-github
    lavoro-rtd
    user-guide
    hypothesis-partecipazione
    sintassi-rst
    pubblicare-su-docs-italia
    licenza
    opendatasicilia


..  Tip:: 

    il contenuto di questa pagina che state leggendo è editato in \ |LINK5|\ 

--------


|REPLACE6|


.. bottom of content


.. |STYLE0| replace:: **Read the Docs**

.. |STYLE1| replace:: **PDF**


.. |REPLACE1| raw:: html

    <p><span style="background-color: #6462d1; color: #ffffff; display: inline-block; padding: 3px 8px; border-radius: 10px;">Passando automaticamente da Github!</span></p>
.. |REPLACE2| raw:: html

    <img src="https://ggeditor.readthedocs.io/en/latest/_images/index_1.png" />
.. |REPLACE3| raw:: html

    <p><span style="background-color: #6462d1; color: #ffffff; display: inline-block; padding: 3px 8px; border-radius: 10px;">Responsive</span></p>
    
    <p><span style="background-color: #105618; color: #ffffff; display: inline-block; padding: 3px 8px; border-radius: 10px;">Funzioni avanzate di ricerca testo</span></p>
    
    <p><span style="background-color: #14c9ab; color: #ffffff; display: inline-block; padding: 3px 8px; border-radius: 10px;">Fornisce testo in HTML, EPUB e PDF</span></p>
    
    <p><span style="background-color: #e86514; color: #ffffff; display: inline-block; padding: 3px 8px; border-radius: 10px;">Codice sorgente del testo online</span></p>
    
    <p><span style="background-color: #c914c0; color: #ffffff; display: inline-block; padding: 3px 8px; border-radius: 10px;">E’ elegante e bello da vedere</span></p>
.. |REPLACE4| raw:: html

    <img src="https://ggeditor.readthedocs.io/en/latest/_images/index_2.png" alt="" width="800 />
    <br>
.. |REPLACE5| raw:: html

    <iframe width="100%" height="500" src="https://www.youtube.com/embed/5O2D4h5hI18" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    Breve video introduttivo (2’10”)
.. |REPLACE6| raw:: html

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

    <a href="http://ggeditor.readthedocs.io/en/latest/" target="_blank">tutorial GGeditor</a>

.. |LINK2| raw:: html

    <a href="http://googledocs.readthedocs.io/it/latest/pubblicare-su-docs-italia.html" target="_blank">Docs Italia</a>

.. |LINK3| raw:: html

    <a href="http://come-creare-guida.readthedocs.io/it/latest/" target="_blank">Come abbiamo creato un «Read the Docs» per pubblicare documenti pubblici su Docs Italia</a>

.. |LINK4| raw:: html

    <a href="https://chrome.google.com/webstore/detail/ggeditor/piedgdbcihbejidgkpabjhppneghbcnp" target="_blank">GGeditor</a>

.. |LINK5| raw:: html

    <a href="https://docs.google.com/document/d/1L53rUYYMd5-UJUv6nj87uE6giZXHb9n4BsRemodCevI/" target="_blank">questo Google Doc</a>

