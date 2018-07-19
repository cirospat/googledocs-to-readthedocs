
.. _h305104c304e4b5e363d34c61406852:

Da Google Doc direttamente a Read the Docs con ``GGeditor``
###########################################################

Passando automaticamente da Github!

\ |IMG1|\ 

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

|REPLACE1|

.. _h28105e656d4d48041184d771d3b4a1a:

GGeditor
========

\ |IMG2|\ 

\ |LINK4|\  è un componente plugin che si installa direttamente da Google Doc (della suite di Google Drive) cercandolo nei componenti aggiuntivi e installandolo. Rappresenta uno strumento molto utile e comodo in quanto i servizi di Google Drive oggi sono molto usati anche nelle Pubbliche Amministrazioni, oltre che dai privati, per la facilità d’uso e per la funzionalità di condivisione dei documenti in gruppo.

Il lavoro principale che svolge il componente aggiuntivo GGeditor è quello di trasformare semplice testo editato su un foglio di Google doc in un file con linguaggio ``.RST`` dentro il repository di Github, che a sua volta permette la compilazione automatica dello stesso documento su Read the Docs.


|REPLACE2|

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
    sintassi-rst
    licenza

--------


|REPLACE3|

--------


|REPLACE4|


|REPLACE5|


.. bottom of content


.. |STYLE0| replace:: **Read the Docs**

.. |STYLE1| replace:: **PDF**


.. |REPLACE1| raw:: html

    <p><span class="btn btn-danger btn-xs">Responsive, per tutti i display</span></p>
    
    <p><button type="button" class="btn btn-xs btn-pill btn-warning">Funzioni avanzate di ricerca testo</button></p>
    
    <p><button class="btn btn-pill btn-success" type="button">Fornisce testo in HTML, EPUB e PDF</button></p>
    
    <p><button class="btn btn-pill btn-success" type="button">Codice sorgente del testo online</button></p>
    
    <p><button class="btn btn-pill btn-info"type="button">E’ elegante e bello da vedere</button></p>
.. |REPLACE2| raw:: html

    <iframe width="100%" height="500" src="https://www.youtube.com/embed/5O2D4h5hI18" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    Breve video introduttivo (2’10”)
.. |REPLACE3| raw:: html

    <p><img src="http://siciliahub.github.io/mappe/carto_omira/lib/images/opendatasicilia.png" alt="" width="91" height="104" />&nbsp;&nbsp;<strong>S</strong><strong>ervizi di&nbsp;<span style="color: #3366ff;"><a href="http://opendatasicilia.it/" rel="nofollow noopener" style="color: #3366ff;" target="_blank">OpendataSicilia</a></span></strong></p>
    <p><a href="http://accussi.opendatasicilia.it/index.html" target="_blank" rel="noopener"><img src="https://camo.githubusercontent.com/24bc1b1450d155db547405fa90d92b6b34f4a132/68747470733a2f2f6369726f737061742e6769746875622e696f2f6d6170732f696d672f616363757373695f66617669636f6e2e706e67" alt="accussi" width="46" height="46" /></a>&nbsp; &nbsp; &nbsp;<a href="http://nonportale.opendatasicilia.it/index.html" rel="nofollow noopener" target="_blank"><img src="https://camo.githubusercontent.com/7ad90a32a27ec7b68b3f5d1c9aec83d0bf5e4120/68747470733a2f2f6369726f737061742e6769746875622e696f2f6d6170732f696d672f6e6f6e706f7274616c655f66617669636f6e2e706e67" alt="non portale" width="41" height="41" data-canonical-src="https://cirospat.github.io/maps/img/nonportale_favicon.png" /></a>&nbsp; &nbsp; &nbsp;<a href="http://petrusino.opendatasicilia.it/index.html" target="_blank" rel="noopener"><img src="https://camo.githubusercontent.com/acae135c1a21da78bfd3423518810cd5465a8642/68747470733a2f2f6369726f737061742e6769746875622e696f2f6d6170732f696d672f706574727573696e6f5f66617669636f6e2e706e67" alt="petrusino" width="47" height="47" /></a>&nbsp;&nbsp;</p>
    <p><a href="http://albopop.it/" rel="nofollow noopener" target="_blank">Albo Pop</a>&nbsp; &nbsp;&nbsp;<a href="http://www.foiapop.it/" rel="nofollow noopener" target="_blank">FOIA Pop</a>&nbsp; &nbsp;&nbsp;<a href="http://www.visualcad.it/" rel="nofollow noopener" target="_blank">Visual CAD</a>&nbsp;<strong>&nbsp;</strong></p>
    <p>Licenza&nbsp;<a href="http://creativecommons.org/licenses/by-sa/4.0/" rel="nofollow noopener" target="_blank"><img alt="Licenza Creative Commons" src="https://camo.githubusercontent.com/d1b3cb5c3bc0b0de6fb5445b1657c03464125482/68747470733a2f2f692e6372656174697665636f6d6d6f6e732e6f72672f6c2f62792d73612f342e302f38307831352e706e67" data-canonical-src="https://i.creativecommons.org/l/by-sa/4.0/80x15.png" /></a></p>
    <p><strong>OpendataSicilia</strong> &egrave; una iniziativa civica condivisa da pi&ugrave; persone, che si propone di far conoscere e diffondere la cultura dell'open government e le prassi dell'open data nel nostro territorio e aprire una discussione pubblica partecipata. Siamo anche su:</p>
    <ul style="list-style-type: disc;">
    <li>la <span style="color: #0000ff;"><a href="https://groups.google.com/forum/#!forum/opendatasicilia" target="_blank" rel="noopener" style="color: #0000ff;">mailing list</a></span> di lavoro;</li>
    <li>il <a href="http://opendatasicilia.it" target="_blank" rel="noopener"><span style="color: #3366ff;">blog</span></a>;</li>
    <li>il gruppo <a href="https://www.facebook.com/groups/opendatasicilia" target="_blank" rel="noopener">facebook</a>;</li>
    <li>l'account <span style="color: #3366ff;"><a href="http://twitter.com/opendatasicilia" target="_blank" rel="noopener" style="color: #3366ff;">twitter</a></span>;</li>
    <li>il canale <a href="http://opendatasicilia.slack.com" target="_blank" rel="noopener">Slack</a><span>&nbsp;</span>(<a href="http://slack.opendatasicilia.it" target="_blank" rel="noopener">per iscriversi</a>).</li>
    </ul>
    
.. |REPLACE4| raw:: html

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
.. |REPLACE5| raw:: html

    <a href="https://twitter.com/cirospat?ref_src=twsrc%5Etfw" class="twitter-follow-button" data-show-count="false">Follow @cirospat</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

.. |LINK1| raw:: html

    <a href="http://ggeditor.readthedocs.io/en/latest/" target="_blank">tutorial GGeditor</a>

.. |LINK2| raw:: html

    <a href="http://googledocs.readthedocs.io/it/latest/pubblicare-su-docs-italia.html" target="_blank">Docs Italia</a>

.. |LINK3| raw:: html

    <a href="http://come-creare-guida.readthedocs.io/it/latest/" target="_blank">Come abbiamo creato un «Read the Docs» per pubblicare documenti pubblici su Docs Italia</a>

.. |LINK4| raw:: html

    <a href="https://chrome.google.com/webstore/detail/ggeditor/piedgdbcihbejidgkpabjhppneghbcnp" target="_blank">GGeditor</a>


.. |IMG1| image:: static/index_1.png
   :height: 250 px
   :width: 504 px

.. |IMG2| image:: static/index_2.png
   :height: 132 px
   :width: 216 px
