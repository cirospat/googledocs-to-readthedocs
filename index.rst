
|REPLACE1|

.. _h305104c304e4b5e363d34c61406852:

Da Google Doc direttamente a Read the Docs con ``GGeditor``
###########################################################


|REPLACE2|


|REPLACE3|

Le spiegazioni contenute in questo documento rappresentano una via piuttosto facile per migliorare la qualità dei documenti pubblicati sul web e sono la traduzione in italiano del \ |LINK1|\ . Fondamentalmente il tutorial spiega come usare lo strumento di \ |STYLE0|\ , ed un componente aggiuntivo, per pubblicare documenti con lo stile di \ |STYLE1|\  e con il design di \ |LINK2|\ .

Questo documento nasce subito dopo la produzione del tutorial “\ |LINK3|\ ”.


.. admonition:: Per questo tutorial i seguenti ringraziamenti particolari

    Ringraziare queste persone è importante, perché con i loro approfondimenti hanno permesso di ampliare le possibilità d’uso di ``Read the Docs`` come piattaforma di pubblicazione documentale:
    
    \ |LINK4|\ , \ |LINK5|\ , \ |LINK6|\ , \ |LINK7|\ , \ |LINK8|\ , \ |LINK9|\ , \ |LINK10|\ , \ |LINK11|\ , \ |LINK12|\ , \ |LINK13|\ .

|

.. _h387bd41572c6e60811453b41204663:

Vantaggi dell’uso di “Read the Docs”
====================================

L’uso di “\ |STYLE2|\ ” come piattaforma di pubblicazione di documenti ha i seguenti vantaggi sul formato “\ |STYLE3|\ ”:

|REPLACE4|


|REPLACE5|

|

.. _h3b6913a3a806b6bb385d6a194b578:

``GGeditor``, un componente aggiuntivo di Google doc
====================================================

\ |STYLE4|\  è un componente plugin che si installa direttamente da Google Doc (della suite di Google Drive). 

.. admonition:: Aggiornamento gennaio_2020

    Se da Google doc cliccando su “\ |STYLE5|\ ” non trovate “\ |STYLE6|\ ” - cercando sul Marketplace di Google (capita dall’agosto 2019 per una ridefinizione dei termini d’uso di Google) - potete cliccare direttamente sul \ |LINK14|\ .


.. sidebar:: Non scoraggiatevi!😵😭
    :subtitle: Se vi serve un file Google doc contenente il codice del componente aggiuntivo GGeditor ↓

    inviate un'email 👉 a \ |LINK15|\  con oggetto: “Google doc con codice componente aggiuntivo GGeditor”
    
    .. rubric:: non vi lascerò soli...↓
    così come non mi hanno lasciato solo coloro che con pazienza mi hanno insegnato ad usare questi preziosi strumenti 😉


.. admonition:: Aggiornamento 14_febbraio_2020

    In alternativa all’installazione del componente aggiuntivo su Google doc (dall’elenco dei componenti aggiuntivi forniti da Google), le funzioni svolte da GGeditor possono anche essere assicurate creando un Google doc che contiene uno script con il codice del componente GGeditor. Una volta creato lo script (con la procedura di seguito illustrata) avviando il comando “Commit to Github” (percorso: componenti aggiuntivi / GGeditor / Commit to Github), è possibile creare automaticamente un file in formato ``.RST`` su Github partendo dal contenuto editato su Google doc.
    
    ↓
    
    \ |STYLE7|\ 
    
    Lo script è costituito dai seguenti files che si trovano dentro il repository \ |LINK16|\ :
    
    * conversion.html
    
    * explicitMarkup.html
    
    * generator.gs
    
    * github.html
    
    * properties.gs
    
    * reSTMetadata.gs
    
    * settings.html
    
    * sidebar.html
    
    * 程式碼.gs   (程式碼 in cinese significa :guilabel:`codice`)
    
    Per creare lo script su Google doc, andare su \ |STYLE8|\  / \ |STYLE9|\ . Nella pagina dello script copiare il codice dei 9 file di cui al repository \ |LINK17|\  dando lo stesso nome dei 9 file di cui sopra. Allo script così creato dare il nome ``GGeditor``.


.. admonition:: Aggiornamento 19_febbraio_2020

    Messaggio “\ |STYLE10|\ ” (“Credenziali errate di Github”) su GGeditor. Github ha deprecato la sua API di autenticazione per “\ |STYLE11|\ ” e “\ |STYLE12|\ ”, che è la causa principale del problema del messaggio “Bad Credential” ("Credenziali non valide"). \ |LINK18|\ , basta sostituire la password con cui si entra nell'account Github con il  "\ |STYLE13|\ " quando si esegue il commit in GGEditor nel Google doc. I passi da seguire sono i seguenti:
    
    #. Vai alla \ |LINK19|\  e \ |STYLE14|\  in Github.com (\ |LINK20|\ ). Quindi copia il token di accesso personale negli appunti.
    
    #. Apri un documento Google e rimuovi tutte le credenziali archiviate precedentemente in GGEditor, quindi aggiungi un nuovo account Github con il token copiato come password.


