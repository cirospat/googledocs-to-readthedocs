
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

    Guarda, ad esempio, il feed RSS delle annotazioni postate dagli utenti come commenti ad una pagina del Libro bianco dell’innovazione della PA 2018: 
    \ |LINK5|\  

Esempio di visualizzazione del feed rss dei commenti ad una pagina (html) del Libro bianco innovazione PA 2018 

|REPLACE1|


.. code:: 

    <?xml version="1.0"?>
    <rss version="2.0"
         xmlns:atom="http://www.w3.org/2005/Atom"
         xmlns:dc="http://purl.org/dc/elements/1.1/">
      <channel>
        <title>Hypothesis Stream</title>
        <link>https://hypothes.is/stream</link>
        <atom:link href="https://hypothes.is/stream.rss" rel="self" type="application/rss+xml" />
        <description>The Web. Annotated</description>
        <pubDate>Sat, 15 Sep 2018 10:15:42 -0000</pubDate>
        <docs>http://blogs.law.harvard.edu/tech/rss</docs>
    
        
        <item>
           <title>2. Nuovi processi per la PA abilitante — Libro bianco innovazione 2018 ForumPA documentazione</title>
           <description>gli acquisti vanno anche agevolati soprattutto quelli del funzionamento delle segreterie che sono speso messi da parte costringendo il personale ad acquistare con il proprio stipendio la cancelleria mancante, evitando gli sprechi, con possibilità di fax telefoni fotocopiatrici scanner o altro a disposizione del dipendente che lavora nella segreteria oltre agli arredi base </description>
           <pubDate>Sat, 15 Sep 2018 10:15:42 -0000</pubDate>
           <guid isPermaLink="false">tag:hypothes.is,2015-09:TXlfhLjQEeitoSumpIxwIw</guid>
           <link>https://hypothes.is/a/TXlfhLjQEeitoSumpIxwIw</link>
           <dc:creator><![CDATA[LyLilly]]></dc:creator>
        </item>
        
        <item>
           <title>2. Nuovi processi per la PA abilitante — Libro bianco innovazione 2018 ForumPA documentazione</title>
           <description>Si ricorda soprattutto di tenere conto di tutto il cartaceo esami,lastre, tac nelle aziende sanitarie ospedaliere che anche dopo anni potrebbero tornare utili al paziente comprendendo anche il privato o convenzionato che abbiano una piattaforma comune e che il tutto non sia trasportato lontano dal luogo di residenza e di cura ma che sia tracciabile anche a distanza di anni </description>
           <pubDate>Sat, 15 Sep 2018 10:12:11 -0000</pubDate>
           <guid isPermaLink="false">tag:hypothes.is,2015-09:z97SPrjPEeiHFMtlTtD4UA</guid>
           <link>https://hypothes.is/a/z97SPrjPEeiHFMtlTtD4UA</link>
           <dc:creator><![CDATA[LyLilly]]></dc:creator>
        </item>
        
        <item>
           <title>2. Nuovi processi per la PA abilitante — Libro bianco innovazione 2018 ForumPA documentazione</title>
           <description>&lt;blockquote&gt;modello organizzativo unico e diffuso&lt;/blockquote&gt;che sia funzionante e che tenga conto dei lavoratori soprattutto a livello umano </description>
           <pubDate>Sat, 15 Sep 2018 10:09:36 -0000</pubDate>
           <guid isPermaLink="false">tag:hypothes.is,2015-09:c1nP-rjPEeiGNROjgbIDzw</guid>
           <link>https://hypothes.is/a/c1nP-rjPEeiGNROjgbIDzw</link>
           <dc:creator><![CDATA[LyLilly]]></dc:creator>
        </item>
        
        <item>
           <title>2. Nuovi processi per la PA abilitante — Libro bianco innovazione 2018 ForumPA documentazione</title>
           <description>nel rispetto e con rispetto dei lavoratori </description>
           <pubDate>Sat, 15 Sep 2018 10:08:27 -0000</pubDate>
           <guid isPermaLink="false">tag:hypothes.is,2015-09:Sh8NirjPEeiQB2N0A8sSng</guid>
           <link>https://hypothes.is/a/Sh8NirjPEeiQB2N0A8sSng</link>
           <dc:creator><![CDATA[LyLilly]]></dc:creator>
        </item>
        
        <item>
           <title>2. Nuovi processi per la PA abilitante — Libro bianco innovazione 2018 ForumPA documentazione</title>
           <description>&lt;blockquote&gt;mancanza di una cultura della trasparenza &lt;/blockquote&gt;la mancanza della cultura della trasparenza nasce dall&#39;incapacità organizzativa di diffondere informazioni, strategie, obiettivi.. si raggiungono gli obiettivi incuranti del personale e di come è stato coinvolto di solito ultimamente negativo in tutti i sensi (controlli personali, solo a determinate persone, verifica continua degli orari ed assillate soprattutto in strutture con pochissimo personale e mai aiutato con delle supplenze in caso di malattia, ferie,ecc. </description>
           <pubDate>Sat, 15 Sep 2018 10:03:14 -0000</pubDate>
           <guid isPermaLink="false">tag:hypothes.is,2015-09:j45mKLjOEeiFmJt0S9uMLg</guid>
           <link>https://hypothes.is/a/j45mKLjOEeiFmJt0S9uMLg</link>
           <dc:creator><![CDATA[LyLilly]]></dc:creator>
        </item>
        
        <item>
           <title>2. Nuovi processi per la PA abilitante — Libro bianco innovazione 2018 ForumPA documentazione</title>
           <description>&lt;blockquote&gt;nuove tecnologie&lt;/blockquote&gt;tecnologie valide, facilmente utilizzabili da tutta Italia con pc, stampanti, ecc che dialogano e con un costo abbordabile e senza costi aggiuntivi per eventuali modifiche dell&#39;utilizzo</description>
           <pubDate>Sat, 15 Sep 2018 09:57:24 -0000</pubDate>
           <guid isPermaLink="false">tag:hypothes.is,2015-09:vyFVQLjNEeizAk_yvufcTQ</guid>
           <link>https://hypothes.is/a/vyFVQLjNEeizAk_yvufcTQ</link>
           <dc:creator><![CDATA[LyLilly]]></dc:creator>
        </item>
        
        <item>
           <title>2. Nuovi processi per la PA abilitante — Libro bianco innovazione 2018 ForumPA documentazione</title>
           <description>&lt;blockquote&gt;telelavoro o forma di conciliazione&lt;/blockquote&gt;basta che la forma di conciliazione non si un ennesimo atto di mobbing, bossing,pressing ecc. nei confronti dei lavoratori, potrebbero essere esclusi i dirigenti amministrativi e contabili, tecnici sanitari e di radiologia, ma non il normale personale amministrativo contabile che necessita di forme di conciliazione soprattutto dal compimento del 55° anno di età e cioè verso la pensione </description>
           <pubDate>Sat, 15 Sep 2018 09:55:45 -0000</pubDate>
           <guid isPermaLink="false">tag:hypothes.is,2015-09:g7h1sLjNEeiuQPM57QMZlg</guid>
           <link>https://hypothes.is/a/g7h1sLjNEeiuQPM57QMZlg</link>
           <dc:creator><![CDATA[LyLilly]]></dc:creator>
        </item>
        
        <item>
           <title>2. Nuovi processi per la PA abilitante — Libro bianco innovazione 2018 ForumPA documentazione</title>
           <description>&lt;blockquote&gt;smart working (o Lavoro Agile) &lt;/blockquote&gt;Lo smart working non dovrebbe essere adottato dai dirigenti soprattutto amministrativi e contabili per cui è necessaria la quotidiana presenza, ma solo dai dipendenti che abbiano una reale necessità dovuta alla salute e alla gestione della famiglia presente e passata e che non abbiamo parenti ed affini che si prestino in sostituzione alle difficoltà</description>
           <pubDate>Sat, 15 Sep 2018 09:49:55 -0000</pubDate>
           <guid isPermaLink="false">tag:hypothes.is,2015-09:szanDrjMEeiTZRvPWGYxjw</guid>
           <link>https://hypothes.is/a/szanDrjMEeiTZRvPWGYxjw</link>
           <dc:creator><![CDATA[LyLilly]]></dc:creator>
        </item>
        
        <item>
           <title>2. Nuovi processi per la PA abilitante — Libro bianco innovazione 2018 ForumPA documentazione</title>
           <description>sempre  con una visione di coinvolgimento umana, sociale e non di esclusione, ma di inclusione anche dei dipendenti deboli o che hanno subito troppi capovolgimenti di mansioni e ufficio nella loro non riconosciuta carriera </description>
           <pubDate>Sat, 15 Sep 2018 09:46:17 -0000</pubDate>
           <guid isPermaLink="false">tag:hypothes.is,2015-09:MRhl0rjMEeiuPwOWtMJ9ug</guid>
           <link>https://hypothes.is/a/MRhl0rjMEeiuPwOWtMJ9ug</link>
           <dc:creator><![CDATA[LyLilly]]></dc:creator>
        </item>
        
        <item>
           <title>2. Nuovi processi per la PA abilitante — Libro bianco innovazione 2018 ForumPA documentazione</title>
           <description>importanti che i costi delle tecnologie non siano esosi ed a caspito della comunità e della società ma che siano controllati per essere efficienti, efficaci, semplici da utilizzare e con costi abbordabili </description>
           <pubDate>Sat, 15 Sep 2018 09:42:51 -0000</pubDate>
           <guid isPermaLink="false">tag:hypothes.is,2015-09:tssCvLjLEeiRDX_TrFg4Mw</guid>
           <link>https://hypothes.is/a/tssCvLjLEeiRDX_TrFg4Mw</link>
           <dc:creator><![CDATA[LyLilly]]></dc:creator>
        </item>
        
        <item>
           <title>2. Nuovi processi per la PA abilitante — Libro bianco innovazione 2018 ForumPA documentazione</title>
           <description>ottimo progetto, quello di Barcellona, assieme a CONSUL di Madrid. Anche in Italia ci difendiamo bene - ci sono diverse piattaforme simili - ma sono tutte iniziative civiche e non comunali (salvo per alcuni aspetti Bologna), come in Spagna, in grado di dare sostenibilità e solidità a questi progetti. 
    
    Ciò che conta e distingue le piattaforme, dal mio punto di vista, è tuttavia la finalità per cui sono messe online: segnalazioni, contributi...o processi decisionali? Oltre al bilancio partecipativo - che permette ai cittadini la sperimentazione di un percorso (e di una responsabilità) decisionale attraverso un budget - è possibile anche prevedere dei processi di &#34;obbligo politico&#34; (o di pressione sociale) attraverso cui le amministrazioni si impegnano non tanto a realizzare quanto chiesto ma almeno affrontare un tema prioritario - rispondendo a quesiti o organizzando degli incontri pubblici - che altrimenti rimarrebbe nel cassetto perché magari troppo scomodo. </description>
           <pubDate>Sat, 15 Sep 2018 09:21:54 -0000</pubDate>
           <guid isPermaLink="false">tag:hypothes.is,2015-09:yYPunrjIEeif8AcEL2kapg</guid>
           <link>https://hypothes.is/a/yYPunrjIEeif8AcEL2kapg</link>
           <dc:creator><![CDATA[ste.sto]]></dc:creator>
        </item>
        
        <item>
           <title>2. Nuovi processi per la PA abilitante — Libro bianco innovazione 2018 ForumPA documentazione</title>
           <description>&lt;blockquote&gt;Occorre avviare sperimentazioni serie e verificabili di auditing civico in diverse tipologie di enti, attraverso un investimento importante sia di risorse, sia di relazioni con i soggetti della cittadinanza organizzata. Occorre inoltre dare evidenza dei risultati delle sperimentazioni e discuterli con la dirigenza apicale degli enti.&lt;/blockquote&gt;Auditing civico non può funzionare senza una buona e funzionante organizzazione che non tenga conto solo degli obiettivi da raggiungere ma che crei un buon ambiente di lavoro per il lavoratore e per la cittadinanza se raggiungi lo stesso obiettivo con due persone mi pare che la situazione sia squilibrata dove magari un altro obiettivo è stato raggiunto con 100 persone e magari con l&#39;assunzione di personale giovane dirottato a favore di personaggi che non sanno gestire senza il loro apporto </description>
           <pubDate>Sat, 15 Sep 2018 08:59:04 -0000</pubDate>
           <guid isPermaLink="false">tag:hypothes.is,2015-09:mKyilrjFEeiGK7fYjXIHFw</guid>
           <link>https://hypothes.is/a/mKyilrjFEeiGK7fYjXIHFw</link>
           <dc:creator><![CDATA[LyLilly]]></dc:creator>
        </item>
        
        <item>
           <title>2. Nuovi processi per la PA abilitante — Libro bianco innovazione 2018 ForumPA documentazione</title>
           <description>&lt;blockquote&gt;un codice deontologico della professione. &lt;/blockquote&gt;codice deontologico della professione che tenga conto anche del lato umano del dipendente </description>
           <pubDate>Sat, 15 Sep 2018 08:48:40 -0000</pubDate>
           <guid isPermaLink="false">tag:hypothes.is,2015-09:JI_NbLjEEeiHBzfC_7fkTg</guid>
           <link>https://hypothes.is/a/JI_NbLjEEeiHBzfC_7fkTg</link>
           <dc:creator><![CDATA[LyLilly]]></dc:creator>
        </item>
        
        <item>
           <title>2. Nuovi processi per la PA abilitante — Libro bianco innovazione 2018 ForumPA documentazione</title>
           <description>&lt;blockquote&gt;compiti impossibili&lt;/blockquote&gt;compiti impossibili sempre diversi dalla segretaria, alla bibliotecaria, alla tecnica, alla &#34;badante&#34; di soggetti anziani, ecc. ed inoltre, continui trasferimenti interni alla struttura per chiusure di uffici, o altro soprattutto per le persone over 50 anni sono deleteri a livello professionale ed umano</description>
           <pubDate>Sat, 15 Sep 2018 08:47:31 -0000</pubDate>
           <guid isPermaLink="false">tag:hypothes.is,2015-09:-209PrjDEeiP_ish9r9BBw</guid>
           <link>https://hypothes.is/a/-209PrjDEeiP_ish9r9BBw</link>
           <dc:creator><![CDATA[LyLilly]]></dc:creator>
        </item>
        
        <item>
           <title>2. Nuovi processi per la PA abilitante — Libro bianco innovazione 2018 ForumPA documentazione</title>
           <description>&lt;blockquote&gt; i modi dell’attuazione.&lt;/blockquote&gt;I modi di attuazione non devono essere fugaci ed invisibili, perchè la parte migliore viene sempre offerta ad una parte di persone e gli altri sono allo scuro di tutto, inoltre, deve sempre contenere una parte umana a favore del lavoratore che ha problemi di famiglia o che ha avuti grazie </description>
           <pubDate>Sat, 15 Sep 2018 08:45:07 -0000</pubDate>
           <guid isPermaLink="false">tag:hypothes.is,2015-09:pdQtGrjDEeif61vIR4APdA</guid>
           <link>https://hypothes.is/a/pdQtGrjDEeif61vIR4APdA</link>
           <dc:creator><![CDATA[LyLilly]]></dc:creator>
        </item>
        
        <item>
           <title>2. Nuovi processi per la PA abilitante — Libro bianco innovazione 2018 ForumPA documentazione</title>
           <description>&lt;blockquote&gt;coaching.&lt;/blockquote&gt;il coaching funziona se c&#39;è una base umana e non solo lavorativa </description>
           <pubDate>Sat, 15 Sep 2018 08:41:27 -0000</pubDate>
           <guid isPermaLink="false">tag:hypothes.is,2015-09:Ip4YtrjDEeitl5sQx-ID9g</guid>
           <link>https://hypothes.is/a/Ip4YtrjDEeitl5sQx-ID9g</link>
           <dc:creator><![CDATA[LyLilly]]></dc:creator>
        </item>
        
        <item>
           <title>2. Nuovi processi per la PA abilitante — Libro bianco innovazione 2018 ForumPA documentazione</title>
           <description>&lt;blockquote&gt;retribuzioni&lt;/blockquote&gt;aumento delle retribuzioni a chi non effettua visite in extramoenia oltre a 2000 euro in campo medico, riconoscimento dei diritti ed esclusione dalle notti dei medici over60 anni 
    </description>
           <pubDate>Sat, 15 Sep 2018 08:40:14 -0000</pubDate>
           <guid isPermaLink="false">tag:hypothes.is,2015-09:9vPwZLjCEeiTYT9FhEe3wQ</guid>
           <link>https://hypothes.is/a/9vPwZLjCEeiTYT9FhEe3wQ</link>
           <dc:creator><![CDATA[LyLilly]]></dc:creator>
        </item>
        
        <item>
           <title>2. Nuovi processi per la PA abilitante — Libro bianco innovazione 2018 ForumPA documentazione</title>
           <description>&lt;blockquote&gt;comunità educanti&lt;/blockquote&gt;Le comunità educanti devo essere a loro volta umane e contrarie al bullismo, semimobbing, mobbing,  bossing , violenze psicologiche utilizzate per far carriera sia a livello di personale non docente/dirigente che a livello di semplici impiegati soprattutto per chi lo esercita o l&#39;ha esercitato in passato </description>
           <pubDate>Sat, 15 Sep 2018 08:31:47 -0000</pubDate>
           <guid isPermaLink="false">tag:hypothes.is,2015-09:yRrqpLjBEeiTXpM2dYVoSQ</guid>
           <link>https://hypothes.is/a/yRrqpLjBEeiTXpM2dYVoSQ</link>
           <dc:creator><![CDATA[LyLilly]]></dc:creator>
        </item>
        
        <item>
           <title>2. Nuovi processi per la PA abilitante — Libro bianco innovazione 2018 ForumPA documentazione</title>
           <description>&lt;blockquote&gt;formazione puntuale &lt;/blockquote&gt;La formazione puntuale deve inserirsi in un periodo di lavoro dove non si siano vacanze oppure prolungarsi di almeno 6 mesi per quella on line, corsi ad hoc e ben studiati per i lavoratori over 50 anni che hanno difficoltà di apprendimento e di memoria oltre al tempo che si deve dedicare alla famiglia e alle proprie condizioni fisiche </description>
           <pubDate>Sat, 15 Sep 2018 08:28:00 -0000</pubDate>
           <guid isPermaLink="false">tag:hypothes.is,2015-09:QgUg1LjBEeitlevRH5hrFA</guid>
           <link>https://hypothes.is/a/QgUg1LjBEeitlevRH5hrFA</link>
           <dc:creator><![CDATA[LyLilly]]></dc:creator>
        </item>
        
        <item>
           <title>2. Nuovi processi per la PA abilitante — Libro bianco innovazione 2018 ForumPA documentazione</title>
           <description>Sono d&#39;accordo di tenere conto dell&#39;esperienze maturate in ambito lavorativo e dell&#39;anzianità di servizio oltre ad un riconoscimento di CFU a livello di laurea per chi ha superano i 30 anni di servizio grazie </description>
           <pubDate>Sat, 15 Sep 2018 08:16:30 -0000</pubDate>
           <guid isPermaLink="false">tag:hypothes.is,2015-09:pq3Snri_EeiP_FOnvElAKA</guid>
           <link>https://hypothes.is/a/pq3Snri_EeiP_FOnvElAKA</link>
           <dc:creator><![CDATA[LyLilly]]></dc:creator>
        </item>
        
      </channel>
    </rss>
    

