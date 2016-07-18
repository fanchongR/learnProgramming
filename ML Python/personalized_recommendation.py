critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0,
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}







from math import sqrt

def sim_distance(pref,person1,person2):
    share={}
    for key in pref[person1].keys():
        if key in pref[person2]:share[key]=1
    if len(share)==0:return 0
    distance=0
    for key in share.keys():
        distance+=( pref[person1][key]-pref[person2][key] )**2
    return 1/(1+sqrt(distance))

sim_distance(critics,'Lisa Rose','Gene Seymour')


def sim_pearson(prefs,p1,p2):
    si={}
    for key in prefs[p1]:
        if key in prefs[p2]:si[key]=1
    n = len(si)
    if n == 0 :return 1
    sum1=sum([prefs[p1][it] for it in si])
    sum2=sum([prefs[p2][it] for it in si])
    sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
    sum2Sq=sum([pow(prefs[p2][it],2) for it in si])
    pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
    num=pSum-(sum1*sum2/n)
    den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den==0: return 0
    r=num/den
    return r

sim_pearson(critics,'Lisa Rose','Gene Seymour')

def topMatches(pref,person,similarity=sim_pearson,n=5):
    scores=[ (similarity(pref,other,person),other) for other in pref if other!=person ]
    scores.sort()
    scores.reverse()
    return scores[0:n]

topMatches(critics,'Toby',n=3)






def getRecommendations(pref,person,similarity=sim_pearson):
    sim_sum={}
    total_sum={}
    for other in pref:
        if other == person:continue
        sim = similarity(pref,person,other)
        if sim<=0:continue
        for item in pref[other]:
            if item not in pref[person] or pref[person][item] == 0:
                sim_sum.setdefault(item,0)
                sim_sum[item]+=sim
                total_sum.setdefault(item,0)
                total_sum[item]+=sim*pref[other][item]
    ranking=[(total_sum[item]/sim_sum[item],item) for item in total_sum]
    ranking.sort()
    ranking.reverse()
    return ranking


getRecommendations(critics,'Toby')

##########################################################################

def transform(pref):
    output={}
    for person in pref:
        for item in pref[person]:
            output.setdefault(item,{})
            output[item][person] = pref[person][item]
    return output

#result: item -> (相似度，item)
def similarityItems(pref,n=10):
    result={}
    itemspref = transform(pref)
    for item in itemspref:
        result[item]=topMatches(itemspref,item,similarity=sim_distance,n=10)
    return result



def getRecommendationItems(pref,itemsim,user):
    simsum={}
    totals={}
    score=pref[user]
    for item in score:
        for (similarscore,item2) in itemsim[item]:
            if item2 in score:continue
            simsum.setdefault(item2,0)
            simsum[item2]+=similarscore
            totals.setdefault(item2,0)
            totals[item2]+=score[item]*similarscore
    ranking=[ (totals[item2]/simsum[item2],item2) for item2 in totals ]
    ranking.sort()
    ranking.reverse()
    return ranking

getRecommendationItems(critics,similarityItems(critics),'Toby')
