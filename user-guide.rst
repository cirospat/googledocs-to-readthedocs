
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

    E' importante sapere che prima di effettuare questa operazione illustrata nella figura di sopra, è necessario creare il nome del progetto su Github, in maniera tale che quando seguiamo le operazioni della figura (dalla 1 alla 5) indichiamo a Github il nome del progetto nel quale GGeditor deve andare a creare il file che prende lo stesso nome del titolo del Google Doc, in più GGeditor provvede ad aggiungere il suffisso ".rst" dentro la directory "doc" di Github.

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

    Il GGeditor manterrà i file immagini su una cartella ("static") del progetto su Github. Se nel Doc vengono modificate immagini o anche vengono cancellate o sostituite, ogni volta bisogna cliccare su "commit images".


..  Attention:: 

    Se avete molte immagini in un Doc, il che significa molte immagono da caricare su Github tramite GGeditor, potrebbe succedere di incontrare situazioni di immagini rotte nelle corrispondenti pagine HTML di Read the Docs.
    Questo perchè il processo di rigenerazione delle pagine HTML è ancora in corso, non dovete -quindi- preoccuparvi. In questo caso dovete aspettare ancora un po che finisca il processo di costruzione delle stesse pagine su Read the Docs. Oppure se le immagini non compaiono ancora nelle pagine HTML, un ultima cosa da fare è andare nella pagina "Administration" del progetto su Read the Docs e cliccare su "Saving".
    
    Comunque se vedi immagini vecchie e non rispondenti all'ultima versione del Doc, elimina la cache del browser o controlla sul repository di Github la corrispondenza delle foto di Doc con quelle nella cartella "static" su Github.

.. _h132d7f7f1b3e1a3d73666d401101e7d:

Conversione
===========

Per la \ |STYLE0|\  si fa riferimento a \ |LINK1|\ 


|REPLACE1|


|REPLACE2|


.. bottom of content


.. |STYLE0| replace:: **conversione**


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

    <a href="http://ggeditor.readthedocs.io/en/latest/User%20Guide.html#conversion" target="_blank">questo paragrafo del tutorial di GGeditor</a>


.. |IMG1| image:: static/user-guide_1.png
   :height: 494 px
   :width: 601 px

.. |IMG2| image:: static/user-guide_2.png
   :height: 304 px
   :width: 600 px

.. |IMG3| image:: static/user-guide_3.png
   :height: 52 px
   :width: 152 px
