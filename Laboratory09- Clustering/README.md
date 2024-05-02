# Laboratory week 10 (Laboratory 09)
## Resolving clustering problems with k-means algorithm

### Objectives:
1. Extracting features from text
2. Other tehnics for extracting features from text
3. Labeling text with emotions using kMeans (tool)
4. Implementing (own code) kMeans for clustering
5. Alternatives to k-means and performance analysis


## Useful links and Information:
1. Extracting features from text:
   - **Bag of Words** (basically a list of words in a text)
       - we can filter out some words (stop words) that are not useful
       - we can use the root of the words (stemming)
       - we count the number of times a word appears in a text
       - explanation : https://www.youtube.com/watch?v=IRKDrrzh4dE
   - **TF-IDF** (Term Frequency - Inverse Document Frequency)
       - TF-IDF(t,d)=TF(t,d)∗IDF(t)
       - TF(t,d) = number of times term t appears in document d ( times/words in document)
       - IDF(t) = log(N/df(t)) where: 
         - N = number of documents
         - df(t) = number of documents that contain term t
       - tf-idf is a measure of how important a word is to a document in a collection or corpus
       - If it is 0 it means that it is equally relevant for all documents
       - explanation : https://www.youtube.com/watch?v=vZAXpvHhQow
   - **Word2Vec** (word embeddings)
       - similar words are close in the vector space
       - it uses Continuous Bag of Words (CBOW) and Skip-gram
       - CBOW predicts the word given the context
       - Skip-gram predicts the context given the word
       - it speeds up with negative sampling
       - it randomly selects words to not predict
       - explanation: https://www.youtube.com/watch?v=viZrOnJclY0
2. **k-means algorithm**
      - it is an Unsupervised Learning algorithm
        - Unsupervised learning: 
          - there is no true outcome. It sees relationships between data
          - it is used for clustering
          - it is for reducing the number of features
          - filter abnormal data
      - k is the number of clusters
      - we randomly select k points as centroids
      - we assign each point to the nearest centroid
      - we recalculate the centroids
      - we repeat the process until the centroids do not change
      - we can use the elbow method to find the optimal number of clusters
      - we can use the silhouette score to evaluate the model
      - it does as many iterations as it needs to find the best centroids ( or how many you want)
      - Metrics of evaluation:
        - Purity: majority class in the cluster 
        - Rand Index: 
          - gain points when two points are in the same cluster
          - lose points when two points are in different clusters
          - RI = (TP + TN) / (TP + FP + FN + TN)
      - explanation: 
        - K-means: https://www.youtube.com/watch?v=4b5d3muPQmA 
        - Text Clustering: https://www.youtube.com/watch?v=WY5MdnhoG9w (University of Michigan)
      ![kmeans.png](images%2Fkmeans.png)
3. Other clustering algorithms:
   - **Hierarchical Clustering**
     - it is a tree of clusters
     - it is used for small datasets
   - Dendograms
     - it is a tree-like diagram that records the sequences of merges or splits
     - it is used to visualize the clustering
     - it is used to find the optimal number of clusters
     - compute pairwise similarity between clusters
     - identify closest pairs
     - merge pair into a new cluster
     - repeat until all data is in one cluster
     
      
      