# Cerinta a II-a

Nume Echipa: 404NameNotFound

Echipa Adversa: gcodes [(link repo)](https://github.com/annemarie04/xor-project)

Parola Adversa: cataannevlad123

## Partea 1

Metoda Obtinere:

XOR input.txt cu output returneaza cheia repetata din proprietatile XORului (crackkey.py)

## Partea 2

Metoda Obtinere:

Bruteforcing: pentru fiecare lungime posibila a parolei, pentru fiecare pozitie am interat prin caracterele alfanumerice. Citeam cate un sir de bytes de lungimea parolei si XORam pozitia corespunzatoare din acesta cu pozitia curenta pe care o testam. Un rezultat era valid daca apartinea unui string de caractere valide obtinut din restrictille cerintei anterioare si trial-and-error SAU daca era caracter non-ASCII (am descoperit ca inputul adversar continea cateva caractere non-ASCII, am decis drept solutie temporara sa consider orice caracter non-ASCII drept valid si pare sa mearga pentru textul lor cel putin). Daca un caracter parcurgea intreg fisierul binar fara sa dea rezultate invalide atunci era considerat correct si era adaugat la parola. (truecrack.py)

-----------------
# Detalii Proiect

## Proiect realizat de:

Tava Andrei-Daniel

Duca Cosmina-Elena

Nedelcu Alexandru

-----------------
Utilizare: 

```python encrypt.py <cheie> <fisier_text_input> <fisier_output>```

```python decrypt.py <cheie> <fisier_input> <fisier_text_output>```
