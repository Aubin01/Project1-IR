# 🌟 Ubuntu Information Retrieval System 🌟
`A project that implements an information retrieval system to query technical questions related to the Ubuntu operating system. Using PyTerrier, we explore and compare the traditional retrieval models BM25 and TF-IDF, evaluating their ability to retrieve the most relevant documents.`

# 🚀 Features
📄 Document Indexing: `Efficiently builds an inverted index of Ubuntu-related technical documents.`

🔍 Query Processing: `Supports both user-provided single queries and batch processing using predefined topics.`

⚖️ Model Comparison: `Implements and compares BM25 and TF-IDF retrieval models.`

📊 Evaluation: `Measures model performance using standard metrics like Precision, Recall, Mean Average Precision (MAP), and nDCG, evaluated against ground truth Qrels.`

# 🛠️ Technologies Used
🐍 Python: `The backbone of the project.`
🧰 PyTerrier: `For retrieval and indexing.`
📊 Ranx: `For model evaluation.`

# 📋 How to Run the Project
```bash
Clone the Repository: `git clone https://github.com/Aubin01/Project1-IR.git`
Install Dependencies: `Install the necessary libraries using pip`
- pip install pyterrier ranx
## 📥 Download Dataset
```bash
You can download the dataset from Google Drive by clicking [here](https://drive.google.com/drive/folders/1GGRWCf9cRP2DfrlUJ7ihZMKIOxQAC-wX?usp=drive_link).

# Run the Retrieval System: `Build the index, perform retrieval, and run evaluation:`
- `requirements: mkdir -p results`
# Time frame: It will take between 5 and 8 minutes for the both models' results to be written!
1. `Sample command to run the check.py`
```bash
python3 check.py \
 --answers_file data/Answers.json \
 --topics_1_file data/topics_1.json \
 --topics_2_file data/topics_2.json \
 --output_file_tfidf_1 results/output_tfidf_1.tsv \
 --output_file_tfidf_2 results/output_tfidf_2.tsv \
 --output_file_bm25_1 results/output_bm25_1.tsv \
 --output_file_bm25_2 results/output_bm25_2.tsv

 2. `Sample command to run the evaluate.py`
```bash
 python evaluate.py \
 --qrel_file /Users/aubinmugisha/Documents/Project1/data/qrel_1.trec \
 --run_file_tfidf /Users/aubinmugisha/Documents/Project1/results/result_tfidf_1.tsv \
 --run_file_bm25 /Users/aubinmugisha/Documents/Project1/results/result_bm25_1.tsv \
 --output_file_tfidf /Users/aubinmugisha/Documents/Project1/results/eval_tfidf.csv \
 --output_file_bm25 /Users/aubinmugisha/Documents/Project1/results/eval_bm25.csv

  3. `Sample command to run the evaluate.py`
```bash
python query.py \                                                                       
  --index_path /Users/aubinmugisha/Documents/Project1/src/index \                                    
  --query "How do I sync contacts on Ubuntu Touch?" \                                              
  --answers_file /Users/aubinmugisha/Documents/Project1/data/answers.json \                         
  --results_dir /Users/aubinmugisha/Documents/Project1/results
    

# 📂 Project Structure
```bash
Ubuntu/
├── data/
│   ├── Answers.json          # Dataset containing Ubuntu-related technical documents
│   ├── qrel_1.trec           # Ground truth relevance judgments (Qrels)
│   ├── topics_1.json         # Predefined queries (topics)
│   ├── topics_2.json         # Additional predefined queries
├── index/                    # Folder for storing the inverted index
├── results/
│   ├── bm25_evaluation.csv   # Evaluation metrics for BM25 model
│   ├── bm25_results_1.tsv    # Retrieval results from BM25 for topics_1
│   ├── bm25_results_2.tsv    # Retrieval results from BM25 for topics_2
│   ├── tfidf_evaluation.csv  # Evaluation metrics for TF-IDF model
│   ├── tfidf_results_1.tsv   # Retrieval results from TF-IDF for topics_1
│   ├── tfidf_results_2.tsv   # Retrieval results from TF-IDF for topics_2
├── src/
│   ├── check.py              # Script for testing or preprocessing
│   ├── evaluate.py           # Script to evaluate retrieval results
│   ├── load_data.py          # Utility functions to load and process data
│   ├── query.py              # script to run retrieval for user provided queries
└── README.md                 # Project documentation



