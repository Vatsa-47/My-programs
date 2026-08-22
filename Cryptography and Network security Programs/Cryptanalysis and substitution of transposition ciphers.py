from collections import Counter
import matplotlib.pyplot as plt
english_freq={
    'E':12.7,
    'T':9.1,
    'A':8.2,
    'O':7.5,
    'I':7.0,
    'N':6.7
}
ciphertext=input("Enter the Ciphertext:")
ciphertext=''.join(ciphertext.split()).upper()
counter=Counter(ciphertext)
total_letters=sum(counter.values())
print("\n=====================")
print("     FREQUENCY ANALYSIS")
print("=======================\n")
print("{:<8}{:<10}{:<10}".format("Letter","Count","Percent"))
letters=[]
percentages=[]
for letter in sorted(counter.keys()):
    percent=(counter[letter]/total_letters)*100
    letters.append(letter)
    percentages.append(percent)
plt.figure(figsize=(10,5))
plt.bar(letters,percentages)
plt.title("Letter frequency Distribution")
plt.xlabel("Letters")
plt.ylabel("Frequency (%)")
plt.grid(axis='y')
plt.show()
print("\nTypical English Letter Frequencies")
print("--------------------------------")
for letter,value in english_freq.items():
    print(f"{letter} : {value}%")
print("\nObservations")
print("------------")
print("1. Frequency distribution of the ciphertext has been calculated")
print("2. Histogram shows occurence of each charecter")
print("3. Similar frequency patterns indicate vulnerability to frequency analysis")
print("4. Substitution and Rail fence ciphers preserve statstical charecterstics")

print("\nConclusion")
print("-----------")
print("The ciphertext is susceptible to frequency analysis because")
print("classical substitution and transpositiion ciphers preserve")
print("the statistical distribution of letters.")

