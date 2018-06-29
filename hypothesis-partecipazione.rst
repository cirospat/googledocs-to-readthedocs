
.. _h6d46677b7505a86515774b7b35546d:

Hypothes.is per partecipare ad un documento su Read the Docs
############################################################

Al fine di permettere la partecipazione di utenti che intendono commentare un documento pubblicato su Read the Docs viene in aiuto la piattaforma \ |LINK1|\ .

Di seguito vengono esposte dettagliatamente le procedure da seguire per integrare hypothes.is su Read the Docs.

A

Aggiungere ``templates_path = ['_templates']`` al file  ``conf.py``.

B

Creare nel repo una cartella ``_templates``, e all’interno della cartella creare un file ``layout.html`` ed in questo file inserire il seguente codice:


.. code:: 

    {% extends "!layout.html" %}
    {% block extrahead %}
    {{ super() }}
        <script src="https://hypothes.is/embed.js" async></script>
    {% endblock %}

Tutto qui.

La procedura è stata definita da \ |LINK2|\  al quale va un ringraziamento per questa importante integrazione su Read the Docs. Andrea ha sperimentato per la prima volta  l’applicazione di questa procedura sul progetto del \ |LINK3|\ .

|

.. _ha4d55555d1c27693371432ac737318:

Le annotazioni su hypothes.is disponibili in tempo reale in un feed RSS o in un formato Json
********************************************************************************************

\ |STYLE0|\ . Ad esempio:

\ |LINK4|\  ``url-di-readthedocs`` / ``pagina-specifica-del-documento-readthedocs``.html


..  Note:: 

    Guarda, ad esempio, il feed RSS delle annotazioni postate dagli utenti come commenti ad un apagina del Libro bianco dell’innovazione della PA 2018: 
    \ |LINK5|\  

Esempio di visualizzazione del feed rss dei commenti ad una pagina (html) del Libro bianco innovazione PA 2018 

|REPLACE1|

\ |STYLE1|\ :

\ |LINK6|\  ``url-di-readthedocs`` / ``pagina-specifica-del-documento-readthedocs``.html

Sono diversi modi per seguire i commenti sulle pagine di Read the Docs, e per attivare eventuali notifiche automatiche.

|


|REPLACE2|


.. bottom of content


.. |STYLE0| replace:: **C'è un feed RSS per le note di ogni pagina HTML**

.. |STYLE1| replace:: **C'è anche in formato JSON**


.. |REPLACE1| raw:: html

    <iframe width="100%" height="500px" frameBorder="0" src="https://hypothes.is/stream.rss?uri=https://forumpa-librobianco-innovazione-2018.readthedocs.io/it/latest/2-nuovi-processi.html"></iframe>
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

    <a href="https://web.hypothes.is/" target="_blank">hypothes.is</a>

.. |LINK2| raw:: html

    <a href="https://twitter.com/aborruso" target="_blank">Andrea Borruso</a>

.. |LINK3| raw:: html

    <a href="http://forumpa-librobianco-innovazione-2018.readthedocs.io" target="_blank">Libro bianco dell’innovazione della PA, 2018, del ForumPA</a>

.. |LINK4| raw:: html

    <a href="https://hypothes.is/stream.rss?uri=" target="_blank">https://hypothes.is/stream.rss?uri=</a>

.. |LINK5| raw:: html

    <a href="https://hypothes.is/stream.rss?uri=https://forumpa-librobianco-innovazione-2018.readthedocs.io/it/latest/2-nuovi-processi.html" target="_blank">https://hypothes.is/stream.rss?uri=https://forumpa-librobianco-innovazione-2018.readthedocs.io/it/latest/2-nuovi-processi.html</a>

.. |LINK6| raw:: html

    <a href="https://hypothes.is/api/search?url=" target="_blank">https://hypothes.is/api/search?url=</a>

