# General Notes for Hugging Face

## login to CLI
- check to see if logged in with ```huggingface-cli whoami```
- if not logged in with use ```huggingface-cli login ```

## Welcome Screen

Here is the link to the [Welcome Screen](https://huggingface.co/welcome)

# running through the following tutorials
Transformers provides APIs and tools to easily download and train state-of-the-art pretrained models. Using pretrained models can reduce your compute costs, carbon footprint, and save you the time and resources required to train a model from scratch. These models support common tasks in different modalities, such as:
- 📝 Natural Language Processing: text classification, named entity recognition, question answering, language modeling, summarization, translation, multiple choice, and text generation.
- 🖼️ Computer Vision: image classification, object detection, and segmentation.
- 🗣️ Audio: automatic speech recognition and audio classification.
- 🐙 Multimodal: table question answering, optical character recognition, information extraction from scanned documents, video classification, and visual question answering.

[tutorials on transformers](https://huggingface.co/docs/transformers/en/index)



## Keras Error

RuntimeError: Failed to import transformers.models.distilbert.modeling_tf_distilbert because of the following error (look up to see its traceback):
Your currently installed version of Keras is Keras 3, but this is not yet supported in Transformers. Please install the backwards-compatible tf-keras package with `pip install tf-keras`.

## Speach from audio
there is an error: ```ValueError: ffmpeg was not found but is required to load audio files from filename```

you must install ffmpgeg.  I installed via ```brew install ffmpeg```, which took quite a while withy many dependencies.

Validate by running ```ffmpeg``` after install

## Huggingface Cache
The tutorials download pre-trained models..  Make sure your machine has space. For just the pipeline tutorial, it used 9.1 GB
The chache is located here ```~/.cache/huggingface```

# my take on the tutorials

## pipelines
following [Pipelines for inference](https://huggingface.co/docs/transformers/en/pipeline_tutorial)
Jupyter Lab File: ```hf-pipeline-tutorial.ipynb```
## Preprocess data
following [Preprocess](https://huggingface.co/docs/transformers/en/preprocessing)
Jupyter Lab File: ```hf-preprocess-tutorial.ipynb```

