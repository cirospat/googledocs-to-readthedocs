
.. _h7d4d73362b291793a962411315d6b:

Il lavoro da fare su Read the Docs
##################################

Questa rappresenta la fase finale del lavoro ed è molto semplice come operazioni da effettuare. Una volta completato il lavoro di compilazione su Github, bisogna andare su \ |LINK1|\  e (dopo aver creato il relativo account) importare il progetto, già creato, da Github.

Nella finestra, su URL del Deposito Codice bisogna scrivere l’URL del progetto che avete creato su Github, e quindi scegliere il nome del progetto, esempio:

“linee guida open data comune vattelapesca”

e lasciare Tipo del Deposito Codice selezionato su Git.

A quel punto verrà messo in collegamento il vostro progetto di Github con la piattaforma di Red the Docs. 

Una primissima cosa da fare è andare su Amministrazione e settare la lingua italiana. Questo consentirà a Read the Docs di aggiungere al titolo del vostro progetto la desinenza ``/it/latest``. Il documento è in italiano quindi prende la desinenza ``/it``. Questa impostazione permetterà alle note colorate di avere un titolo italiano (“Nota” al posto di “Note”, “Avvertimento” al posto di “Warning”, ecc.).

Esempio: come-creare-guida.readthedocs.io/it/latest

A questo punto il progetto di Github è compilato su Read the Docs.

Considerato che avevamo scelto come titolo del nostro progetto su Read the Docs: “linee guida open data comune vattelapesca”, l”URL compilato da Read the Docs per vedere il nostro progetto sarà: 

| ``linee-guida-open-data-comune-vattelapesca.readthedocs.io``


.. admonition:: Avviso di passing

    \ |STYLE0|\ 
    
    Se non ci sono errori commessi durante le procedure spiegate fino ad ora, tutto andrà a buon fine, e Read the Docs darà il messaggio in colore verde di «passing» al nostro progetto, significa che il nostro progetto è - quindi - online. La compilazione (build) su Read the Docs avviene con successo.


.. admonition:: Avviso di failing

    \ |STYLE1|\ 
    
    Diversamente Read the Docs alla sezione i miei progetti, darà un messaggio in colore rosso di «failed». In questo caso c’è qualche problema e bisogna ripercorrere tutti i passaggi fatti da quando si è iniziato a lavorare sul sito di Read the Docs. 
    La compilazione su Read the Docs ha incontrato qualche problema, e quando si presenta questo caso la prima cosa da fare è andare nel file ``conf.py`` dentro il repository del progetto su Github e verificare le istruzioni date. Generalmente se si presenta un problema nella compilazione di Read the Docs, il problema sta dentro questo file. Una volta individuato e risolto il problema automaticamente Read the Docs comincerà a compilare le istruzione del file ``conf.py`` di Github e dara il bollino verde di passed (cioè compilazione effettuata con successo).

Abbiamo completato tutte le procedure e ci possiamo godere il nostro documento nella nuova modalità di pubblicazione e visualizzazione su Read the Docs o Docs Italia.

[Questa pagina è \ |LINK2|\  del tutorial “\ |LINK3|\ ”].


.. bottom of content


.. |STYLE0| replace:: **Procedura andata a buon fine: «passing»**

.. |STYLE1| replace:: **Procedura con Errore: «failing»**


.. |LINK1| raw:: html

    <a href="http://readthedocs.io/" target="_blank">http://readthedocs.io</a>

.. |LINK2| raw:: html

    <a href="http://come-creare-guida.readthedocs.io/it/latest/_docs/capitolo2.html" target="_blank">ripresa da quella</a>

.. |LINK3| raw:: html

    <a href="http://come-creare-guida.readthedocs.io/it/latest/index.html" target="_blank">Tutorial pubblicazione Read the Docs su DocsItalia</a>

