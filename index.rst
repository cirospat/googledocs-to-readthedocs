
|REPLACE1|

.. _h403f631c642863610673372f386278:

Da Google Doc a Read the Docs
*****************************

Questo documento rappresenta una via facile per migliorare la qualità dei documenti pubblicati sul web.

Oggi il formato PDF rappresenta il principale formato di testo per la pubblicazione di documenti sia da parte della Pubblica Amministrazione che dai soggetti privati.

Purtroppo il PDF è un formato che non si adatta ai display piccoli dei dispositivi mobili, ed oggi la fruizione dei contenuti del web è molto consistente sui dispositivi mobili. In più il formato PDF non consente un agevole e facile ricerca di parole all'interno del documento.

Queste due criticità lo rendono un formato ormai vetusto nel 2018, non più rispondente alle esigenze di fruibilità di contenuti documentali su display di dimensioni contenute (smartphone, tablet).

\ |LINK1|\  è un componente plug-in che si installa direttamente da Google Doc della suite di Google Drive. Google Drive (e i suoi servizi) oggi è molto usato anche nelle Pubbliche Amministrazioni, oltre che dai privati, per la facilità di condivisione dei documenti in gruppo.


..  Important:: 

    Questa pagina che state leggendo deriva direttamente da \ |LINK2|\ )

|

\ |STYLE0|\  consente di compilare documenti sulla piattaforma di repository codice Github, che a sua volta serve per illustrare i documenti su Read the Docs in maniera gradevole, e strutturata per la fruizione dei contenuti indicizzati ad albero (capitoli, paragrafi, sotto- paragrafi).

.. _h3092c7d75e1f5a466f42767b37185:

GGeditor ed i file RST
======================

\ |IMG1|\ 

[il plug-in GGeditor installabile da Google Docs (cercalo nei "Componenti aggiuntivi")]

|


..  Important:: 

    \ |LINK3|\  é un plug-in di Google Docs che serve a generare file \ |STYLE1|\  (\ |LINK4|\ ) direttamente da Google Docs. Il file RST generato può essere compilato nel repository di Github direttamente dall'editor GG. La documentazione così creata su Google Docs può essere ospitata da \ |LINK5|\  venendo aggiornata automaticamente ad ogni aggiornamento del Google Docs

|

.. _h326df60552448603d593767751d0d:

Video tutorial di funzionamento di GGeditor
===========================================


|REPLACE2|

|

.. _h5d92650581a8042635e3d4b2ef7d7d:

Il processo che svolge GGeditor
===============================

\ |IMG2|\ 


+----------+------------+-----------------+----------+
|Google    |GGeditor    |Github           |Read      |
|Docs      |addon       |                 |the Docs  |
+==========+============+=================+==========+
|\ |IMG3|\ |\ |IMG4|\   |\ |IMG5|\        |\ |IMG6|\ |
+----------+------------+-----------------+----------+
|edita     |trasmette   |Github prepara   |espone    |
|          |            |                 |          |
|→         |doc a Github|per pubblicazione|documento |
|          |            |                 |          |
|          |→           |→                |online    |
+----------+------------+-----------------+----------+

|

\ |STYLE2|\ 

\ |IMG7|\  \ |STYLE3|\  

(scrivi facilmente testo in un documento senza conoscere il linguaggio RST)

\ |STYLE4|\  

\ |IMG8|\ \ |STYLE5|\  

(GG editor è un plug-in di Google Docs che automatizza il lavoro di compilazione sul repository di Github)

\ |STYLE6|\  

\ |IMG9|\ \ |STYLE7|\ 

(Il progetto sul repository di Github è fondamentale per esporre il documento da pubblicare su Read the Docs)

\ |STYLE8|\  

\ |IMG10|\ \ |STYLE9|\ 

(Read the Docs è la piattaforma che espone documenti con un efficace architettura dei contenuti, in un formato usabile da tutte le dimensioni di display e che permette una facile ricerca di parole nel testo)

Questo è il processo svolto da GGeditor: da Google Docs a GGeditor a Github a Readthedocs

|

