# De raketvergelijking

Het is tijd om te vertrekken richting het intergalactische strijdtoneel. Het mensen van het ruimte-ondersteuningscommando laden je snel in een ruimtevaartuig  en maken zich klaar om te lanceren. Voor de lancering moet de raket, bestaande uit verschillend raketmodules, worden volgetankt met brandstof voor de raketmotor.

De benodigde brandstof om een gegeven module te lanceren, is gebaseerd op zijn massa. Om precies te zijn, om de brandstof voor een module te vinden, neem je zijn massa, deel je door drie, rond je af naar beneden en trek je er 2 van af.

Bijvoorbeeld:
- Voor een massa van 12, deel je door 3 en rond je af naar beneden om 4 te krijgen, trek je er dan 2 van af om 2 te krijgen.
- Voor een massa van 14, geeft delen door 3 en afronden naar beneden nog steeds 4, dus de benodigde brandstof is ook 2.
- Voor een massa van 1969 is de benodigde brandstof 654.
- Voor een massa van 100756 is de benodigde brandstof 33583.

De Adj. Brandstofmeter moet de totale brandstofbehoefte weten. Om deze te vinden, bereken je individueel de brandstof die nodig is voor de massa van elke module (zie input.txt), en tel je vervolgens alle brandstofwaarden bij elkaar op.

Wat is de som van de brandstofvereisten voor alle modules op je ruimtevaartuig?

## Deel 2
Tijdens de tweede Go / No Go controle stopt de Adjudant die verantwoordelijk is voor het dubbelchecken van de raketvergelijking de lanceersequentie. Blijkbaar ben je vergeten om extra brandstof toe te voegen voor de brandstof die je zojuist hebt toegevoegd.

Brandstof zelf heeft ook brandstof nodig, net als een module - neem zijn massa, deel door drie, rond naar beneden af en trek er 2 van af. Die brandstof heeft echter ook brandstof nodig, en die brandstof heeft ook brandstof nodig, enzovoort. Elke massa die negatieve brandstof zou vereisen, moet in plaats daarvan worden behandeld alsof het nul brandstof vereist; de resterende massa, indien aanwezig, wordt in plaats daarvan afgehandeld met wilskracht en discipline, wat geen massa heeft en buiten de scope van deze berekening valt.

Dus, voor elke modulemassa, bereken je zijn brandstof en tel je deze op bij het totaal. Behandel vervolgens de zojuist berekende brandstofhoeveelheid als de invoermassa en herhaal het proces, ga door totdat een brandstofvereiste nul of negatief is. Bijvoorbeeld:

- Een module met een massa van 14 vereist 2 brandstof. Deze brandstof vereist geen verdere brandstof (2 gedeeld door 3 en afgerond naar beneden is 0, wat zou leiden tot negatieve brandstof), dus de totale benodigde brandstof is nog steeds slechts 2.
- In eerste instantie vereist een module met een massa van 1969 654 brandstof. Vervolgens vereist deze brandstof nog eens 216 brandstof (654 / 3 - 2). 216 vereist dan nog eens 70 brandstof, die op zijn beurt 21 brandstof vereist, wat 5 brandstof vereist, wat geen verdere brandstof vereist. Dus de totale benodigde brandstof voor een module met een massa van 1969 is 654 + 216 + 70 + 21 + 5 = 966.
- De brandstof die vereist is voor een module met een massa van 100756 en zijn brandstof is: 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.

Wat is de som van de brandstofvereisten voor alle modules op je ruimtevaartuig wanneer ook rekening wordt gehouden met de massa van de toegevoegde brandstof? (Bereken de brandstofvereisten voor elke module afzonderlijk en tel ze allemaal aan het einde op.)


