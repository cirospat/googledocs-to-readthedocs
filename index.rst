
.. _h305104c304e4b5e363d34c61406852:

Da Google Doc direttamente a Read the Docs con ``GGeditor``
###########################################################

Passando automaticamente da Github!

|REPLACE1|

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

|REPLACE2|

|

.. _h28105e656d4d48041184d771d3b4a1a:

GGeditor
========


|REPLACE3|

|

\ |LINK4|\  è un componente plugin che si installa direttamente da Google Doc (della suite di Google Drive) cercandolo nei componenti aggiuntivi e installandolo. Rappresenta uno strumento molto utile e comodo in quanto i servizi di Google Drive oggi sono molto usati anche nelle Pubbliche Amministrazioni, oltre che dai privati, per la facilità d’uso e per la funzionalità di condivisione dei documenti in gruppo.

Il lavoro principale che svolge il componente aggiuntivo GGeditor è quello di trasformare semplice testo editato su un foglio di Google doc in un file con linguaggio ``.rST`` dentro il repository di Github, che a sua volta permette la compilazione automatica dello stesso documento su Read the Docs.


|REPLACE4|

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
    tabelle
    licenza

--------

.. _h76f5da654649526d52795a54407f13:

Community opendatasicilia
=========================


|REPLACE5|


|REPLACE6|

--------


|REPLACE7|


.. bottom of content


.. |STYLE0| replace:: **Read the Docs**

.. |STYLE1| replace:: **PDF**


.. |REPLACE1| raw:: html

    <img src="https://ggeditor.readthedocs.io/en/latest/_images/index_1.png" />
.. |REPLACE2| raw:: html

    <p><span style="background-color: #6462d1; color: #ffffff; display: inline-block; padding: 3px 8px; border-radius: 10px;">Responsive</span></p>
    
    <p><span style="background-color: #105618; color: #ffffff; display: inline-block; padding: 3px 8px; border-radius: 10px;">Funzioni avanzate di ricerca testo</span></p>
    
    <p><span style="background-color: #14c9ab; color: #ffffff; display: inline-block; padding: 3px 8px; border-radius: 10px;">Fornisce testo in HTML, EPUB e PDF</span></p>
    
    <p><span style="background-color: #e86514; color: #ffffff; display: inline-block; padding: 3px 8px; border-radius: 10px;">Codice sorgente del testo online</span></p>
    
    <p><span style="background-color: #c914c0; color: #ffffff; display: inline-block; padding: 3px 8px; border-radius: 10px;">E’ elegante e bello da vedere</span></p>
.. |REPLACE3| raw:: html

    <img src="https://ggeditor.readthedocs.io/en/latest/_images/index_2.png" alt="" width="800 />
    <br>
.. |REPLACE4| raw:: html

    <iframe width="100%" height="500" src="https://www.youtube.com/embed/5O2D4h5hI18" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    Breve video introduttivo (2’10”)
.. |REPLACE5| raw:: html

    <iframe width="100%" height="500" src="https://www.youtube.com/embed/Zj2Kosq-v6k" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    <span class="footer_small">Raduno della community di OpendataSicilia del 9 e 10 novembre 2018 a Palermo.</span>
    
