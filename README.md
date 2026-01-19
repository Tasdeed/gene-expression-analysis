A data processing pipeline utilizing the GEOparse API to process gene expression datasets and visualize differences between samples (i.e., controls vs experimental).  

Technologies Used: 
  - numpy
  - pandas
  - biopython
  - matplotlib
  - seaborn
  - jupyter

To Run the Program (using my dataset): 

1. cd gene-expression-analysis
2. python3 -m venv venv
3. source venv/bin/activate
4. pip install -r requirements.txt
5. jupyter notebook
    - Open notebooks/01_data_exploration.ipynb
    - Run all cells

- To change to another dataset, Change `geo_accession = 'GSE68849'` to any GEO dataset ID
