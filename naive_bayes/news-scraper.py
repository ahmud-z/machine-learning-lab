import requests
import pandas as pd
import json

def scrapeNewsArticle(url, filename):

    source = "prothom alo"
    response = requests.get(url)

    data = json.loads(response.content)
    dataset = []

    for item in data["items"]:
        if (
            "story" in item
            and "seo" in item["story"]
            and "meta-description" in item["story"]["seo"]
        ):
            dataset.append(
                {
                    "headline": item["story"]["headline"],
                    "description": item["story"]["seo"]["meta-description"],
                    "category": data["slug"],
                    "source": source,
                    "url": item["story"]["url"],
                }
            )

    df = pd.read_json(json.dumps(dataset))
    df.to_csv(f"{filename}.csv", mode="a", header=False, index=False)


def main():

    datasetName = "sports-news-dataset"  # The name you want to use for your dataset.
    newsAPI = "https://en.prothomalo.com/api/v1/collections/cricket-sports?offset=20&limit=100"

    scrapeNewsArticle(
        newsAPI,
        datasetName,
    )


main()