\ |STYLE1|\ :

\ |LINK6|\  ``url-di-readthedocs`` / ``pagina-specifica-del-documento-readthedocs``.html

Sono diversi modi per seguire i commenti sulle pagine di Read the Docs, e per attivare eventuali notifiche automatiche.

|

.. _h163c547219793f2d94347267c23426:

Funzionalità di collaborazione per le annotazioni di Hypothes.is
****************************************************************

A questo \ |LINK7|\  sono illustrate le funzionalità che abilitano alla collaborazione attraverso le annotazioni di Hypothes.is. Si tratta degli “\ |STYLE2|\ ” e “\ |STYLE3|\ ”.

In sostanza ora sono disponibili: 

* Public Layer 

* Open Group 

* Restricted Group 

* Private Group


+-------------------------+-----------------------------------------------------------------------------+--------------------------------------------------------------------------+----------------------------+-------------------------------------------------------------------+
|                         |Public Layer                                                                 |Open Group                                                                |Restricted Group            |Private Group                                                      |
+-------------------------+-----------------------------------------------------------------------------+--------------------------------------------------------------------------+----------------------------+-------------------------------------------------------------------+
|Who can read annotations?|Anyone                                                                       |Anyone                                                                    |Anyone                      |Only logged-in group members                                       |
+-------------------------+-----------------------------------------------------------------------------+--------------------------------------------------------------------------+----------------------------+-------------------------------------------------------------------+
|Who can post annotations?|Any logged-in user                                                           |Any logged-in user                                                        |Only logged-in group members|Only logged-in group members                                       |
+-------------------------+-----------------------------------------------------------------------------+--------------------------------------------------------------------------+----------------------------+-------------------------------------------------------------------+
|Who can join?            |N/A as anyone who is logged in to Hypothesis can annotate in the Public Layer|N/A as anyone who is logged in to Hypothesis can annotate in an Open Group|Invite only                 |Invite only: Group creator can share a link for users to join group|
+-------------------------+-----------------------------------------------------------------------------+--------------------------------------------------------------------------+----------------------------+-------------------------------------------------------------------+

The table above describes the configurations and permissions available to readers and annotators of the Public Layer and Open, Restricted, and Private Groups in Hypothesis.


|REPLACE2|


.. bottom of content


.. |STYLE0| replace:: **C'è un feed RSS per le note di ogni pagina HTML**

.. |STYLE1| replace:: **C'è anche in formato JSON**

.. |STYLE2| replace:: **open group**

.. |STYLE3| replace:: **restricted group**


.. |REPLACE1| raw:: html

    <iframe width="99%" height="600px" frameBorder="0" src="https://hypothes.is/stream.rss?uri=https://forumpa-librobianco-innovazione-2018.readthedocs.io/it/latest/2-nuovi-processi.html"></iframe>
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

.. |LINK7| raw:: html

    <a href="https://web.hypothes.is/blog/expanding-our-groups-capabilities/" target="_blank">link</a>

