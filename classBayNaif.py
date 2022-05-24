# -*- coding: utf-8 -*-
"""
Created on Wed May  6 09:42:04 2020

@author: elise

Classifieur Bayesien Naif
TP4

Générique tant que les catégories sont dans la dernière colonne des données
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


#-----------------
#Fonction qui extrait les données d'un fichier csv vers une matrice
def retrieveData(file,delim):
    
    data = np.loadtxt(file,delimiter = delim)
        
    return data

#------------------
#Fonction qui permet de récupérer la liste des catégories uniques du set de données
def findCat(data):
    
    categories = []
    
    for i in range(len(data)):
        categories.append(data[i][-1])
    
    return np.unique(np.array(categories))
    
    
#-------------------
#Fonction de calcul des mus : 1/N * Somme(valeurs)
def findMu(data, cat):
    
    mu = [0]*(len(data[0])-1)
    count = 0
    
    for j in range(len(data)):
        if data[j][-1] == cat:
            count +=1
            for k in range(len(data[j])-1):
                mu[k] += data[j][k]
    
    for l in range(len(mu)):
        mu[l]/= count
    
    return mu, count
 

#--------------------    
#Fonction de calcul des sigmas : 1/(N-1) * Somme((valeurs-moyenne)^2)
def findSigma(data, cat, mu, count):
    
    sigma = np.zeros(len(data[0])-1)
    
    for j in range(len(data)):
        if data[j][-1] == cat:
            for k in range(len(data[j])-1):
                sigma[k] += (data[j][k]-mu[k])**2
    
    for l in range(len(sigma)):
        sigma[l] = sigma[l]/(count-1)
        
    return sigma

#--------------------
#Fonction d'évaluation de l'appartenance aux catégories
def evaluate(mus,sigmas,counts,data):
    
    probs = [0]*len(counts)

    for i in range(len(counts)):
        
        probs[i] = counts[i]/sum(counts) #P(C=c)
        
        for j in range(len(mus)):
            
            probs[i] *= (1/(np.sqrt(2*np.pi*sigmas[i][j])))*(pow(np.e,(-1*pow(data[j]-mus[i][j],2)/(2*sigmas[i][j]))))

    return np.argmax(np.array(probs))

#--------------------
#Fonction d'affichage de catégories réelles et estimées    
def printResults(a,b,label):
    
    print("This is "+label[a])
    print("\tI should have found : "+label[int(b[-1]-1)]+"\n")
    
    if b[-1] == a+1 :
        return 0
    else :
        return 1
   
#---------------------
#Fonction d'affichage des gaussiennes et des données        
def plotCurves(mus,sigmas,counts,dataS,cat):
    
    t = np.linspace(0,10,1000)
    fig, axs = plt.subplots(4, figsize = (20,10))
    fig.suptitle('Distribution des données')
    
    for i in range(len(mus[0])):
    
        for j in range(len(counts)):
            
            axs[i].plot(t, stats.norm.pdf(t,mus[j][i],sigmas[j][i]), linewidth=2)
            
        for data in dataS :
            
            if data[-1] == cat[j] :
                axs[i].scatter(data[i],0) 
        
    plt.show()        
    
    
    
if __name__ == '__main__':

    
#Obtenir le nom du fichier contenant les données et les séparateurs entre les données :
#Ici : iris.csv et ;
    
        file = input("What is the name of the dataset file ?")
        delim = input("What character is delimiting these datas ?")
        
#Récupérer les données de ces fichiers et en extraire les différentes catégories
        
        data = retrieveData(file,delim)
        cat = findCat(data)
        
        mus = []
        sigmas = []
        counts = []
        
        
#Pour chaque catégorie, calculer le mu de chaque attribut, compter le nombre d'échantillon dans la catégorie
#Grâce à ces informations : calculer les sigmas pour chaque attribut
        for i in range(len(cat)):
            a,b = findMu(data,cat[i])
            mus.append(a)
            counts.append(b)
            sigmas.append(findSigma(data, cat[i], mus[i], counts[i]))
        
        
#Affichage des distributions gaussiennes pour chaque catégorie et pour chaque attribut
        plotCurves(mus,sigmas,counts,data,cat)
       
#Demande des noms des étiquettes (jusqu'ici numériques)
#Ici : -- Iris Setosa
#      -- Iris Versicolour
#      -- Iris Virginica
        
        
        label=[]
        print(cat)
        print("In the above order of appearance, what are the name of the labels ?")
        
        for i in range(len(counts)):
            label.append(input("N°"+str(i+1)+"  "))
        
        
#Récupération des données de test 
        file = input("What is the name of the dataset test file ?")
        delim = input("What character is delimiting these datas ?")
        
        a = retrieveData(file, delim)
        results = []
        error= np.zeros(len(cat))

#Pour chaque test effectué, affichage de la catégorie d'appartenance réelle et de la catégorie estimée
        
        for i in range(len(a)):
            results.append(evaluate(mus,sigmas,counts,a[i]))
            index = int(a[i][-1] - 1)
            error[index] += printResults(evaluate(mus,sigmas,counts,a[i]),a[i],label)
 
#Affichage du nombre d'erreurs faites par catégorie       
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        ax.bar(label,error)
        ax.set_yticks(range(0,counts[0],10))
        ax.set_ylabel('Erreurs')
        ax.set_title("Nombre d'erreurs par catégorie")
        plt.show()

