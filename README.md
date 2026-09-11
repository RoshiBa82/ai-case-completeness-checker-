# AI Case Completeness Checker

Slutprojekt för Building AI-kursen.

## Summary

Idén är att använda AI för att hjälpa till med den första kontrollen av handlingar i ett ärende hos UHR. Systemet skulle kunna identifiera saknade eller dubbla handlingar, kontrollera om handlingar verkar tillhöra den sökande och ge en indikation på om ärendet verkar vara komplett för fortsatt handläggning.

Syftet är inte att ersätta handläggaren. AI skulle i stället fungera som ett stöd vid den första kontrollen av inkomna handlingar.

## Bakgrund

När ett ärende handläggs kan det innehålla flera olika handlingar. Innan ärendet kan gå vidare för utredning behöver de inkomna handlingarna kontrolleras för att se om de handlingar och uppgifter som behövs finns med. Vad är egentligen de handlingarana?

Den första kontrollen kan innebära mycket manuellt och återkommande arbete, dvs.snabbgranskning. Tanken med projektet är därför att använda AI för att göra denna del av arbetet enklare och snabbare.

Systemet skulle till exempel kunna hjälpa till att svara på frågor som:

- Vilken typ av handling har skickats in? (examensbevis - transcrip -  yrkesmässig översättningar - verifiering osv.) 
- Finns ett officiellt examensbevis och transcrip med? 
- Innehåller handlingarna uppgifter om studentens personuppgifter , utbildning, lärosäte och examensår. Signatur och exemplar dessutom?
- Verkar namnet eller andra uppgifter på handlingen stämma överens med den sökande i ärendet?
- Har samma handling skickats in mer än en gång?
- Saknas någon viktig handling?
- Verkar ärendet innehålla tillräckligt med handlingar för att kunna gå vidare till handläggning?

AI:n skulle inte fatta det slutliga beslutet. Den skulle i stället uppmärksamma möjliga problem som en handläggare kan kontrollera.

## Hur används lösningen?

Ett möjligt arbetsflöde skulle kunna se ut så här:

1. Handlingar kommer in i ett ärende.
2. AI:n läser och analyserar handlingarna.
3. Systemet identifierar vilken typ av handling det är.
4. Relevant information hämtas från handlingarna.
5. Systemet jämför handlingarna med den information och de handlingar som förväntas i ärendet.
6. Systemet markerar möjliga saknade, dubbla eller felaktiga handlingar.
7. Systemet ger en indikation på om ärendet verkar vara komplett.
8. Handläggaren granskar resultatet och gör den slutliga bedömningen.

Ett exempel på hur resultatet skulle kunna visas:

**Ärendestatus: Möjlig handling saknas**

- Examensbevis för bachelor och master: Hittat
- Transcrip för master: Hittad
- Identitetshandling: Hittad
- Översättningar för examensbevis (bachelor och master) samt för Transcrip för bachelor och master : Hittat
- Obligatorisk handling - Transcrip (originalspråk) för bachelor: Saknas

Handläggaren kan sedan skicka en komplettering innan ärendet går vidare.

## Datakällor och AI-metoder

En möjlig prototyp skulle kunna använda anonymiserade exempel på handlingar och olika typer av dokument.

Projektet skulle kunna använda flera AI-metoder:

- Maskininlärning
- Dokumentklassificering
- Optical Character Recognition (OCR)
- Natural Language Processing (NLP)
- Likhetsanalys för att hitta möjliga dubbletter

OCR kan användas för att läsa text från inskannade handlingar eller bilder.

Dokumentklassificering kan hjälpa till att identifiera vilken typ av handling som har skickats in.

NLP kan användas för att hitta information som namn, lärosäte, utbildning och datum.

Likhetsanalys kan användas för att identifiera handlingar som är identiska eller mycket lika varandra.

I en verklig tillämpning behöver informationen hanteras med stor försiktighet eftersom handlingarna kan innehålla personuppgifter.

## Utmaningar

Det finns flera utmaningar med idén.

Handlingar kan se mycket olika ut från olika länder. De kan ha olika format, språk, layouter och kvalitet. Vissa handlingar kan också vara inskannade bilder eller svåra att läsa.

Det kan också vara svårt för ett AI-system att avgöra om en handling verkligen tillhör den sökande. En skillnad i namn behöver till exempel inte alltid betyda att handlingen är felaktig.

En annan utmaning är att avgöra när ett ärende är komplett. Olika typer av ärenden kan kräva olika handlingar. Systemet skulle därför behöva tydliga regler och bra exempel att utgå från.

Integritet och informationssäkerhet är också viktiga frågor. Ett verkligt system skulle behöva följa relevanta regler för hantering av personuppgifter och handlingar.

På grund av dessa begränsningar bör AI:n användas som ett beslutsstöd. En handläggare ska kunna granska resultatet och göra den slutliga bedömningen.

## Nästa steg

Ett första steg skulle kunna vara att bygga en liten prototyp med anonymiserade exempel på handlingar.

Prototypen skulle kunna börja med ett begränsat antal handlingstyper och några enkla kontroller, till exempel:

- Identifiera vilken typ av handling som har skickats in
- Kontrollera om de handlingar som behövs finns med
- Identifiera möjliga dubbletter
- Kontrollera om grundläggande uppgifter verkar stämma överens med den sökande

Om prototypen fungerar bra skulle den senare kunna utvecklas för att hantera fler handlingstyper och mer avancerade kontroller.

## Tack

Idén till projektet är inspirerad av praktiska utmaningar kring hantering av handlingar och handläggning av ärenden.

Projektet är framtaget som slutprojekt för Building AI-kursen vid Helsingfors universitet och Reaktor.
