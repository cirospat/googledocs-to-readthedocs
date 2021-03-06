
.. _h7c3078395a79661a4b65806a4d21442:

Sintassi del linguaggio Markdown (MD) per le finalità di ‘Read the Docs’
########################################################################

Questa pagina illustra alcune guide online per i requisiti che i file di tipo \ |STYLE0|\  ``.MD`` devono possedere al fine di compilare le ‘builds’ su Read the Docs.

Infatti oltre al formato ReStructuredText ``.RST`` anche il formato MarkDown  ``.MD`` può compilare le ‘builds’ su Read the Docs per la visualizzazione dei contenuti nelle pagine HTML.


..  Note:: 

    Questa pagina di tutorial nasce dall’esperienza vissuta nel costruire il tutorial \ |LINK1|\ , una guida “\ |STYLE1|\ ”. 


+-------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
|Sintassi di base del linguaggio Markdown                                                                                 |\ |LINK2|\                                                                             |
+-------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
|Basic writing and formatting syntax. Create sophisticated formatting for your prose and code on GitHub with simple syntax|\ |LINK3|\                                                                             |
+-------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
|Una breve guida al linguaggio Markdown                                                                                   |\ |LINK4|\                                                                             |
+-------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
|Un tool online per editare codice in Markdown                                                                            |\ |LINK5|\                                                                             |
+-------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
|Una guida Read the Docs sul linguaggio Markdown                                                                          |\ |LINK6|\  (con utili analisi comparative tra sintassi del linguaggio MarkDown e HTML)|
+-------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
|Project documentation with Markdown                                                                                      |\ |LINK7|\                                                                             |
+-------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
|markdown-it ``demo``                                                                                                     |\ |LINK8|\                                                                             |
+-------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+

|

.. _h6c1f7a017361b2c2d521461f614336:

Fare leggere i file in formato “.md” a Read the Docs
****************************************************

Come descritto in questa \ |LINK9|\ , si possono fare leggere file in formato  ``.md `` a Read the Docs.

Azioni da effettuare:

1. bisogna creare un file ``requirements.txt`` che ha il seguente contenuto:

.. code-block:: python
    :linenos:

    sphinx-rtd-theme
    sphinx
    recommonmark
    markdown
    sphinx-markdown-tables

2. bisogna aggiungere nel file ``conf.py`` le seguenti istruzioni.

Dopo ``import sys, os`` inserire il seguente codice:

.. code-block:: python
    :linenos:

    import recommonmark
    from recommonmark.transform import AutoStructify
    # Add any paths that contain templates here, relative to this directory.
    templates_path = ['_templates']
    html_static_path = ['static']
    def setup(app):
        # overrides for wide tables in RTD theme
        app.add_stylesheet('theme_overrides.css') # path relative to static
    
    app.add_stylesheet('theme_overrides.css') # path relative to static
    source_parsers = {
        '.md': 'recommonmark.parser.CommonMarkParser',
    }
    
    source_suffix = ['.rst', '.md']
    
    extensions = ['sphinx.ext.ifconfig','sphinx_markdown_tables']

``source_suffix = '.rst'`` si trasformerà in ``source_suffix = ['.rst', '.md']`` 

|


|REPLACE1|


.. bottom of content


.. |STYLE0| replace:: **Markdown**

.. |STYLE1| replace:: *per rispondere alle numerose richieste di aiuto sull’uso del calcolatore di campi e per colmare un vuoto sulla guida online di QGIS con esempi e molti screenshot*


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

.. |LINK1| raw:: html

    <a href="http://hfcqgis.readthedocs.io" target="_blank">http://hfcqgis.readthedocs.io</a>

.. |LINK2| raw:: html

    <a href="https://www.markdownguide.org/basic-syntax" target="_blank">https://www.markdownguide.org/basic-syntax</a>

.. |LINK3| raw:: html

    <a href="https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax#styling-text" target="_blank">https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax#styling-text</a>

.. |LINK4| raw:: html

    <a href="https://www.html.it/articoli/markdown-guida-al-linguaggio" target="_blank">https://www.html.it/articoli/markdown-guida-al-linguaggio</a>

.. |LINK5| raw:: html

    <a href="https://stackedit.io/app#" target="_blank">https://stackedit.io/app#</a>

.. |LINK6| raw:: html

    <a href="https://markdown-guide.readthedocs.io" target="_blank">https://markdown-guide.readthedocs.io</a>

.. |LINK7| raw:: html

    <a href="https://www.mkdocs.org" target="_blank">https://www.mkdocs.org</a>

.. |LINK8| raw:: html

    <a href="https://markdown-it.github.io/" target="_blank">https://markdown-it.github.io/</a>

.. |LINK9| raw:: html

    <a href="https://github.com/opendatasicilia/tansignari/issues/106" target="_blank">issue</a>

