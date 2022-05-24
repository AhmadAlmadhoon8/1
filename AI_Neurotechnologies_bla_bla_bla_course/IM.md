# Innovation methodology 

## Sources

https://en.wikipedia.org/wiki/TRIZ

https://altshuller.ru/triz/ariz85v.asp

https://www.youtube.com/watch?v=XKYsteB-KPk

https://en.wikipedia.org/wiki/Software_development_process

The proposed innovation methodology is based on the ARIZ process (Algorithm of the solution of  inventory problems (in Russian)) and Software development life-cycle (SDL).
The SDL contains the following phases analysis, design, development and validation phases, but here we take in account only analysis, design and early prototyping, for the reason that they are affected by ARIZ process.
The picture below contains simple waterfall SDL, below we indicate that with the influence of ARIZ it convolves into double spiral process.

![Innovation methodology](Innovation_methodology-TRIZ_LS.png)


## Analysis and IFR

The fist phase of the SDL usually contains the context description that corresponds ARIZ context and context time steps.

Functional and non functional requirements contains as well as "traditional" descriptions also the description of Ideal Final Result (IFR) in the following form:

	The X element, without additional complications of the system preserving all the useful functions of the system 
	does following:
		[useful actions] 
	in [the context of the system] during [the context time].

## Design 

The design starts with the High level view (HLD) where we broadly try to understand the possible solution having functional and non functional requirements in hand as well as IFR.

Firstly we have to identify the technical contradiction (TC) in the form:

	IF [brief solution description]
	THEN [positive results]
	BUT [negative consequences]

## Double spiral life-cycle

![2 spiral process](Innovation_methodology-2_spiral.png)


## 40 principles of invention
https://altshuller.ru/triz/technique1.asp

http://www.ipface.org/pdfs/reading/TRIZ_Principles.pdf

### Principle 1. Segmentation 
(**model of 6: Divide and conquer**)

A. Divide an object into independent parts.

### Principle 5. Merging
(**model of 6: Correlation**)


A - Bring closer together (or merge) identical or similar objects or
operations in space.
Close to the separate the concerns principle.

### Principle 6. Universality
(**model of 6:  Elevation**)

...

### Principle 7. Russian Dolls “Nested Doll”

B - Place multiple objects inside others

### Principle 10. Preliminary Action
(**model of 6: Planing, Logical reasoning**)

...

### Principle 11. Beforehand Cushioning
(**model of 6: Planing**)

Back up!


### Principle 13. “The Other Way Round”
(**model of 6: Reformulation, Reasoning by analogy**)

Inverse dependency.


### Principle 20. Continuity of Useful Action.

B - Eliminate all idle or intermittent actions or work
Booted notebooks use.
...

### Principle 22. Blessing in Disguise
(**model of 6: Reformulation**)

A - Use harmful factors (particularly, harmful effects of the
environment or surroundings) to achieve a positive effect

Use arctic cold to cool a data-center.

### Principle 23. Feedback


### Principle 24. Intermediary

Proxy objects.

### Principle 25. Self-service

Self-test. 

### Principle 26. Copying
(**model of 6: Reformulation, Simulation, Use external representations**)

Reformulation.
Using computational models.