.. _h58156b41121c145b694d71b3e2a7618:

I file che GGeditor genera automaticamente su Github
====================================================

\ |IMG11|\ 

[immagine del repository di Github che mostra come i file RST vengono generati direttamente dall'interno di Google Docs tramite il plug-in GGeditor]

|

.. _h50b7ed1b74462d6e213e4c2f2e2b23:

Aspetti di GGeditor
===================

#. Facile inizio per chi non ha dimestichezza con i file RST, anche per chi non ha idea dei marcatori di RST.

#. Alimentato da Google Docs. Quasi la totalità di quello che vedi su Google Docs è quello che ottieni su Readthedocs. Lo stesso è per l'intero gruppo di lavoro.

#. Un click per commissionare il lavoro sul repository di Github.

#. Puoi vedere in anteprima il file RST generato dall'interno di Google Docs e scaricarlo nel tuo PC.

#. Supporta headings, bold, italic, hyperlink, subscript e superscript.

#. Support note a margine, immagini, liste di articolo e tabelle.

#. Supporta caratteri a larghezza intera (CKJ) nelle intestazioni e nelle tabelle.

#. Support i link interni ai bookmarks, headings e le Google Docs tabelle native di contenuti (in document table of contents).

#. Supporta i link relativi ai file RST generati dai Google Docs all'interno della stessa directory e sotto-directory Google Docs.

#. Supporta la tabella dei contenuti  (cross-document table of content (.. toctree::)) per fare generare l'indice a Readthedocs.

#. Supporta tutti gli stili di "admonitions" di Readthedocs.

#. Supporta account multipli per compilare i file nei repository di diversi account Github.

#. Supporta la conversione di tabelle con i tags HTML to let look-and-feel come la stessa cosa possibile per i blogger.

--------

.. _h292a20344d21577179215c531d397512:

Contenuti di questo documento 
******************************


.. toctree:: indice
    :maxdepth: 3

    come-usarlo
    tutorial
    user-guide

--------


|REPLACE3|

--------


|REPLACE4|


|REPLACE5|


.. bottom of content


.. |STYLE0| replace:: **GGeditor**

.. |STYLE1| replace:: **RST**

.. |STYLE2| replace:: **da**

.. |STYLE3| replace:: **Google Docs**

.. |STYLE4| replace:: **a ↓**

.. |STYLE5| replace:: **GGeditor**

.. |STYLE6| replace:: **a ↓**

.. |STYLE7| replace:: **Github**

.. |STYLE8| replace:: **a ↓**

.. |STYLE9| replace:: **Readthedocs**


.. |REPLACE1| raw:: html

    <a href="https://twitter.com/cirospat?ref_src=twsrc%5Etfw" class="twitter-follow-button" data-show-count="false">Follow @cirospat</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
.. |REPLACE2| raw:: html

    <iframe width="100%" height="380" src="https://www.youtube.com/embed/PUswAbvpE7c" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
.. |REPLACE3| raw:: html

    <h3>Servizi di<span>&nbsp;</span><a href="http://opendatasicilia.it/" rel="nofollow">OpendataSicilia</a></h3>
    <p><a href="http://accussi.opendatasicilia.it/index.html" rel="nofollow"><img src="https://camo.githubusercontent.com/24bc1b1450d155db547405fa90d92b6b34f4a132/68747470733a2f2f6369726f737061742e6769746875622e696f2f6d6170732f696d672f616363757373695f66617669636f6e2e706e67" alt="accussi" width="32" height="32" data-canonical-src="https://cirospat.github.io/maps/img/accussi_favicon.png" /></a>&nbsp; &nbsp;&nbsp;<a href="http://nonportale.opendatasicilia.it/index.html" rel="nofollow"><img src="https://camo.githubusercontent.com/7ad90a32a27ec7b68b3f5d1c9aec83d0bf5e4120/68747470733a2f2f6369726f737061742e6769746875622e696f2f6d6170732f696d672f6e6f6e706f7274616c655f66617669636f6e2e706e67" alt="non portale" width="32" height="32" data-canonical-src="https://cirospat.github.io/maps/img/nonportale_favicon.png" /></a>&nbsp;<span>&nbsp;</span><a href="http://petrusino.opendatasicilia.it/index.html" rel="nofollow"><img src="https://camo.githubusercontent.com/acae135c1a21da78bfd3423518810cd5465a8642/68747470733a2f2f6369726f737061742e6769746875622e696f2f6d6170732f696d672f706574727573696e6f5f66617669636f6e2e706e67" alt="petrusino" width="32" height="32" data-canonical-src="https://cirospat.github.io/maps/img/petrusino_favicon.png" /></a></p>
    <p><a href="http://albopop.it/" rel="nofollow">Albo Pop&nbsp;</a>/&nbsp;<a href="http://www.foiapop.it/" rel="nofollow">FOIA Pop&nbsp;</a>/&nbsp;<a href="http://www.visualcad.it/" rel="nofollow">Visual CAD</a></p>
    <p>Licenza aperta&nbsp;<a href="http://creativecommons.org/licenses/by-sa/4.0/" rel="nofollow"><img alt="Licenza Creative Commons" src="https://camo.githubusercontent.com/d1b3cb5c3bc0b0de6fb5445b1657c03464125482/68747470733a2f2f692e6372656174697665636f6d6d6f6e732e6f72672f6c2f62792d73612f342e302f38307831352e706e67" data-canonical-src="https://i.creativecommons.org/l/by-sa/4.0/80x15.png" /></a></p>
    <p><strong>OpendataSicilia</strong> &egrave; una iniziativa civica condivisa da pi&ugrave; persone, che si propone di far conoscere e diffondere la cultura dell'open government e le prassi dell'open data nel nostro territorio e aprire una discussione pubblica partecipata. Siamo anche su:</p>
    <ul>
    <li>la <a href="https://groups.google.com/forum/#!forum/opendatasicilia" target="_blank" rel="noopener">mailing list</a> di lavoro;</li>
    <li>il <a href="http://opendatasicilia.it" target="_blank" rel="noopener">blog</a>;</li>
    <li>il gruppo <a href="https://www.facebook.com/groups/opendatasicilia" target="_blank" rel="noopener">facebook</a>;</li>
    <li>l'account <a href="http://twitter.com/opendatasicilia" target="_blank" rel="noopener">twitter</a>;</li>
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

    <a href="http://ggeditor.readthedocs.io/" target="_blank">GGeditor</a>

.. |LINK2| raw:: html

    <a href="https://docs.google.com/document/d/1MEiFKrAxPg5pM5WuspQwo1Pnf54a77IjblL9UuvrHew/edit?usp=sharing" target="_blank">questo doc sul Google Drive</a>

.. |LINK3| raw:: html

    <a href="http://ggeditor.readthedocs.io/" target="_blank">GGeditor</a>

.. |LINK4| raw:: html

    <a href="https://en.wikipedia.org/wiki/ReStructuredText" target="_blank">resStructuredText</a>

.. |LINK5| raw:: html

    <a href="https://readthedocs.org/" target="_blank">Readthedocs</a>


.. |IMG1| image:: static/index_1.png
   :height: 172 px
   :width: 273 px

.. |IMG2| image:: static/index_2.png
   :height: 250 px
   :width: 504 px

.. |IMG3| image:: static/index_3.png
   :height: 64 px
   :width: 49 px

.. |IMG4| image:: static/index_4.png
   :height: 32 px
   :width: 134 px

.. |IMG5| image:: static/index_5.png
   :height: 45 px
   :width: 49 px

.. |IMG6| image:: static/index_6.png
   :height: 33 px
   :width: 134 px

.. |IMG7| image:: static/index_3.png
   :height: 76 px
   :width: 57 px

.. |IMG8| image:: static/index_4.png
   :height: 32 px
   :width: 134 px

.. |IMG9| image:: static/index_5.png
   :height: 45 px
   :width: 49 px

.. |IMG10| image:: static/index_6.png
   :height: 33 px
   :width: 134 px

.. |IMG11| image:: static/index_7.png
   :height: 226 px
   :width: 500 px
