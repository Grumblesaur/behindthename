usages_text = '''
all:any
afr:african
alb:albanian
ara:arabic
arm:armenian
aze:azerbaijani
bas:basque
bre:breton
bul:bulgarian
cat:catalan
chi:chinese
cro:croatian
cze:czech
dan:danish
dut:dutch
eng:english
esp:esperanto
est:estonian
fin:finnish
fre:french
fri:frisian
gal:galician
geo:georgian
ger:german
gre:greek
haw:hawaiian
heb:hebrew
hun:hungarian
ice:icelandic
igb:igbo
ind:indian
ins:indonesian
iri:irish
ita:italian
jap:japanese
kaz:kazakh
khm:khmer
kor:korean
lat:latvian
lim:limburgish
lth:lithuanian
mac:macedonian
mao:maori
ame:native american
nor:norwegian
occ:occitan
per:persian
pol:polish
por:portuguese
rmn:romanian
rus:russian
sco:scottish
ser:serbian
slk:slovak
sln:slovenian
spa:spanish
swe:swedish
tha:thai
tur:turkish
ukr:ukrainian
urd:urdu
vie:vietnamese
wel:welsh
yor:yoruba
myth:mythology
grem:greek mythology:greek myth
romm:roman mythology:roman myth
celm:celtic mythology:celtic myth:celt mythology:celt myth
scam:scandinavian mythology:norse mythology:scandinavian myth:norse myth
indm:hindu mythology:hinduism:hindu myth
anci:ancient
grea:ancient greek
roma:ancient roman
cela:ancient celtic
gmca:ancient germanic
enga:anglo-saxon:anglo saxon
scaa:ancient norse:ancient scandinavian
bibl:biblical:bible
hist:history:historical
lite:literature
theo:theology
whim:whimsical
fairy:fey
goth:emo
hb:hillbilly
hippy:hippie
kk:kreatyve:made-up
rap:rapper
trans:transformer:robots in disguise
witch:witch
wrest:wrestler
fntsy:fantasy
fntsg:gluttakh
fntsm:monstrall
fntsr:romanto
fntss:simitiq
fntst:tsang
fntsx:xalaxxi
'''

def load():
  usages = {}
  for line in usages_text.splitlines():
    if not line.strip():
      continue
    nametypes = list(map(lambda s: s.strip(), line.split(':')))
    key = nametypes[0]
    synonyms = nametypes[1:]
    usages[key] = key
    for synonym in synonyms:
      usages[synonym] = key
  return usages
      
