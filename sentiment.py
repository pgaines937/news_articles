from nltk.corpus import stopwords
from itertools import chain
from nltk.corpus import wordnet
from collections import defaultdict
import pip
import csv
f = open('combined_dataset_verbose.csv')
csv_f = csv.reader(f)

negativeword="downfall,down,decrease,negative,fall,JEOPARDIZED,RECALCULATE,TESTIFY,QUESTIONABLE,IMPEDED,EXACERBATE,OVERSTATEMENT,SLANDER,NONPERFORMING,UNFOUNDED,WORST,ILLICIT,RENEGOTIATE, MANIPULATE, DISTURBING, CIRCUMVENT, PREJUDICED, APPARENTLY, FRIVOLOUS, REJECT, PROTESTED, REJECTS, DOWNSIZED, GRIEVANCE, REFILE, DISSENTING, FORECLOSED, GRATUITOUS,  UNPREDICTED, MISAPPLICATION, CLOSEOUT, COLLABORATES, OBLIGEE, DISSENTERS, FOREGO, WRITS, PLEDGORS, PRECIPITATED, IDLED, SUGGESTS, BAILEE, FRIENDLY, ARBITRAL, BREAKTHROUGHS, FAVORING, CERTIORARI, PERSISTS, ADJOURNMENTS, IGNORING, RECALCULATE"
negativeword=negativeword.split(',')
positiveword="increase,growth,rise,raise,up,UNMATCHED, OUTPERFORM, VOIDED, CONFIDENT, REWARDED, PROSPERITY, DISCREPANCY, RECTIFICATION, CRITICALLY, FORFEITABLE, ARBITRARY, TURMOIL, IMBALANCE, PROGRESSES, ANTECEDENT, OVERCHARGED, DURESS, MANIPULATION, DISTRESSED, DISSOLUTIONS, HAZARD,EXPROPRIATION, UNDERSTATE, UNFIT, PLEADINGS, INVESTIGATED, SOMETIME, ENCROACHMENT, MISSTATE,MUTANDIS, DEFRAUD, UNDEFINED, DELISTING, FORFEITS, UNCOVERS, MALPRACTICE, PRESUMES, GRANTORS, COLLAPSING, FALSELY, UNSOUND, REJECTIONS, WHEREABOUTS, DAMAGING, REASSIGNMENT, DISTRACTING, DISAPPROVED, STAGNANT, PREDECEASES, SAFE"
positiveword=positiveword.split(',')
neutral="FAVORABLE, VULNERABILITY, CLAIMS, ALTERATION, DISCONTINUING, BANKRUPTCY, DEPENDING, DEPENDING, ATTAINING, ISSIONS, CORRECTING, IMPROVES, GAIN, FLUCTUATION, DISCONTINUE, STATUTES, THEREUNTO, RISKY, RISKY, FLUCTUATES, SUBROGATION, NEGATIVELY, LOSE, ATTORNEY, REVISED, COULD, EXPOSURE, DEPENDENT, WILL, CONTRACTS, FAILURE, RISK, EASILY, PROFICIENCY, SUPERSEDES, ACCESSION, DULY, MAY, REMEDIED, VARIABLE, UNENFORCEABLE, RISKS, UNRESOLVED, VARIATIONS, COURTS, PROBLEM, VARIED, HEREBY, PREDICT"
neutral=neutral.split(',')
finalwordlist={}
negtivelist=[]
for w in negativeword:
    w=w.strip()
    negtivelist.append(w)
    synonyms = wordnet.synsets(w)
    lemmas = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
    lists=[x.encode('UTF8') for x in lemmas]
    negtivelist.extend(lists)
finalwordlist[-1]=negtivelist

positivelist=[]
for w in positiveword:
    w = w.strip()
    positivelist.append(w.lower())
    synonyms = wordnet.synsets(w.lower())
    lemmas = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
    lists=[x.encode('UTF8') for x in lemmas]
    positivelist.extend(lists)
finalwordlist[1]=positivelist


neutrallist=[]
for w in neutral:
    w = w.strip()
    neutrallist.append(w.lower())
    synonyms = wordnet.synsets(w.lower())
    lemmas = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
    lists=[x.encode('UTF8') for x in lemmas]
    neutrallist.extend(lists)
finalwordlist[0]=neutrallist
next(csv_f)
stop = set(stopwords.words('english'))
iter=0
fieldnames = ['publish_date','Date','sentiment_polarity','sentiment_subjectivity','Positive','Negative','Neutral','Class']
fp=open('final.csv', 'w')
fp1=open('date.csv', 'w')
fieldnames1 = ['Date']
writer = csv.DictWriter(fp, fieldnames=fieldnames)
writer1 = csv.DictWriter(fp1, fieldnames=fieldnames1)
writer.writeheader()
writer1.writeheader()
for row in csv_f:
    broken=[i for i in row[4].lower().split() if i not in stop]
    pos=len(set(finalwordlist[1])&set(broken))+1
    neg=len(set(finalwordlist[-1])&set(broken))+1
    neut=len(set(finalwordlist[0])&set(broken))+1
    totol=pos+neg+neut

    pos=1.0*pos/totol
    neg=1.0*neg/totol
    neut=1.0*neut/totol
    if row[5]>row[8]:
        label=0
    else:
        label=1
    writer.writerow({'publish_date': row[1], 'Date': row[2],'sentiment_polarity':row[0],'sentiment_subjectivity':row[3],'Positive': pos, 'Negative': neg, 'Neutral': neut,'Class':label})
    writer1.writerow({'Date':row[2]})
    iter+=1