.. |REPLACE6| raw:: html

    <h2><span style="font-size: 14px;"><a href="http://opendatasicilia.it" target="_blank" rel="noopener"> <img src="https://lh3.googleusercontent.com/zwfw9k4vxrCVft07wDWlOI1zvj9uwFci_qqgYw_iismQ4Mzy5DhpShKHSCe3LQpY8OI3JBhBHza6cttSdTy1pFulbUR0oRQmC8hsNgIl7PpkNIFq0Q0vQnzQ8nTInvSqT_8HwFPbkOVhHysNu8HJ0gDUJx2UM3mHmGosu79OuB-_z5FYoCeJCzrGauiYpsajp26ZdqUXkDrAEIIPQunaMOcFLOuXlo5mb-P7fM-OmfTrQPnUApXPwX5AY-VXxIdgXKMii1nAjutHE3Bk3owq5h8nyl0JVc-LKmzqGpcALq7FnfCXjdVicqqN5dN6INq1BdA_EfAz6B3BKQCIqXk-hge58dnP-lDUkkFl9HgMe4Xk4Yz5QRhcBdV1JZCU3k402sPE-Xi3xhD4-SWRwGbUUuiklRWSEg7262TdmSFb7wj2h-iB8tw308dZBEaIwHAbO7isHzgnSsGOEDdHZHCpl9SrYBxFVP15tUzaXJRqrE6wll67bMKkirzdRv4T0N2kgt_JudQZdhQ8n_LlXX5jyYhx4TKfSN8Alpq2nHsLCMhTG3xJXvuZOpChAaXYu0emQdXP0hClASLFcr7Pbpjb6VsRp3g58LvSexy0DOI=w781-h901-no" alt="" width="97" height="112" /></a>&nbsp;</span></h2>
    <p><strong><a href="http://opendatasicilia.it" target="_blank" rel="noopener">Opendatasicilia</a></strong>, community sulla cultura dei dati aperti &egrave; una iniziativa civica condivisa da pi&ugrave; persone, che si propone di far conoscere e diffondere la cultura dell&rsquo;open government e le prassi dell&rsquo;open data nel nostro territorio e aprire una discussione pubblica partecipata. Un gruppo di cittadini con diverse storie, competenze, professioni. Siamo accomunati dalla genuina volont&agrave; di contribuire a migliorare la qualit&agrave; della vita della nostra comunit&agrave;. Lo vogliamo fare con spirito di collaborazione e concretezza.&nbsp;</p>
    <p><strong><span style="background-color: #869da8; color: #ffffff; display: inline-block; padding: 2px 6px; border-radius: 10px;">Canali di comunicazione</span> </strong><span style="font-weight: 400;">&nbsp;di opendatasicilia:</span></p>
    <ul>
    <li style="font-weight: 400;"><span style="font-weight: 400;">la </span><a href="https://groups.google.com/forum/#!forum/opendatasicilia"><span style="font-weight: 400;">mailing list</span></a><span style="font-weight: 400;"> di lavoro (forum Google group);</span></li>
    <li style="font-weight: 400;"><span style="font-weight: 400;">il </span><a href="http://opendatasicilia.it/"><span style="font-weight: 400;">blog</span></a><span style="font-weight: 400;">;</span></li>
    <li style="font-weight: 400;"><span style="font-weight: 400;">il gruppo </span><a href="https://www.facebook.com/groups/opendatasicilia"><span style="font-weight: 400;">Facebook</span></a><span style="font-weight: 400;">;&nbsp;</span></li>
    <li style="font-weight: 400;"><span style="font-weight: 400;">il canale <a href="https://twitter.com/opendatasicilia" target="_blank" rel="noopener">Twitter</a>;</span></li>
    <li style="font-weight: 400;">il canale <a href="http://opendatasicilia.slack.com/">Slack</a> (<a href="http://slack.opendatasicilia.it/">per iscriversi</a>).</li>
    </ul>
    <p><strong><span style="background-color: #869da8; color: #ffffff; display: inline-block; padding: 2px 6px; border-radius: 10px;">Servizi </span></strong><span style="font-weight: 400;">&nbsp;a cura di Opendatasicilia:</span>&nbsp;</p>
    <p><a title="accuss&igrave; tutorial catalogue" href="http://accussi.opendatasicilia.it/index.html" target="_blank" rel="noopener"> <img src="https://camo.githubusercontent.com/24bc1b1450d155db547405fa90d92b6b34f4a132/68747470733a2f2f6369726f737061742e6769746875622e696f2f6d6170732f696d672f616363757373695f66617669636f6e2e706e67" alt="accussi" width="41" height="41" /></a>&nbsp;<a href="http://accussi.opendatasicilia.it/index.html" target="_blank" rel="noopener">accuss&igrave;</a>&nbsp; &nbsp; &nbsp;</p>
    <p><a title="petrusino" href="http://petrusino.opendatasicilia.it/index.html" target="_blank" rel="noopener"><img src="https://camo.githubusercontent.com/acae135c1a21da78bfd3423518810cd5465a8642/68747470733a2f2f6369726f737061742e6769746875622e696f2f6d6170732f696d672f706574727573696e6f5f66617669636f6e2e706e67" alt="petrusino" width="41" height="41" /></a>&nbsp;<a href="http://petrusino.opendatasicilia.it/index.html" target="_blank" rel="noopener">petrusino</a></p>
    <p><a title="non portale open data regione sicilia" href="http://nonportale.opendatasicilia.it/index.html" target="_blank" rel="nofollow noopener"> <img src="https://camo.githubusercontent.com/7ad90a32a27ec7b68b3f5d1c9aec83d0bf5e4120/68747470733a2f2f6369726f737061742e6769746875622e696f2f6d6170732f696d672f6e6f6e706f7274616c655f66617669636f6e2e706e67" alt="non portale" width="41" height="41" data-canonical-src="https://cirospat.github.io/maps/img/nonportale_favicon.png" /></a>&nbsp;<a href="http://nonportale.opendatasicilia.it/index.html" target="_blank" rel="noopener">non portale</a>&nbsp;&nbsp;</p>
    <p><a title="albopo" href="http://albopop.it/" target="_blank" rel="noopener"><img src="http://albopop.it/images/logo.png" width="41" height="41" /></a>&nbsp;<a href="http://albopop.it/" target="_blank" rel="noopener">albopop</a>&nbsp;&nbsp;</p>
    <p><a title="foia pop" href="http://foiapop.it/" target="_blank" rel="noopener"><img src="https://lh3.googleusercontent.com/5mPgjmfRCJ6mgv0-OjTNj8i_CiYEaMnXZ3LHs48QCQG7X2AiG9L87f8LgCKw2l2hMuHZmoBRIhuybiHWJgBEixT6mjL8YrEV9_4SpR0fPsVPPptqqc_fW16cA9th5jxVTuExQXQWAzu5kqYBDgtWpCVeTPw4OX2Fml6AVBMfmzO3gNL2H5jvRdGrqAV67P3Nrl-bJDvqlwXna3gAWikjxZRJzk925fBbth-h0Vs577x1fVD69y_Q7DWMBTjUgR9Y5YuKpoMGO6RfSY1zkcCEXdncFGf7uIk6EB2zvQvLeVDt4pqJFlf0JRbK4WLR7SsAvfKCz0cmlYkiRi4K9KalWnK1RhO08k2xsfZGsKf9aIVqL_K-r8SlW9HJ0cFkwcTRRD8lDPqurdxkIUKsYMY9Fx8MspczsPijqlJeu_AgsMPMwJjppfmgP951LS6fVgu99Csso2JaGk9BN0BWYpLk8e7pqBrvF0fR0jIBfiIAnzVj1loh4bER3n1W9FG0nvrh67fsngfMozKzDSBHvFoXchJoG2e83-r1CwWoEQK3tDazIhkpZkxzLCLJYi4fASURZPsi2a0XEsGxn7h70K4s6AWuQo8R6hMLenbpeG0=s53-no" alt="" width="44" height="44" /></a>&nbsp;<a href="http://foiapop.it/" target="_blank" rel="noopener">foiapop</a>&nbsp; &nbsp;&nbsp;</p>
    <p><a title="visual cad" href="http://www.visualcad.it/" target="_blank" rel="noopener"><img src="https://lh3.googleusercontent.com/zMrMz72sJ1JjKagZKoq-1gbg8TTLWIggKZ67vBsNRTUaUcd2Pm7dKGQXTVrl_bEQFbzG2DMYx06bmW-oN8VndQ2vqOHiibkKEMLjnS0AneovCNx58hyoaH3PqzxCt__5MKqYjepqzVbC7pNbQ1SEUaWtDGmcCReqV6bYaKLHCi6VIN5R18DjmIuVTh3nbUJYjbVsd2upIBITuJGKuErtFYzNk_f-nZ88I3W4KDbgHWBDVWf5Wx5My_b40QacDemr4YhVgSsJMQ9Si6inPNnJF9N9d2BcxW__sy8FSNll87wzH_Sk0Pw0a7e7oDjq0y4VNw0LJzXLl0KDBc-c3HX7GWrb2xY9VnUl2-hkaGID9g1nyvNMmSMreynpyn5Az9iqQ5KlcVJT7GehDHODDEeH25ktD3Nb3a2mmOv12SXh1ULuwIBWoqXFcRdFMSKG42XpR2Qs3tzj7RaE9kPKsCdmrr6AvbfNeELgQNBIJLKmPenJib5rgt-ddEhJr518SM2Ma5OGmW4uBQdooTAgxESB6Ir71qTBaXv9XcL_1_wBLbYC06PvKb3YoXnAl0Opx_zCR1bNMl5-yCpO58d7FEddNhmxKzcVQOOc-QWtEek=w192-h132-no" alt="" width="60" height="41" /></a>&nbsp;<a href="http://www.visualcad.it/" target="_blank" rel="noopener">visualcad</a></p>
    <p><a title="hfcqgis" href="http://hfcqgis.opendatasicilia.it/it/latest/" target="_blank" rel="noopener"><img src="https://lh3.googleusercontent.com/re2PpwOiIpZRKnmU2ZTk1xfoPxjk4xs3pc4yfbZkegGkmldMDujSCNWOSutMpmRo05YrS023YgeRfrt2Qg1_fpmw2_6gOpNPoyo_zMm7M14izw554KdGWbzvImZgNeQ_WX5Aho5zNL1kIZpyljZxW95WnX3KFBGzZdJ_NTZfwIK1iZQcooP5BLRQjJ9yrRS3-vg1Gm_Gor4xNlI6fXAV__ElF9A5R_Q4w--BbbOgd5yR2TWGvndO2Ol3CArQhhaf5WEcrzHtRV2l5wPRgopVgjf-Ysb33uKSa4hqt0sl0OYQLO4fwjhgOm2P1q5K-im7pMT61x9ePSgDi7G4t-MvxqjFDUnDlke614hazUshTcCPhVw2l6fxSdr_4q9XA8bHNtHs3s1N6tc4RUfSI6YK2jpPiEG1Ru_iD2slFPRrGAIS0cLaUiyLPIZuhngRvHOrkORlZlhl4gebM_Vh-xzQtPIdo3yiQZhDyorx0X1sJ0Mi6mQceqUPI-LpWANi8dp-jxKzotOHmaSUSFWtrmqjE4CECMSUNj8PwXSgEAjXUtyq641gpXcXRKdEI6mdF-yplGEKzxIsXmNCxuCt4OSEpw85X5JUwehxEXnuPlM=w256-h65-no" alt="" width="173" height="44" /></a> <a href="http://hfcqgis.opendatasicilia.it/it/latest/" target="_blank" rel="noopener">campi Qgis</a></p>
    <p><img src="https://lh3.googleusercontent.com/Hw4sOKZFQu9WOPYS1BXyHmBg7Rw0O3QIwA0uIywsX3oa0q6A3VUQSoZ23Zxr8tPhZkBrvk1e-huO7jD-y-lOhSw7sYHP_IbrSqQl-CT3SXN70yapNyalSyxnKcHBdEOdYZVZiy0HwCoFwxFygvavAtTyo5Vmq1xmfeIiGwoVIX-fzh5zdj1bBEHgK1ENQatv12YT45Edak8cxP7cN3InZRKX5_j_rthYAxUT8bDDe0A9OAI54vaHx_YX81JNyStBF1yvXBm6uGBIeA3POE5bbeisvKJ-76nA9WAWzk5T6BzZQt1YQASzbCoV_QLpi9wD267B0afkbuZSmrgW4NufoX_QCyL0Jp2KL417bAblfp8dvvOnLj73gIIDkq_qhQ85fYqRFictfZAFLinCP-qaDXdzn-Tyt7bNiPo6TXp3crYMNIGkMWNNyBYMq6IyAf5nVTSG3EpHO3wsgpQVXkOjItcH9CDdkUQkutwJvg9zYZtVbrOisPvhlx-Os9dKS1gjV-w-y_ABJ0KvuXO9DyOcvsnRfS_GNlWIcb2NApJHbwQ1HiV14zjmqBfVMlcvjjzWEkUCv0DtYk7SkdX9AIZ-RtldHVMmrA=s91-w91-h32-no" alt="openars" width="91" height="32" />&nbsp;<a href="http://www.openars.org/" target="_blank" rel="noopener" title="openars">openARS</a></p>
    <a href="https://twitter.com/opendatasicilia?ref_src=twsrc%5Etfw" class="twitter-follow-button" data-show-count="false">Follow @opendatasicilia</a>
      <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    
.. |REPLACE7| raw:: html

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

