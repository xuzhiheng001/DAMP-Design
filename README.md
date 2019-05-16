# DAMP-Design
DAMP-Design-Liu
DAMP Primer Design Python Instruction

1. The Numpy package and CSV package are indispensable to run the whole program.
2. Almost all the parameters can be setup in the parameters.py.
3. The main program is DAMP Design.py to load the target sequence (at least 300 bp) in this folder. 
4. The target sequence can also be set in the parameters.py file. The default sequence is DNA sequence. For RNA target, use the complementary DNA (cDNA) sequence.
5. Besides the main function, the program is able to analyze the melting temperature (Tm), GC content, hairpin dimerization and self-dimerization of the sequence, as well as the free energy (△H, △S, △G) at the ends. The calculated GC content, Tm, △H, △S, and △G are shown in the Tm.py file. The hairpin dimerization is in the Hairpin file which can be also used to convert the sequence including reverse, complement, and reverse-complement. The self-dimerization is in the thrcom.py file.
6. Using the free energy (△H, △S, △G) at the ends, melting temperature (Tm) is calculated based on the oligonucleotide DNA nearest-neighbor thermodynamics. The equation is shown below.
T_m=∆H×1000/(∆S+R×ln(C/4) )-273.15+16.6log⁡[Na^+])
Where, R is gas constant (1.987cal/ºC/mol), C is oligonucleotide concentration (M), [Na+] is sodium ion concentration. 
The table for the ΔH, ΔS and ΔG is shown as below.
	Interaction	△H	△S	△G
	AA/TT	-8	-21.9	-1.2
	AT/TA	-5.6	-15.2	-0.9
	TA/AT	-6.6	-18.4	-0.9
	CA/GT	-8.2	-21	-1.7
	GT/CA	-6.6	-16.4	-1.5
	CT/GA	-8.8	-23.5	-1.5
	GA/CT	-9.4	-25.5	-1.5
	CG/GC	-11.8	-29	-2.8
	GC/CG	-10.5	-26.4	-2.3
	GG/CC	-10.9	-28.4	-2.1

7. The primer recognition sites are selected as the defined ranges of Tm, size and distance according the GC content of the target sequence, as shown below.

Feel free to contact us if you have any question. We are glad to answer your questions and make the program better. 

References:
Hilbers,C.W., Blommers,M.J.J., Haasnoot,C.A.G., van der Marel, G.A. and van Boom, J. H. (1987) Structure and folding of DNA and RNA hairpins. Anal Chem 327:70.
Serra,M.J., Lyttle,M.H., Axenson,T.J., Schadt.C.A. and Turner,D.H. (1993) Nucleic Acids Res 21:3845-3849.
Vallone,P.M., Paner,T.M., Hilario,J., Lane,M.J., Faldasz,B.D., Benight,A.S. (1999) Biopolymers. 50, 425-442.
