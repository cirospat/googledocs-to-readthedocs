
.. _h177d435d25486f612146d312e31242a:

Inserimento di video, immagini e embedding nel documento
########################################################

.. _h1280345a324633724a27d6f35594b78:

Inserimento di immagini
***********************

Il componente aggiuntivo GGeditor permette all’utente di inserire immagini nello stesso documento. Lo stesso GGeditor pensa a creare dei file immagine dentro la cartella ``static`` nel repository creato su Github.

Tuttavia inserendo immagini in questa modalità, è stato riscontrato che nella visione da dispositivi mobili, le immagini tendono a comprimersi in maniera casuale, risultando non di gradevole impatto visivo.

Per superare questa criticità la procedura da seguire per inserire immagini nel documento Google è la seguente:

* cliccare “componenti aggiuntivi”,

* cliccare GGeditor

* cliccare Show Markup Panel

* cliccare sull’ultimo componente elencato, cioè “Embed HTML (tag,js…)

A questo punto dentro il box di colore bianco, andrà inserito il codice seguente

.. code:: 

    <img src="https://ggeditor.readthedocs.io/en/latest/_images/index_1.png" />

dove l\ |STYLE0|\  è quello dove si trova caricata (online) l’immagine.

E’ buona prassi caricare le immagini nella cartella ``static`` o in una cartella specificatamente dedicata, dentro il repository di Github, a raccogliere le immagini, e poi cliccando su ogni immagine, con tasto destro del mouse, cliccare su “copia l’indirizzo dell’immagine” e incollarlo nel box HTML dentro i doppi apici. Se si ha esigenza di dare all’immagine una misura in larghezza, dopo l’url dentro i doppi apici si inserirà ad esempio ``width=600`` dove 600 è il numero dei pixel in altezza dell’immagine dentro la pagina HTML del progetto Read the Docs.

|

.. _h3a515853385481e2c71204e67257357:

Inserimento di video (embedding)
********************************

E’ possibile inserire video all’interno dei documenti Google da far visualizzare poi nelle pagine HTML del progetto Read the Docs.

Nel caso di video di Youtube, l’azione da compiere è:

* cliccare “componenti aggiuntivi”,

* cliccare GGeditor

* cliccare Show Markup Panel

* cliccare sull’ultimo componente elencato, cioè “Embed HTML (tag,js…)

A questo punto dentro il box di colore bianco, andrà inserito il codice seguente

.. code:: 

    <iframe width="100%" height="500" src="https://www.youtube.com/embed/PUswAbvpE7c" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

dove nella parte ``https://www.youtube.com/embed/PUswAbvpE7c`` l’ultima parte dopo \ |STYLE1|\  cioè ``PUswAbvpE7c`` è quella che identifica univocamente il singolo video che vogliamo inserire nel documento da pubblicare.

Nel caso di video di \ |STYLE2|\ , la stessa piattaforma fornisce un codice per effettuare la modalità di ``embedding`` (incorporamento). Basta inserire il codice fornito da Vimeo per ogni video nel box HTML dentro il Google doc.

|

.. _h285e3559587b126e77516c374479419:

Inserimento di mappe interattive (embedding)
********************************************

Per ottenere, nel documento da pubblicare, una mappa interattiva come questa di seguito mostrata, è necessario inserire un box HTML (tramite lo strumento del “Show Markup Panel” all’interno del quale inserire il seguente codice:

.. code:: 

    <iframe width="100%" height="600px" frameBorder="0" allowfullscreen src="https://umap.openstreetmap.fr/it/map/spazi-verdi-fruibili-a-palermo-italia_14577#12/38.1529/13.3673?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=caption&captionBar=false"></iframe></br><a href="https://umap.openstreetmap.fr/es/map/spazi-verdi-fruibili-a-palermo-italia_14577">Visualizza a schermo intero</a>

dove ``height=”600px”`` indica l’altezza del riquadro che include la mappa, cioè quella mappa avrà un'altezza di 600 pixel e tale dato può essere variato in ragione delle esigenze del redattore del documento. 

|REPLACE1|

|


|REPLACE2|


.. bottom of content


.. |STYLE0| replace:: **’url**

.. |STYLE1| replace:: **/embed/**

.. |STYLE2| replace:: **Vimeo**


.. |REPLACE1| raw:: html

    <iframe width="100%" height="600px" frameBorder="0" allowfullscreen src="https://umap.openstreetmap.fr/it/map/spazi-verdi-fruibili-a-palermo-italia_14577#12/38.1529/13.3673?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=caption&captionBar=false"></iframe></br><a href="https://umap.openstreetmap.fr/es/map/spazi-verdi-fruibili-a-palermo-italia_14577">Visualizza a schermo intero</a>
.. |REPLACE2| raw:: html

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