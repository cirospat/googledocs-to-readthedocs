
.. _h536951b201c66601516d7823355c44:

Caratteristiche di ``GGeditor``
*******************************

.. _h403f631c642863610673372f386278:

Da Google Doc a Read the Docs
=============================

\ |IMG1|\ 

Oggi il formato PDF rappresenta il principale formato di testo per la pubblicazione di documenti sia da parte della Pubblica Amministrazione che dai soggetti privati.

#. Purtroppo il PDF è un formato che non si adatta ai display piccoli dei dispositivi mobili, ed oggi la fruizione dei contenuti del web è molto consistente sui dispositivi mobili. 

#. In più il formato PDF non consente un agevole e facile ricerca di parole all'interno del documento.

Queste due criticità lo rendono un formato ormai vetusto nel 2018, non più rispondente alle esigenze di fruibilità di contenuti documentali su display di dimensioni contenute (smartphone, tablet).

``GGeditor`` soddisfa questi requisiti rendendo la fruizione di un documento online un esperienza gradevole.


..  Important:: 

    Questa pagina che state leggendo deriva direttamente da \ |LINK1|\ 

|

..  Note:: 

    ``GGeditor`` consente di compilare documenti sulla piattaforma di repository codice Github, che a sua volta serve per illustrare i documenti su Read the Docs in maniera gradevole, e strutturata per la fruizione dei contenuti indicizzati ad albero (capitoli, paragrafi, sotto-paragrafi).

.. _h64552c6174542573751e1232e73f79:

GGeditor ed i file formato  .rst
================================

\ |IMG2|\ 

[il plugin ``GGeditor`` installabile da Google Docs (cercalo nei "Componenti aggiuntivi")]

|


..  Important:: 

    \ |LINK2|\  é un plug-in di Google Docs, creato dal taiwanese Hsin Yuan Yeh, che serve a generare file \ |STYLE0|\  (\ |LINK3|\ ) direttamente da Google Docs. Il file RST generato può essere compilato nel repository di Github direttamente dall'editor GG. La documentazione così creata su Google Docs può essere ospitata da \ |LINK4|\  venendo aggiornata automaticamente ad ogni aggiornamento del Google Docs

|

.. _h326df60552448603d593767751d0d:

Video tutorial di funzionamento di GGeditor
===========================================


|REPLACE1|

|

.. _h5d92650581a8042635e3d4b2ef7d7d:

Il processo che svolge GGeditor
===============================

\ |IMG3|\ 

[Questo è il processo svolto da ``GGeditor``: da Google Docs a GGeditor a Github a Readthedocs]

\ |STYLE1|\ 

\ |IMG4|\  \ |STYLE2|\  

Scrivi facilmente testo in un documento senza conoscere il linguaggio RST)

\ |STYLE3|\  

\ |IMG5|\ \ |STYLE4|\  

``GGeditor`` è un plug-in di Google Docs che automatizza il lavoro di compilazione sul repository di Github

\ |STYLE5|\  

\ |IMG6|\ \ |STYLE6|\ 

Il progetto sul repository di Github è fondamentale per esporre il documento da pubblicare su Read the Docs

\ |STYLE7|\  

\ |IMG7|\ \ |STYLE8|\ 

Read the Docs è la piattaforma che espone documenti con un efficace architettura dei contenuti, in un formato usabile da tutte le dimensioni di display e che permette una facile ricerca di parole nel testo

|

.. _h58156b41121c145b694d71b3e2a7618:

I file che GGeditor genera automaticamente su Github
====================================================

\ |IMG8|\ 

[immagine del repository di Github che mostra come i file RST vengono generati direttamente dall'interno di Google Docs tramite il plugin ``GGeditor``]


|REPLACE2|


.. bottom of content


.. |STYLE0| replace:: **RST**

.. |STYLE1| replace:: **da**

.. |STYLE2| replace:: **Google Docs**

.. |STYLE3| replace:: **a ↓**

.. |STYLE4| replace:: **GGeditor**

.. |STYLE5| replace:: **a ↓**

.. |STYLE6| replace:: **Github**

.. |STYLE7| replace:: **a ↓**

.. |STYLE8| replace:: **Readthedocs**


.. |REPLACE1| raw:: html

    <iframe width="100%" height="500" src="https://www.youtube.com/embed/PUswAbvpE7c" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
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

.. |LINK1| raw:: html

    <a href="https://docs.google.com/document/d/194fbf2vPA1f97tVznuqMv4XL4AhPl4BJ0YvMx2gmHn4/edit" target="_blank">questo doc sul Google Drive</a>

.. |LINK2| raw:: html

    <a href="http://ggeditor.readthedocs.io/" target="_blank">GGeditor</a>

.. |LINK3| raw:: html

    <a href="https://en.wikipedia.org/wiki/ReStructuredText" target="_blank">resStructuredText</a>

.. |LINK4| raw:: html

    <a href="https://readthedocs.org/" target="_blank">Readthedocs</a>


.. |IMG1| image:: static/gdocs-rtd_1.png
   :height: 250 px
   :width: 504 px

.. |IMG2| image:: static/gdocs-rtd_2.png
   :height: 172 px
   :width: 273 px

.. |IMG3| image:: static/gdocs-rtd_1.png
   :height: 250 px
   :width: 504 px

.. |IMG4| image:: static/gdocs-rtd_3.png
   :height: 76 px
   :width: 57 px

.. |IMG5| image:: static/gdocs-rtd_4.png
   :height: 32 px
   :width: 134 px

.. |IMG6| image:: static/gdocs-rtd_5.png
   :height: 45 px
   :width: 49 px

.. |IMG7| image:: static/gdocs-rtd_6.png
   :height: 33 px
   :width: 134 px

.. |IMG8| image:: static/gdocs-rtd_7.png
   :height: 226 px
   :width: 500 px
