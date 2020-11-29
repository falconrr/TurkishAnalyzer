# read in the subtitle  frequency file and add the data to dictionary where the key is the word form
import sys
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


IN = open("data/FreqCorpusTurkish.txt") # abrimos el corpus del español
dictlist = {}

for w in IN:
    data = w.split()
    key, value = data[0], data[1] # generamos un diccionario con las palabras más la frecuencia
    dictlist[key] = value
#print(list(dictlist.items())[:5])
IN.close()

# read through the stimuli file and print out. Aquí debemos declararlo en el command line así: cat results/wordlist.txt | python3 SubtitleToStimuliFinal3.py
inline = sys.stdin.readline() #
freqlist = []
cnt = 0
while inline:
    inline = inline.strip()
    if inline not in dictlist:
        inline = sys.stdin.readline()
        continue
    freq = dictlist[inline]
    freqlist.append((inline, freq))
    inline = sys.stdin.readline()


x = list(zip(*freqlist))[0] # sacamos la información que necesitamos
y = list(zip(*freqlist))[1]

tokens = []
tokens2 = []
for i in x: # creamos las dos tablas
    data2 = i.split()
    data2 = i.strip()
    tokens.append(data2)

for n in y:
    data3 = n.split()
    data3 = n.strip()
    tokens2.append(data3)

cnt = 0
while cnt < len(tokens):
    print(tokens[cnt], tokens2[cnt], sep = '\t') # imprimimos las palabras junto con su frecuencia en el español
    cnt += 1


num = [float(i) for i in y] # convertimos los strings a floats
mean = (sum(num)/len(num)) # generamos el promedio
print("\nThe global frequency is:", round(mean))

frecuencia = ('Lexicon')
promedio = [mean]

fig = plt.figure(figsize =(10, 7))
plt.boxplot(num) # boxplot = mejor
plt.xticks([1], ['Frequency'])
#plt.yticks(np.arange(0, 3000, 250))
plt.title('Global Frequency in Turkish')
plt.savefig("results/frequency")
