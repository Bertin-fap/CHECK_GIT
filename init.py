def download_nltk_data():
   """
 This function blabla

   """

    # Standard library imports

    import os # on bb
 
    # 3rd party imports
    import nltk
 
    for nltk_path in nltk.data.path: # if data are already downloaded than exit  
        if os.path.exists(nltk_path): return
    
    # no nltk data found then download them	
    nltk.download('averaged_perceptron_tagger')
    nltk.download('punkt')
    nltk.download('wordnet')

download_nltk_data()