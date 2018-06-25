
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

La procedura è stata definita da \ |LINK2|\  al quale va un ringraziamento per questa importante integrazione su Read the Docs.

C'è un feed RSS per le note di ogni pagina HTML. Ad esempio:

\ |LINK3|\  ``url-di-readthedocs`` / ``pagina-specifica-del-documento-readthedocs``.html

C'è anche in formato JSON:

\ |LINK4|\  ``url-di-readthedocs`` / ``pagina-specifica-del-documento-readthedocs``.html

Tanti modi per seguire i commenti sulle pagine di Read the Docs, e per attivare eventuali notifiche automatiche.


.. bottom of content


.. |LINK1| raw:: html

    <a href="https://web.hypothes.is/" target="_blank">hypothes.is</a>

.. |LINK2| raw:: html

    <a href="https://twitter.com/aborruso" target="_blank">Andrea Borruso</a>

.. |LINK3| raw:: html

    <a href="https://hypothes.is/stream.rss?uri=" target="_blank">https://hypothes.is/stream.rss?uri=</a>

.. |LINK4| raw:: html

    <a href="https://hypothes.is/api/search?url=" target="_blank">https://hypothes.is/api/search?url=</a>

