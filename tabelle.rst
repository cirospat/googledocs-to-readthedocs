
.. _hc7b2930471036563401d48693a206b:

Creare tabelle da esporre su Read the Docs
##########################################

Creare tabelle da esporre in pagina HTML su Read the Docs, utilizzando il linguaggio rST è un argomento non molto semplice.

Se la tabella è semplice, ad esempio costituita da poche colonne, l’uso di un servizio online come \ |LINK1|\  può essere la soluzione più veloce. Terminato l’editing dentro le celle si procede con la selezione del tasto reStructuredText e si ottiene il testo già formattato per essere usato su un file formato rST.

Se le tabelle si devono editare nativamente con la sintassi rST, la cosa si fa più complicata, vedi questa speiegazione \ |LINK2|\ : 

+---+---+---+
| a | b | c |
+===+===+===+
| e | f | g |
+---+---+---+
| h | i | l |
+---+---+---+
| m | n | o |
+---+---+---+

L’uso di Google Spreadsheet di Drive per incorporare tabelle sulle pagine HTML può offrire una soluzione comoda, anche se didatticamente non rappresenta la soluzione ideale.

Al fine di rendere l’uso di tabelle un'azione diffusa anche tra chi non ha consolidate esperienze nel campo della sintassi del linguaggio reStructuredText, le tabelle dei fogli Google rappresenta una via facile per l’esposizione su pagine HTML di Read the Docs.

Vediamo come.

.. _h5d337e262a2375619107a586767119:

Crea la tabella su Google spreadsheet
*************************************

Chiunque è in grado di creare una tabella su Google spreadsheet. Utilizziamo liberamente anche i colori per delimitare le celle e per evidenziare il contenuto delle celle o del testo. Prendiamo ad esempio questa tabella: \ |LINK3|\  

.. _h584ff595b30387a4114425f9184e2b:

Pubblica la tabella sul web
***************************

La seconda azione da fare, dopo aver terminato l’editing nella tabella, è quella di pubblicare la tabella sul web. Le operazioni da compiere sono:

* seleziona in alto “\ |STYLE0|\ ”

* selezione “\ |STYLE1|\ ”

* clicca su “\ |STYLE2|\ ” e seleziona “\ |STYLE3|\ ” 

* seleziona e copia l’url generato: \ |LINK4|\  

.. _h655b521a672a67c1e47f5c6d12d7b:

Con GGeditor Markup Panel si crea un blocco HTML 
*************************************************

per incorporare l’indirizzo URL sopra riportato nella pagina HTML, quindi si edita:

<iframe width="100%" height="1900px" frameBorder="0" src=”``indirizzo url``”></iframe>

.. code:: 

    <iframe width="100%" height="1900px" frameBorder="0" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vRrShxVf6VZYXPeHR9e3NXsYZ_x8nrE1gGTuhqao4ERRm1XDYuXBO7G4vqDkk4u96BfLRAjekwZPk3K/pubhtml?widget=true&amp;headers=false"></iframe>

Il risultato sarà questo di seguito illustrato, cioè una tabella incorporata nella pagina HTML di Read the Docs.

L’unica cosa a cui porre attenzione è selezionare il limite destro della tabella al fine di farla rientrare interamente nella pagina HTML. Con 2-3 prove da fare si capirà quale è il limite massimo oltre il quale non andare.

|REPLACE1|

E’ una soluzione che permette di esporre tabelle avendo un file Google spreadsheet di origine che possiamo aggiornare quando vogliamo, e che si aggiornerà automaticamente sempre sulle pagine HTML di Read the Docs.

.. bottom of content


.. |STYLE0| replace:: **file**

.. |STYLE1| replace:: **pubblica sul web**

.. |STYLE2| replace:: **link**

.. |STYLE3| replace:: **pagina web**


.. |REPLACE1| raw:: html

    <iframe width="100%" height="900px" frameBorder="0" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vRrShxVf6VZYXPeHR9e3NXsYZ_x8nrE1gGTuhqao4ERRm1XDYuXBO7G4vqDkk4u96BfLRAjekwZPk3K/pubhtml?widget=true&amp;headers=false"></iframe>

.. |LINK1| raw:: html

    <a href="https://truben.no/table/" target="_blank">https://truben.no/table/</a>

.. |LINK2| raw:: html

    <a href="http://docutils.sourceforge.net/docs/user/rst/quickref.html#tables" target="_blank">http://docutils.sourceforge.net/docs/user/rst/quickref.html#tables</a>

.. |LINK3| raw:: html

    <a href="https://docs.google.com/spreadsheets/d/1z_W4tiBco8-p4n8uLL818jrgiPdqyXDUSq_2-Y65NN8/edit#gid=0" target="_blank">https://docs.google.com/spreadsheets/d/1z_W4tiBco8-p4n8uLL818jrgiPdqyXDUSq_2-Y65NN8/edit#gid=0</a>

.. |LINK4| raw:: html

    <a href="https://docs.google.com/spreadsheets/d/e/2PACX-1vRrShxVf6VZYXPeHR9e3NXsYZ_x8nrE1gGTuhqao4ERRm1XDYuXBO7G4vqDkk4u96BfLRAjekwZPk3K/pubhtml" target="_blank">https://docs.google.com/spreadsheets/d/e/2PACX-1vRrShxVf6VZYXPeHR9e3NXsYZ_x8nrE1gGTuhqao4ERRm1XDYuXBO7G4vqDkk4u96BfLRAjekwZPk3K/pubhtml</a>

