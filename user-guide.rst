
.. _h03e36184a274f643d276c3036316164:

User-guide (gli step operativi)
*******************************

.. _h713143325814353613281e551531322a:

Consegnare i file (da Google Doc) a Github
==========================================

Una volta effettuato l'accesso a Github (dall'interno di Google Doc) e terminata la compilazione del testo su Google Doc si passa all'operazione di commissionamento del file a Github. La finestra di GGeditor guida alla creazione del file di Google Doc dentro il progetto di Github. La procedura guidata dalla finestra di GGeditor è abbastanza intuitiva.

\ |IMG1|\ 

Una volta cliccato OK per il commit s Github, verrà creato un file RST sulla cartella "doc" dentro il progetto di Github.


..  Attention:: 

    E' importante sapere che prima di effettuare questa operazione illustrata nella figura di sopra, è necessario creare il nome del progetto su Github, in maniera tale che quando seguiamo le operazioni della figura (dalla 1 alla 5) indichiamo a Github il nome del progetto nel quale GGeditor deve andare a creare il file che prende lo stesso nome del titolo del Google Doc, in più GGeditor provvede ad aggiungere il suffisso ".rst" dentro la directory madre di Github.

If you want to commit to a new file. Please

#. Navigate to the folder where the new file would be

#. Click on the “New File” item

#. Give the file name to create. The name will be suffix with “.rst” automatically.

.. _h572153e49969743e69262f2d637743:

Committing
----------

\ |IMG2|\ 

[la finestra che ci indica il Google Doc che dobbiamo inviare in una cartella (".doc") del progetto su Github]

\ |IMG3|\ Se solo il testo è stato modificato nel Doc, puoi evitare di flaggare il tasto “Commit images” per escludere il commit a Github delle immagini, questo porterà a una riduzione dei tempi dell'effettuazione del processo di commit.


..  Note:: 

    GGeditor posizionerà i file immagini presenti nel Google doc sulla cartella ``static`` del progetto su Github. Se nel Google doc vengono modificate immagini o anche vengono cancellate o sostituite, ogni volta bisogna cliccare sul componente aggiuntivo GGeditor e quindi su "commit images".


..  Attention:: 

    Se avete molte immagini in un Doc, il che significa molte immagini da caricare su Github tramite GGeditor, potrebbe succedere di incontrare situazioni di immagini rotte nelle corrispondenti pagine HTML di Read the Docs.
    Questo perché il processo di rigenerazione delle pagine HTML è ancora in corso, non dovete -quindi- preoccuparvi. In questo caso dovete aspettare ancora un po che finisca il processo di costruzione delle stesse pagine su Read the Docs. Oppure se le immagini non compaiono ancora nelle pagine HTML, un ultima cosa da fare è andare nella pagina "\ |STYLE0|\ " del progetto su Read the Docs e cliccare su "\ |STYLE1|\ ".
    
    Comunque se vedi immagini vecchie e non rispondenti all'ultima versione del Doc, elimina la cache del browser o controlla sul repository di Github la corrispondenza delle foto del Google doc con quelle nella cartella ``static`` su Github.

.. _h534e17712232613c42586df1412f1b:

Limitazioni 
============

\ |LINK1|\  da Google Doc sui file reST:

* Comments. This is not supported by the reST\ [#F1]_\ .

* Drawing objects. Because there is no API to get it as an image.

* List styles. The list style is defined by the CSS settings in the html page.

* Math equations. Because this is no API to get it as an image.

* Multi-columns. This is not supported by the reST.

* Page break. This is not able to apply to a html page.

* Page header and page footer. This is not supported by the reST.

* Page numbering. This is not able to apply to a html page.

* Internal link to heading does not work. Currently there is no API to identifiy the target heading element. Please use “Bookmark“ instead.

* Bold and italic styles in footnote content does not exposed by Doc’s API. Which means bold and italic text is rendered as normal text in footnote content.

.. _h664e1b56760748493264151c256561:

Strumenti per i più esperti
***************************

.. _h132d7f7f1b3e1a3d73666d401101e7d:

Conversione
===========

Per la \ |STYLE2|\  del testo da Google Doc al formato RST (e anche previsto il download del file RST) si fa riferimento a \ |LINK2|\ .

.. _h2b426234521b486d3a6d7e3d167d91b:

Api Docs
========

Per \ |STYLE3|\  si fa riferimento a \ |LINK3|\ .

.. _h2e427c26763f767566236c4a5e2d6c14:

Backend
=======

Documentazione specificata nel \ |LINK4|\ . Si fa \ |LINK5|\ .


|REPLACE1|


|REPLACE2|


.. bottom of content


.. |STYLE0| replace:: **Administration**

.. |STYLE1| replace:: **Saving**

.. |STYLE2| replace:: **conversione**

.. |STYLE3| replace:: **API document for a Python module**


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

    <a href="http://ggeditor.readthedocs.io/en/latest/Limitations.html" target="_blank">Funzioni non supportate</a>

.. |LINK2| raw:: html

    <a href="http://ggeditor.readthedocs.io/en/latest/User%20Guide.html#conversion" target="_blank">questo paragrafo del tutorial di GGeditor</a>

.. |LINK3| raw:: html

    <a href="http://ggeditor.readthedocs.io/en/latest/ApiDoc.html" target="_blank">questo paragrafo del tutorial di GGeditor</a>

.. |LINK4| raw:: html

    <a href="http://google.github.io/styleguide/pyguide.html" target="_blank">Google Python Style Guide</a>

.. |LINK5| raw:: html

    <a href="http://ggeditor.readthedocs.io/en/latest/api/backend.html" target="_blank">riferimento a questo paragrafo del tutorial di GGeditor</a>



.. rubric:: Footnotes

.. [#f1]  per i commenti usa il servizio di hypothes.is illustrato in  `questa pagina de tutorial <http://googledocs.readthedocs.io/it/latest/hypothesis-partecipazione.html>`__ 

.. |IMG1| image:: static/user-guide_1.png
   :height: 494 px
   :width: 601 px

.. |IMG2| image:: static/user-guide_2.png
   :height: 304 px
   :width: 600 px

.. |IMG3| image:: static/user-guide_3.png
   :height: 52 px
   :width: 152 px