|REPLACE6|


|REPLACE7|

|

.. _h7f3a342a4be53407b632069722a6:

L’utilità di ``GGeditor`` per i progetti di documentazione online
=================================================================

Il componente aggiuntivo \ |STYLE15|\  rappresenta uno strumento molto utile e comodo in quanto i servizi di Google Drive oggi sono molto usati anche nelle Pubbliche Amministrazioni, oltre che dai privati, per la facilità d’uso e per la funzionalità di condivisione dei documenti in gruppo.

Il lavoro principale che svolge il componente aggiuntivo \ |STYLE16|\  è quello di trasformare il testo editato su un foglio di Google doc in un file con linguaggio ``.rST`` dentro il repository di \ |STYLE17|\ . Github a sua volta permette la compilazione automatica dello stesso documento su \ |STYLE18|\ . Sembra una cosa difficile nella descrizione, ma posso assicurare che se lo faccio \ |LINK21|\  lo possono fare tutti.

|REPLACE8|

|


.. admonition:: Le principali funzioni e punti di forza di GGeditor sono

    * Facile inizio per chi non ha dimestichezza con i file RST, anche per chi non ha idea dei marcatori di RST.
    
    * Alimentato da Google Docs. Quasi la totalità di quello che vedi su Google Docs è quello che ottieni su Read the Docs. Lo stesso è per l'intero gruppo di lavoro.
    
    * Un click per commissionare il lavoro sul repository di Github.
    
    * Puoi vedere in anteprima il file RST generato dall'interno di Google Docs e scaricarlo nel tuo PC.
    
    * Supporta headings, bold, italic, hyperlink, subscript e superscript.
    
    * Supporta note a margine, immagini, liste di articolo e tabelle.
    
    * Supporta caratteri a larghezza intera (CKJ) nelle intestazioni e nelle tabelle.
    
    * Supporta i link interni ai bookmarks, headings e le Google Docs tabelle native di contenuti (in document table of contents).
    
    * Supporta i link relativi ai file RST generati dai Google Docs all'interno della stessa directory e sotto-directory Google Docs.
    
    * Supporta la tabella dei contenuti  (cross-document table of content (.. toctree::)) per fare generare l'indice a Read The Docs.
    
    * Supporta tutti gli stili di "admonitions" di Read The Docs.
    
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
    sintassi-md
    pubblicare-su-docs-italia
    licenza
    opendatasicilia


..  Tip:: 

    ♞ il contenuto di questa pagina che staI leggendo è editato in \ |LINK22|\ 


|REPLACE9|


.. bottom of content


.. |STYLE0| replace:: **Google doc**

.. |STYLE1| replace:: **Read the Docs**

.. |STYLE2| replace:: **Read the Docs**

.. |STYLE3| replace:: **PDF**

.. |STYLE4| replace:: **GGeditor**

.. |STYLE5| replace:: *installa componente aggiuntivo*

.. |STYLE6| replace:: **GGeditor**

.. |STYLE7| replace:: **I file contenuti nello script da creare su Google doc**

.. |STYLE8| replace:: **menu strumenti**

.. |STYLE9| replace:: **< > editor di script**

.. |STYLE10| replace:: **Bad Credential**

.. |STYLE11| replace:: *nome utente*

.. |STYLE12| replace:: *password*

.. |STYLE13| replace:: **token di accesso personale**

.. |STYLE14| replace:: **crea un token di accesso personale**

.. |STYLE15| replace:: **GGeditor**

.. |STYLE16| replace:: **GGeditor**

.. |STYLE17| replace:: **Github**

.. |STYLE18| replace:: **Read the Docs**


.. |REPLACE1| raw:: html

    <img alt="undefined" src="https://img.shields.io/github/last-commit/cirospat/googledocs-to-readthedocs.svg?colorB=%2300bfff&label=ultimo%20aggiornamento&style=flat">
.. |REPLACE2| raw:: html

    <p><span style="background-color: #6462d1; color: #ffffff; display: inline-block; padding: 3px 8px; border-radius: 10px;">Passando automaticamente da Github!</span></p>
.. |REPLACE3| raw:: html

    <img src="https://googledocs.readthedocs.io/it/latest/_images/gdocs-rtd_1.png" />
