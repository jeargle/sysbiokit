# sysbiokit

Toolkit for playing around with systems biology models.  Based around problem sets from *An Introduction to Systems Biology* by Uri Alon as well as material from *Systems Biology: Properties of Reconstructed Networks* by Bernhard Palsson.


## Transcription Network

Transcription network models are built up from nodes (SimpleProduct and LogicProduct) and edges (Switch) that specify the connectivity and interaction rules for the time evolution of the system.

## Metabolic Network

Metabolic network models are represented as flux matrices (StoichioMatrix) with chemical rows and pathway columns specifying the mass transfer through the system.

## Dependencies

1. NumPy
2. matplotlib
