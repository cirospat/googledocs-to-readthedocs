
.. _hc7b2930471036563401d48693a206b:

Creare tabelle da esporre su Read the Docs
##########################################

Creare tabelle da esporre in pagina HTML su Read the Docs, utilizzando il linguaggio ``rST`` è un argomento non molto semplice.

Se la tabella è elementare e piccola, ad esempio costituita da poche colonne, l’uso di un servizio online come \ |LINK1|\  può essere la soluzione più veloce. Terminato l’editing dentro le celle si procede con la selezione del tasto reStructuredText e si ottiene il testo già formattato per essere usato su un file formato rST.

Se le tabelle si devono editare nativamente con la sintassi rST, la cosa si fa più complicata, vedi questa spiegazione \ |LINK2|\ : 

editando questi caratteri


.. code:: 

    +---+---+---+
    | a | b | c |
    +===+===+===+
    | e | f | g |
    +---+---+---+
    | h | i | l |
    +---+---+---+
    | m | n | o |
    +---+---+---+

si ha il seguente risultato

+---+---+---+
| a | b | c |
+===+===+===+
| e | f | g |
+---+---+---+
| h | i | l |
+---+---+---+
| m | n | o |
+---+---+---+

L’uso di \ |LINK3|\  di Drive per incorporare tabelle sulle pagine HTML può offrire una soluzione comoda, anche se didatticamente non rappresenta la soluzione ideale. Al fine di rendere l’uso di tabelle un'azione diffusa anche tra chi non ha consolidate esperienze nel campo della sintassi del linguaggio reStructuredText, la tabella del foglio Google rappresenta una via facile per l’esposizione su pagine HTML di Read the Docs.

|REPLACE1|

Vediamo come.

.. _h5d337e262a2375619107a586767119:

Crea la tabella su Google spreadsheet
*************************************

Chiunque è in grado di creare una tabella su Google spreadsheet. Utilizziamo liberamente anche i colori per delimitare le celle e per evidenziare il contenuto delle celle o del testo. Prendiamo ad esempio questa tabella: \ |LINK4|\  

.. _h584ff595b30387a4114425f9184e2b:

Pubblica la tabella sul web
***************************

La seconda azione da fare, dopo aver terminato l’editing nella tabella, è quella di pubblicare la tabella sul web. Le operazioni da compiere sono:

* seleziona in alto “\ |STYLE0|\ ”

* selezione “\ |STYLE1|\ ”

* clicca su “\ |STYLE2|\ ” e seleziona “\ |STYLE3|\ ” 

* seleziona e copia l’``indirizzo url`` generato: \ |LINK5|\  

.. _h655b521a672a67c1e47f5c6d12d7b:

Con GGeditor Markup Panel si crea un blocco HTML 
*************************************************

per incorporare l’indirizzo URL sopra riportato nella pagina HTML, quindi si edita:

<iframe width="100%" height="900px" frameBorder="0" src=”``indirizzo url``”></iframe>

.. code:: 

    <iframe width="100%" height="900px" frameBorder="0" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vRrShxVf6VZYXPeHR9e3NXsYZ_x8nrE1gGTuhqao4ERRm1XDYuXBO7G4vqDkk4u96BfLRAjekwZPk3K/pubhtml?widget=true&amp;headers=false"></iframe>

dove ``100%`` rappresenta l’ampiezza (larghezza) della tabella, e ``900px`` rappresenta l’altezza della colonna in pixel che troverà  posto nella pagina HTML di Read the Docs.

Il risultato sarà questo di seguito illustrato, cioè una tabella incorporata nella pagina HTML di Read the Docs.

L’unica cosa a cui porre attenzione è selezionare il limite destro della tabella al fine di farla rientrare interamente nella pagina HTML. Con 2-3 prove da fare si capirà quale è il limite massimo oltre il quale non andare.

|REPLACE2|

E’ una soluzione che permette di esporre tabelle avendo un file Google spreadsheet di origine che possiamo aggiornare quando vogliamo, e che si aggiornerà automaticamente sempre sulle pagine HTML di Read the Docs.

.. bottom of content


.. |STYLE0| replace:: **file**

.. |STYLE1| replace:: **pubblica sul web**

.. |STYLE2| replace:: **link**

.. |STYLE3| replace:: **pagina web**


.. |REPLACE1| raw:: html

    <img src="https://www.gstatic.com/images/branding/product/1x/sheets_48dp.png" />
.. |REPLACE2| raw:: html

    <iframe width="100%" height="900px" frameBorder="0" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vRrShxVf6VZYXPeHR9e3NXsYZ_x8nrE1gGTuhqao4ERRm1XDYuXBO7G4vqDkk4u96BfLRAjekwZPk3K/pubhtml?widget=true&amp;headers=false"></iframe>

.. |LINK1| raw:: html

    <a href="https://truben.no/table/" target="_blank">https://truben.no/table/</a>

.. |LINK2| raw:: html

    <a href="http://docutils.sourceforge.net/docs/user/rst/quickref.html#tables" target="_blank">http://docutils.sourceforge.net/docs/user/rst/quickref.html#tables</a>

.. |LINK3| raw:: html

    <a href="https://spreadsheets.google.com/" target="_blank">Google Spreadsheet</a>

.. |LINK4| raw:: html

    <a href="https://docs.google.com/spreadsheets/d/1z_W4tiBco8-p4n8uLL818jrgiPdqyXDUSq_2-Y65NN8/edit#gid=0" target="_blank">https://docs.google.com/spreadsheets/d/1z_W4tiBco8-p4n8uLL818jrgiPdqyXDUSq_2-Y65NN8/edit#gid=0</a>

.. |LINK5| raw:: html

    <a href="https://docs.google.com/spreadsheets/d/e/2PACX-1vRrShxVf6VZYXPeHR9e3NXsYZ_x8nrE1gGTuhqao4ERRm1XDYuXBO7G4vqDkk4u96BfLRAjekwZPk3K/pubhtml" target="_blank">https://docs.google.com/spreadsheets/d/e/2PACX-1vRrShxVf6VZYXPeHR9e3NXsYZ_x8nrE1gGTuhqao4ERRm1XDYuXBO7G4vqDkk4u96BfLRAjekwZPk3K/pubhtml</a>

