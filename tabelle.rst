
.. _h750645f49301867ace3d5a611ee:

Inserimento di tabelle nel documento
####################################

Creare tabelle da esporre in pagina HTML su Read the Docs, utilizzando il linguaggio ``rST`` è un argomento non molto semplice.

Se la tabella è elementare e piccola, ad esempio costituita da poche colonne, l’uso di un servizio online come \ |LINK1|\  può essere la soluzione più veloce. Terminato l’editing dentro le celle si procede con la selezione del tasto reStructuredText e si ottiene il testo già formattato per essere usato su un file formato rST.

Se le tabelle si devono editare nativamente con la sintassi rST, la cosa si fa più complicata, vedi questa spiegazione \ |LINK2|\ : 

editando questi caratteri:

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

|

.. _h8039466e4d50665f3803d3b235c1719:

Con ``GGeditor`` inseriamo tabelle nel Google doc
*************************************************

Con GGeditor possiamo inserire tabelle dentro il nostro documento Google, quindi nel momento del “commit” la tabella sarà automaticamente trasformata in sintassi rST dentro il file rST di Github.

Al momento del “commit” ``GGeditor`` ci dà due possibilità:

* Tables are converted to reStructuredText table markups.

* \ |LINK3|\ . This option would generate table with HTML <TABLE>. Useful for those who utilizes the readthedocs.org as a blog system.


..  Hint:: 

    You can set background-color for header rows by assign CSS in the following file inside Github repo:
    
    ``/docs/static/theme_overrides.css.`` 
    
    For example:
    
    \ |STYLE0|\ 
       background-color: #f0f0f0;
    
    }

|

.. _h101e4e179297547f62624d28137347:

Creare la tabella su Google spreadsheet e poi importarla dentro Google doc
**************************************************************************

L’uso di \ |LINK4|\  di Drive per incorporare tabelle sulle pagine HTML può offrire una soluzione comoda, anche se didatticamente non rappresenta la soluzione ideale. Al fine di rendere l’uso di tabelle un'azione diffusa anche tra chi non ha consolidate esperienze nel campo della sintassi del linguaggio reStructuredText, la tabella del foglio Google rappresenta una via facile per l’esposizione su pagine HTML di Read the Docs.

|REPLACE1|

Vediamo come.

Chiunque è in grado di creare una tabella su Google spreadsheet. Utilizziamo liberamente anche i colori per delimitare le celle e per evidenziare il contenuto delle celle o del testo. Prendiamo ad esempio questa tabella: \ |LINK5|\  

.. _h584ff595b30387a4114425f9184e2b:

Pubblica la tabella sul web
===========================

La seconda azione da fare, dopo aver terminato l’editing nella tabella, è quella di pubblicare la tabella sul web. Le operazioni da compiere sono:

* seleziona in alto “\ |STYLE1|\ ”

* selezione “\ |STYLE2|\ ”

* clicca su “\ |STYLE3|\ ” e seleziona “\ |STYLE4|\ ” 

* seleziona e copia l’``indirizzo url`` generato: \ |LINK6|\  

.. _h1956172479502b736333c3d72e83:

Con ``GGeditor`` Markup Panel si crea un box HTML 
==================================================

Si incorpora l’indirizzo URL sopra riportato nella pagina HTML, quindi si edita:

<iframe width="100%" height="900px" frameBorder="0" src=”``indirizzo url``”></iframe>

.. code:: 

    <iframe width="100%" height="900px" frameBorder="0" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vRrShxVf6VZYXPeHR9e3NXsYZ_x8nrE1gGTuhqao4ERRm1XDYuXBO7G4vqDkk4u96BfLRAjekwZPk3K/pubhtml?widget=true&amp;headers=false"></iframe>

dove ``100%`` rappresenta l’ampiezza (larghezza) della tabella, e ``900px`` rappresenta l’altezza della colonna in pixel che troverà  posto nella pagina HTML di Read the Docs.

Il risultato sarà questo di seguito illustrato, cioè una tabella incorporata nella pagina HTML di Read the Docs.

L’unica cosa a cui porre attenzione è selezionare il limite destro della tabella al fine di farla rientrare interamente nella pagina HTML. Con 2-3 prove da fare si capirà quale è il limite massimo oltre il quale non andare.

|REPLACE2|

E’ una soluzione che permette di esporre tabelle avendo un file Google spreadsheet di origine che possiamo aggiornare quando vogliamo, e che si aggiornerà automaticamente sempre sulle pagine HTML di Read the Docs.

.. bottom of content


.. |STYLE0| replace:: **.wy-table-responsive table th {**

.. |STYLE1| replace:: **file**

.. |STYLE2| replace:: **pubblica sul web**

.. |STYLE3| replace:: **link**

.. |STYLE4| replace:: **pagina web**


.. |REPLACE1| raw:: html

    <img src="https://www.gstatic.com/images/branding/product/1x/sheets_48dp.png" />
.. |REPLACE2| raw:: html

    <iframe width="100%" height="900px" frameBorder="0" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vRrShxVf6VZYXPeHR9e3NXsYZ_x8nrE1gGTuhqao4ERRm1XDYuXBO7G4vqDkk4u96BfLRAjekwZPk3K/pubhtml?widget=true&amp;headers=false"></iframe>

.. |LINK1| raw:: html

    <a href="https://truben.no/table/" target="_blank">https://truben.no/table/</a>

.. |LINK2| raw:: html

    <a href="http://docutils.sourceforge.net/docs/user/rst/quickref.html#tables" target="_blank">http://docutils.sourceforge.net/docs/user/rst/quickref.html#tables</a>

.. |LINK3| raw:: html

    <a href="https://ggeditor.readthedocs.io/en/latest/table_in_html.html" target="_blank">with HTML tags</a>

.. |LINK4| raw:: html

    <a href="https://spreadsheets.google.com/" target="_blank">Google Spreadsheet</a>

.. |LINK5| raw:: html

    <a href="https://docs.google.com/spreadsheets/d/1z_W4tiBco8-p4n8uLL818jrgiPdqyXDUSq_2-Y65NN8/edit#gid=0" target="_blank">https://docs.google.com/spreadsheets/d/1z_W4tiBco8-p4n8uLL818jrgiPdqyXDUSq_2-Y65NN8/edit#gid=0</a>

.. |LINK6| raw:: html

    <a href="https://docs.google.com/spreadsheets/d/e/2PACX-1vRrShxVf6VZYXPeHR9e3NXsYZ_x8nrE1gGTuhqao4ERRm1XDYuXBO7G4vqDkk4u96BfLRAjekwZPk3K/pubhtml" target="_blank">https://docs.google.com/spreadsheets/d/e/2PACX-1vRrShxVf6VZYXPeHR9e3NXsYZ_x8nrE1gGTuhqao4ERRm1XDYuXBO7G4vqDkk4u96BfLRAjekwZPk3K/pubhtml</a>

