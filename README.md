📧 Email Spam Detector

Ever opened your inbox and found messages like “You’ve won a million dollars!” or “Click here to claim your prize”?  
That’s spam — and we all hate it.

This project is built to help computers spot those unwanted emails automatically.  
It’s like giving your inbox a smart brain that says:  
> “Hey, this looks suspicious — probably spam!”


🌟 What This Project Does

This system looks at the text of an email and predicts whether it’s Spam or Not Spam (Ham).  
It learns from hundreds of example emails and figures out which words or patterns are common in spam messages.

It’s similar to how you learn:  
- If a message talks about *“lottery”, “prize”, or “click here”*, it’s probably spam.  
- If it says *“Meeting at 10 AM”*, it’s probably safe.


🧠 How It Works (In Simple Terms)

1. Learn from examples – We feed the computer a list of emails already marked as spam or not spam.  
2. Understand words – It turns each email into numbers (using a method called *TF-IDF*, which measures how important each word is).  
3. Make decisions – A machine learning model (Decision Tree) learns which patterns mean spam.  
4. Predict new emails – When you type or paste a new email, it decides: “Spam or Not Spam”.


🗂 Project Files Explained
|------------------------------|------------------------------------------------|
|             File             |                     Purpose                    |
|------------------------------|------------------------------------------------|
| `email.csv`                  | The dataset of real email messages             |
| `Email.ipynb`                | Notebook where the model is trained and tested |
| `email.py`                   | Simple Python script to test new emails        |
| `email_dt_model.pkl`         | The trained machine learning model             |
| `email_tfidf_vectorizer.pkl` | The word analyzer used to understand text      |
| `README.md`                  | You’re reading it right now!                   |
|------------------------------|------------------------------------------------|


💻 Model Accuracy 
The model was trained and tested on a dataset of emails and achieved an impressive accuracy of 96%, with 95% precision and 94% recall, making it quite reliable for basic spam detection tasks.