.. |REPLACE4| raw:: html

    <p><span style="background-color: #6462d1; color: #ffffff; display: inline-block; padding: 3px 8px; border-radius: 10px;">Responsive</span> </p>
    
    <p><span style="background-color: #105618; color: #ffffff; display: inline-block; padding: 3px 8px; border-radius: 10px;">Funzioni avanzate di ricerca testo</span> </p>
    
    <p><span style="background-color: #14c9ab; color: #ffffff; display: inline-block; padding: 3px 8px; border-radius: 10px;">Fornisce testo in HTML, EPUB e PDF</span> </p>
    
    <p><span style="background-color: #e86514; color: #ffffff; display: inline-block; padding: 3px 8px; border-radius: 10px;">Codice sorgente del testo online</span> </p>
    
    <p><span style="background-color: #c914c0; color: #ffffff; display: inline-block; padding: 3px 8px; border-radius: 10px;">E’ elegante e bello da vedere</span> </p>
.. |REPLACE5| raw:: html

    <img src="https://raw.githubusercontent.com/cirospat/rtd-schematipo/master/static/robin_batman.PNG" />
.. |REPLACE6| raw:: html

    <span style="background-color: #e86514; color: #ffffff; display: inline-block; padding: 3px 8px; border-radius: 10px;">↓ Guarda i passi da compiere nelle schermate di Github (aggiornamento 19_feb_2020)</span>
.. |REPLACE7| raw:: html

    <img src="https://ggeditor.readthedocs.io/en/latest/_images/Github_Bad_Credentials_1.png" alt="" width="650 />
.. |REPLACE8| raw:: html

    <iframe width="100%" height="500" src="https://www.youtube.com/embed/5O2D4h5hI18" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    Breve video introduttivo (2’10”)
.. |REPLACE9| raw:: html

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

    <a href="https://github.com/iapyeh" target="_blank">Hsin Yuan Yeh</a>

.. |LINK5| raw:: html

    <a href="https://twitter.com/aborruso" target="_blank">Andrea Borruso</a>

.. |LINK6| raw:: html

    <a href="https://coseerobe.gbvitrano.it/" target="_blank">Giovan Battista Vitrano</a>

.. |LINK7| raw:: html

    <a href="https://pigrecoinfinito.wordpress.com/" target="_blank">Salvatore Fiandaca</a>

.. |LINK8| raw:: html

    <a href="https://twitter.com/pablopersico78" target="_blank">Pablo Persico</a>

.. |LINK9| raw:: html

    <a href="https://twitter.com/marinabbasta" target="_blank">Marina Bassi</a>

.. |LINK10| raw:: html

    <a href="https://twitter.com/AndyReMagio" target="_blank">Andrea Ivan Baldassarre</a>

.. |LINK11| raw:: html

    <a href="https://twitter.com/rizzodnl" target="_blank">Daniele Rizzo</a>

.. |LINK12| raw:: html

    <a href="https://twitter.com/CostaMaurizio4" target="_blank">Maurizio Costa</a>

.. |LINK13| raw:: html

    <a href="https://twitter.com/m_stentella" target="_blank">Michela Stentella</a>

.. |LINK14| raw:: html

    <a href="https://chrome.google.com/webstore/detail/piedgdbcihbejidgkpabjhppneghbcnp/publish-accepted?authuser=0&hl=en" target="_blank">link del componente aggiuntivo GGeditor</a>

.. |LINK15| raw:: html

    <a href="mailto:cirospat@gmail.com">cirospat@gmail.com</a>

.. |LINK16| raw:: html

    <a href="https://github.com/cirospat/GGeditor_script" target="_blank">https://github.com/cirospat/GGeditor_script</a>

.. |LINK17| raw:: html

    <a href="https://github.com/cirospat/GGeditor_script" target="_blank">https://github.com/cirospat/GGeditor_script</a>

.. |LINK18| raw:: html

    <a href="https://ggeditor.readthedocs.io/en/latest/GithubBadCredentials.html" target="_blank">La soluzione è facile</a>

.. |LINK19| raw:: html

    <a href="https://github.com/settings/tokens" target="_blank">pagina delle impostazioni in Github.com</a>

.. |LINK20| raw:: html

    <a href="https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line" target="_blank">How to by Github</a>

.. |LINK21| raw:: html

    <a href="https://cirospat.readthedocs.io" target="_blank">io</a>

.. |LINK22| raw:: html

    <a href="https://docs.google.com/document/d/1L53rUYYMd5-UJUv6nj87uE6giZXHb9n4BsRemodCevI/" target="_blank">questo Google Doc</a>

