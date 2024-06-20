# -*- coding: utf-8 -*-
"""project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nwXKGXvkfi2vlI9tDjZGcipBNjQWm4ot
"""

# Commented out IPython magic to ensure Python compatibility.
from google.colab import drive

drive.mount('/content/gdrive')

# %cd gdrive/My Drive

!pip install transformers

!pip install sentencepiece

! pip install streamlit -q

!wget -q -O - ipv4.icanhazip.com

! streamlit run app1.py & npx localtunnel --port 8501