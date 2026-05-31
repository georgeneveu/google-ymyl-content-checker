"""
YMYL Content Classifier (IAB Taxonomy API)

This script classifies a single sentence into a topic category using the uClassify IAB taxonomy API.
It then checks whether the content falls under YMYL (Your Money or Your Life) categories such as legal, finance, or health topics.

Useful for:
- SEO content analysis
- E-E-A-T evaluation support
- Content risk classification
"""

import os
import requests

# =========================
# API KEY SETUP
# =========================
# Get your API key here:
# https://www.uclassify.com/account/register

API_KEY = os.getenv("UCLASSIFY_API_KEY")  # store key in environment variables


# =========================
# SAMPLE INPUT
# =========================
TEXT_TO_CLASSIFY = "I need help understanding divorce filing fees in my state."


# =========================
# CLASSIFICATION FUNCTION
# =========================
def classify_text_top_category(text: str):
    """
    Sends text to the uClassify API and returns the top predicted category.
    """

    url = "https://api.uclassify.com/v1/uclassify/iab-taxonomy-v2/classify/"

    headers = {
        "Authorization": f"Token {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        url,
        headers=headers,
        json={"texts": [text]},
        timeout=10
    )

    data = response.json()

    classifications = data[0].get("classification", [])

    if not classifications:
        return None

    # pick highest probability category
    top_category = max(classifications, key=lambda x: x["p"])

    return top_category["className"], top_category["p"]


# =========================
# YMYL CHECKER
# =========================
def check_ymyl(category_name: str) -> str:
    """
    Checks if a category belongs to YMYL-sensitive topics.
    """

    ymyl_prefixes = [
        "personal finance_", "business and finance_",
        "medical health_", "healthy living_",
        "family and relationships_", "real estate_", "careers_",
        "news and politics_", "education_",
        "legal services_", "government_",
        "insurance_", "retirement planning_"
    ]

    return "YMYL warning" if any(category_name.startswith(p) for p in ymyl_prefixes) else "passed"


# =========================
# MAIN FUNCTION
# =========================
def classify_and_check_ymyl(text: str):
    """
    Runs classification + YMYL check and returns structured result.
    """

    result = classify_text_top_category(text)

    if result is None:
        return {"category": None, "probability": None, "ymyl": "unknown"}

    category, probability = result

    return {
        "category": category,
        "probability": probability,
        "ymyl": check_ymyl(category)
    }


# =========================
# RUN SCRIPT
# =========================
result = classify_and_check_ymyl(TEXT_TO_CLASSIFY)
print(result)
