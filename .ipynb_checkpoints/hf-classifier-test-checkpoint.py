from transformers import pipeline

classifier = pipeline("sentiment-analysis") 
results = classifier("I've been waiting for a HuggingFace course my whole life.")
print(results)


results = classifier(["We are very happy to show you the Transformers library.", "We hope you don't hate it."])
for result in results:
    print(f"label: {result['label']}, with score: {round(result['score'], 4)}")