# Google YMYL Content Checker (Text Classifier)
A Python script that analyzes text using the uClassify IAB taxonomy API. It classifies input content into topical categories, selects the highest-probability label, and evaluates whether it falls under YMYL (Your Money or Your Life) topics such as legal, finance, or health, returning a safety classification result. It can also support SEO analysis related to E-E-A-T signals by helping identify sensitive or high-trust content categories.

## 🚀 Features

- Classifies text using IAB taxonomy categories
- Extracts the most relevant topic with probability score
- Detects YMYL (sensitive/high-impact content) categories
- Returns structured output for automation or SEO analysis

## 🧠 How It Works

1. Sends input text to the uClassify API
2. Receives a list of possible categories with probabilities
3. Selects the highest-confidence category
4. Checks if the category is considered YMYL
5. Returns classification result + safety flag

## 📦 Example Output

```python
{
  "category": "family and relationships",
  "probability": 0.87,
  "ymyl": "YMYL warning"
}
````

## ⚙️ Installation

```bash
pip install requests
```


## 🔐 Setup (Important)

```bash
export UCLASSIFY_API_KEY="your_api_key_here"
```

Or create a `.env` file:

```
UCLASSIFY_API_KEY=your_api_key_here
```

## ▶️ Usage

```python
from script import classify_and_check_ymyl

text = "I need to file for divorce and understand court fees."

result = classify_and_check_ymyl(text)
print(result)
```

## 🛡️ YMYL Detection

The script flags content as **YMYL warning** if it belongs to sensitive categories such as:

* Legal services
* Finance and business
* Health and medical topics
* Government and education
* Insurance and retirement

These categories may require higher E-E-A-T standards in SEO contexts.

## 📌 Use Cases

* SEO content analysis
* Topic classification
* Risk/sensitivity detection
* E-E-A-T content auditing
* AI content filtering

## ⚠️ Disclaimer

This tool uses a third-party API (uClassify). Classification results are probabilistic and should not be treated as legal, financial, or medical advice.

## 🧑‍💻 Author

Built for content analysis, SEO research, and automated classification workflows.
